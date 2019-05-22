
import bitshares
import datetime
import time
from bitshares.account import Account
from bitshares.market import Market

accountName = "jr-12"  #Change this to your account

filename = "dataPull.csv"  #str(datetime.date())
f = open(filename, 'a')
		
account = Account(accountName)
f.write(str(account.balances))

f.write(str(account.openorders))
for h in account.history():
    f.write(str(h))
f.close()

