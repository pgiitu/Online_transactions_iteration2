from transactions.models import Transaction
from transactions.models import Connected_Account
from transactions.models import Connected_Account_Interbank
from transactions.models import Bank
from transactions.models import State
from transactions.models import Branch
from transactions.models import Account
from transactions.models import Bank_Account
from django.contrib import admin

admin.site.register(Transaction)
admin.site.register(Connected_Account)
admin.site.register(Bank)
admin.site.register(State)
admin.site.register(Branch)
admin.site.register(Account)
admin.site.register(Bank_Account)
admin.site.register(Connected_Account_Interbank)
