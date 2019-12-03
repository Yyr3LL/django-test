from django import forms
from django.db import models
from .models import Bank, Member, Transaction


class CreateBankForm(forms.ModelForm):
    # name = models.CharField(forms.ModelForm)
    # money_count = models.IntegerField()

    class Meta:
        model = Bank
        fields = ('name', 'money_count')


class CreateMemberForm(forms.ModelForm):
    # full_name = forms.CharField()
    # wallet = forms.IntegerField()

    class Meta:
        model = Member
        fields = ('full_name', 'money_count', 'bank')


class CreateTransactionForm(forms.ModelForm):
    bank = forms.HiddenInput()

    class Meta:
        model = Transaction
        fields = ('value', 'member')
