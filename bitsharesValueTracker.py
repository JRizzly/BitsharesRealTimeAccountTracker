
import bitshares
import datetime
import time
from bitshares.account import Account
from bitshares.market import Market

accountName = "jr-12"  #Change this to your account



def repeat():
        pass
        
                





	
def main():

        filename = "data.csv"  #str(datetime.date())
        f = open(filename, 'a')
        #f.write(HEADER)


        account = Account(accountName)
        market = Market("OPEN.ETH:BTS")
        for i in range(0, len(account.balances)):
                print (str(account.balances[i]).replace(' ',','), end =",")
        print (str(market.ticker()["latest"]).replace(' ', ','), end =",")
        print 
        


        


        
                
        
        
        #print(account.balances)
        #print(account.openorders)


	#for h in account.history():
	#	print(h)



	
if __name__ == '__main__':
    main()
