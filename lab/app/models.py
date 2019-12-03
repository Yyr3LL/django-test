from django.db import models
from django.utils import timezone


class Bank(models.Model):
    name = models.TextField(max_length=255)
    money_count = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "bank"
        verbose_name_plural = "banks"


class Member(models.Model):
    full_name = models.TextField(max_length=255)
    money_count = models.IntegerField()
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name="members")

    def __str__(self):
        return self.full_name



    class Meta:
        verbose_name = "family member"
        verbose_name_plural = "family members"


class Transaction(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="transactions")
    value = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = "transaction"
        verbose_name_plural = "transactions"
