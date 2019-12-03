from django.http import HttpResponseRedirect
from django.views.generic import DetailView, FormView, ListView, DeleteView

from .forms import *


class MainPageView(ListView):
    template_name = "main_page.html"
    queryset = Bank.objects.all().order_by("money_count")
    context_object_name = "banks"


class BankCreateView(FormView):
    template_name = 'create_bank.html'
    form_class = CreateBankForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('/')


class MemberCreateView(FormView):
    template_name = 'create_member.html'
    form_class = CreateMemberForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('/')


class TransactionCreateView(FormView):
    form_class = CreateTransactionForm
    template_name = 'create_transaction.html'

    def form_valid(self, form):
        value = int(form.cleaned_data['value'])
        form.instance.bank = form.cleaned_data['member'].bank
        form.instance.save()
        self.update_money_count(form.instance.bank, form.instance.member, value)
        return HttpResponseRedirect('/')

    # Validates if any of counts are below zero and then if everything is ok
    # it updates money count due to transaction form

    def update_money_count(self, bank, member, value):
        if value > 0 and bank.money_count < value:
            return HttpResponseRedirect('/')
        elif value < 0 and member.money_count < abs(value):
            return HttpResponseRedirect('/')
        bank.money_count -= value
        bank.save()
        member.money_count += value
        member.save()


class MemberDetailView(DetailView):
    model = Member
    template_name = 'detail_page.html'
    context_object_name = 'member'
    pk_url_kwarg = 'member_pk'


class BankDeleteView(DeleteView):
    model = Bank
    template_name = 'delete.html'
    pk_url_kwarg = 'bank_pk'
    success_url = '/'


class MemberDeleteView(DeleteView):
    model = Member
    template_name = 'delete.html'
    pk_url_kwarg = 'member_pk'
    success_url = '/'


class TransactionDeleteView(DeleteView):
    model = Transaction
    template_name = 'delete.html'
    pk_url_kwarg = 'transaction_pk'
    success_url = '/'



