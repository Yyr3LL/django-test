from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView, FormView, ListView

from .models import *
from .forms import *


class MainPageView(ListView):
    template_name = "main_page.html"
    queryset = Bank.objects.all().order_by("money_count")
    context_object_name = "banks"


class MemberDetailView(DetailView):
    model = Member
    template_name = 'detail_page.html'
    context_object_name = 'member'
    pk_url_kwarg = 'member_pk'


def create_bank(request):
    form = CreateBankForm(request.POST)
    if request.method == "POST":
        if form.is_valid:
            form.save()
            return HttpResponseRedirect("/")
        else:
            form = CreateBankForm()
    return render(request, 'create_bank.html', {'form': form})


def create_member(request):
    form = CreateMemberForm(request.POST)
    if request.method == "POST":
        if form.is_valid:
            form.save()
            return HttpResponseRedirect("/")
        else:
            form = CreateMemberForm()
    return render(request, 'create_member.html', {'form': form})


class CreateTransactionView(FormView):
    form_class = CreateTransactionForm
    template_name = 'create_transaction.html'

    def form_valid(self, form):
        value = int(form.cleaned_data['value'])
        form.instance.bank = form.cleaned_data['member'].bank
        form.instance.save()
        self.update_money_count(form.instance.bank, form.instance.member, value)
        return HttpResponseRedirect('/')

    def update_money_count(self, bank, member, value):
        if value > 0 and bank.money_count < value:
            return HttpResponseRedirect('/')
        elif value < 0 and member.money_count < abs(value):
            return HttpResponseRedirect('/')
        bank.money_count -= value
        bank.save()
        member.money_count += value
        member.save()
