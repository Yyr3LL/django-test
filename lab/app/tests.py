from django.test import TestCase

from .models import *
from . import service


class BankTestCase(TestCase):
    def setUp(self):
        Bank.objects.create(name="Some bank", money_count=10000)
        Bank.objects.create(name="Beach FastBank", money_count=3000)

    def test_bank_have_money(self):
        bank_1 = Bank.objects.get(name="Some bank")
        bank_2 = Bank.objects.get(name="Beach FastBank")
        self.assertEqual(bank_1.money_count > 0, True)
        self.assertEqual(bank_2.money_count > 0, True)


class TransactionTestCase(TestCase):
    def setUp(self):
        Bank.objects.create(
            name="Bank",
            money_count=500
        )
        Member.objects.create(
            full_name="Member",
            money_count=200,
            bank=Bank.objects.get(name="Bank")
        )

    def test_transaction_works(self):

        money_amount_before = Bank.objects.get(name="Bank").money_count

        tran = Transaction.objects.create(
            value=100,
            date=models.DateField(auto_now_add=True),
            member=Member.objects.get(full_name="Member")
        )
        service.update_money_count(
            Bank.objects.get(name="Bank"),
            Member.objects.get(full_name="Member"),
            tran.value
        )

        money_amount_after = Bank.objects.get(name="Bank").money_count

        self.assertEqual(money_amount_before, money_amount_after + tran.value)
