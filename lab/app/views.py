from django.http import HttpResponseRedirect
from django.views.generic import DetailView, FormView, ListView

from .forms import *


# Main page with all the info

class MainPageView(ListView):
    template_name = "main_page.html"
    queryset = Bank.objects.all().order_by("money_count")
    context_object_name = "banks"


# Page with info about particular member by member_pk

class MemberDetailView(DetailView):
    model = Member
    template_name = 'detail_page.html'
    context_object_name = 'member'
    pk_url_kwarg = 'member_pk'


# Page where you add banks

class CreateBankView(FormView):
    template_name = 'create_bank.html'
    form_class = CreateBankForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('/')


# Page where you add members

class CreateMemberView(FormView):
    template_name = 'create_member.html'
    form_class = CreateMemberForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('/')


# Page where you add transactions

class CreateTransactionView(FormView):
    form_class = CreateTransactionForm
    template_name = 'create_transaction.html'

    # function that django call when form is valid

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
