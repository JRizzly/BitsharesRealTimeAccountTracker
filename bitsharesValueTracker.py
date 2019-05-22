
import bitshares
import datetime
import time
from bitshares.account import Account
from bitshares.market import Market

accountName = "j-rizzly"  #Change this to your account


	
def main():
        '''
        filename = "data.csv"  #str(datetime.date())
        f = open(filename, 'a')
        #f.write(HEADER)
        '''


        account = Account(accountName)

        ''' 
        market = Market("OPEN.ETH:BTS")
        for i in range(0, len(account.balances)):
                print (str(account.balances[i]).replace(' ',','), end =",")
        print (str(market.ticker()["latest"]).replace(' ', ','), end =",")
        '''

        print(account.balances)
        print(account.openorders)
        i = 0
        #1 this method not pulling past 100 operation event with limit set to
        for j in range(0, 10):
            for h in account.history(first=i):
                print(h)
                print (str(i))
                i += 1

        #2 not working for pulling all the trades, for some reason it keeps stopping at like 120 trades???
        # How can I get them all?
        #for h in Market("BTS:OPEN.ETH").accounttrades( account=account, limit=10000000 ):
        #   print(h)



        print ("hi")
        

        
        #print(account.balances)
        #print(account.openorders)


	#for h in account.history():
	#	print(h)



	
if __name__ == '__main__':
    main()
