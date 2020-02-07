from django.shortcuts import redirect


def create_transaction(self, form):
    value = int(form.cleaned_data['value'])
    form.instance.bank = form.cleaned_data['member'].bank
    form.instance.save()
    update_money_count(self, form.instance.bank, form.instance.member, value)


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
