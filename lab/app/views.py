from django.urls import *
from django.shortcuts import redirect
from django.views.generic import DetailView, CreateView, ListView, DeleteView

from .forms import *


class MainPageView(ListView):
    template_name = "main_page.html"
    context_object_name = "banks"

    def get_queryset(self):
        return Bank.objects.all().order_by("money_count")


class BankCreateView(CreateView):
    template_name = 'create_bank.html'
    form_class = CreateBankForm

    def get_success_url(self):
        return reverse('main_page')


class MemberCreateView(CreateView):
    template_name = 'create_member.html'
    form_class = CreateMemberForm

    def get_success_url(self):
        return reverse('main_page')


class TransactionCreateView(CreateView):
    template_name = 'create_transaction.html'
    form_class = CreateTransactionForm

    def form_valid(self, form):
        value = int(form.cleaned_data['value'])
        form.instance.bank = form.cleaned_data['member'].bank
        form.instance.save()
        self.update_money_count(form.instance.bank, form.instance.member, value)
        return redirect('/')


    # Validates if any of counts are below zero and then if everything is ok
    # it updates money count due to transaction form

    def update_money_count(self, bank, member, value):
        if value > 0 and bank.money_count < value:
            return redirect('/')
        elif value < 0 and member.money_count < abs(value):
            return redirect('/')
        bank.money_count -= value
        bank.save()
        member.money_count += value
        member.save()


class MemberDetailView(DetailView):
    template_name = 'detail_page.html'
    model = Member
    context_object_name = 'member'
    pk_url_kwarg = 'member_pk'


class BankDeleteView(DeleteView):
    template_name = 'delete.html'
    model = Bank
    pk_url_kwarg = 'bank_pk'

    def get_success_url(self):
        return reverse('main_page')


class MemberDeleteView(DeleteView):
    template_name = 'delete.html'
    model = Member
    pk_url_kwarg = 'member_pk'

    def get_success_url(self):
        return reverse('main_page')


class TransactionDeleteView(DeleteView):
    template_name = 'delete.html'
    model = Transaction
    pk_url_kwarg = 'transaction_pk'

    def get_success_url(self):
        return reverse('main_page')

