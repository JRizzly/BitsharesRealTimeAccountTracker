import requests
import json
import bitshares
import datetime
import time
from bitshares.account import Account
from bitshares.market import Market
from bitshares.asset import Asset




#todo Add variables for JSON request here

############################################# JSON #################################################

# modify Request: https://wrapper.elasticsearch.bitshares.ws/apidocs/#!/wrapper/get_account_history
# Translate Request to Python: https://curl.trillworks.com/#

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://wrapper.elasticsearch.bitshares.ws/get_account_history?account_id=1.2.1586454&size=1000&from_date=2015-10-10&to_date=now&sort_by=-block_data.block_time&type=data&agg_field=operation_type', headers=headers)

#GET all FILLS

headers = {
    'Accept': 'application/json',
}

params = (
    ('account_id', '1.2.1612456'),
    ('operation_type', '4'),
    ('size', '3000'),
    ('to_date', 'now'),
    ('sort_by', '-block_data.block_time'),
    ('type', 'data'),
    ('agg_field', 'operation_type'),
)

response = requests.get('https://wrapper.elasticsearch.bitshares.ws/get_account_history', headers=headers, params=params)
############################################# JSON #################################################


QuoteAsset = '1.3.121'  #USD to change as an input
BaseAsset = '1.3.0'   #BTS to change as an input

BaseAmountStart = 17279.83
QuoteAmountStart = 0.0


class FillEvent:


    def __init__(self, datee, receiveAssett, receiveAssetAmountt, payAssett, payAssetAmountt ):

        global BaseAmountStart
        global QuoteAmountStart
        global QuoteAsset
        global BaseAsset


        self.currentBalanceBase = BaseAmountStart
        self.currentBalanceQuote = QuoteAmountStart

        self.currentBaseValueCalc = 0.0
        self.currentQuoteValueCalc = 0.0

        self.currentSequence = 0


        self.date = datee

        self.currentSequence += 1

        self.receiveAsset = receiveAssett
        self.receiveAssetAmount = receiveAssetAmountt
        self.payAsset = payAssett
        self.payAssetAmount = payAssetAmountt

        if  self.receiveAsset == BaseAsset and self.payAsset == QuoteAsset: #check to see if base or quote asset is on recieving end of fill

            self.baseAssetPrice = self.receiveAssetAmount / self.payAssetAmount
            self.quoteAssetPrice = self.payAssetAmount / self.receiveAssetAmount

            #self.BaseAssetPricePercent = (self.baseAssetPrice / self.startBasePrice) * 100.0
            #self.QuoteAssetPricePercent = (self.quoteAssetPrice / self.startQuotePrice) * 100.0

            self.currentBalanceBase += self.receiveAssetAmount
            BaseAmountStart = self.currentBalanceBase
            self.currentBalanceQuote -= self.payAssetAmount
            QuoteAmountStart = self.currentBalanceQuote





        if self.payAsset == BaseAsset :


            self.quoteAssetPrice = self.receiveAssetAmount / self.payAssetAmount
            self.baseAssetPrice = self.payAssetAmount / self.receiveAssetAmount

            #self.QuoteAssetPricePercent = (self.quoteAssetPrice / self.startBasePrice) * 100.0
            #self.BaseAssetPricePercent = (self.baseAssetPrice / self.startQuotePrice) * 100.0

            self.currentBalanceQuote += self.receiveAssetAmount
            QuoteAmountStart = self.currentBalanceQuote
            self.currentBalanceBase -= self.payAssetAmount
            BaseAmountStart = self.currentBalanceBase





        #self.receiverAssetBalanceOverTime = self.getReceiverAssetBalanceOverTime()
        self.payAssetOverTime = None #todo

        self.currentPayAssetAccountValueAppx = None #todo
        self.currentReceiverAssetAccountValueAppx = None  # todo
        self.currentPayAssetAccountValuePercent = None #todo
        self.currentReceiverAssetValuePercent = None #todo

        self.currentPayAssetProportion = None #todo
        self.currentReceiverAssetProportion = None #todo




    ''' 
    def getReceiverAssetBalanceOverTime(self):
        if (self.receiveAsset == baseAsset):
            return self.currentBalanceBase + self.receiveAssetAmount
        if (self.receiveAsset == QuoteAsset):
            return self.currentBalanceQuote + self.receiveAssetAmount
        else :
            print ("Error: in Get ReceiverAssetBalanceOverTime")
            return 0.0
            
    '''


    def csvBasicPrintOut(self):
        print ( self.date + "," + str(self.receiveAssetAmount) + "," + Asset(str(self.receiveAsset))['symbol'] , end=",")
        print (  str(self.payAssetAmount) + "," + Asset(str(self.payAsset))['symbol'] )

    def csvFullPrintOut(self):
        print ( self.date + "," + str(self.receiveAssetAmount) + "," + Asset(str(self.receiveAsset))['symbol'] , end=",")
        print (  str(self.payAssetAmount) + "," + Asset(str(self.payAsset))['symbol'] , end="," )
        print ( str( self.receiverAssetPrice )  + "," + str( self.payerAssetPrice), end=","  )
        print ( str( self.receiverAssetBalanceOverTime ) + ","  )

    def csvFullPrintOut2(self):
        print (  str(self.currentBalanceBase) + "," + Asset(str(BaseAsset))['symbol'] , end=",")
        print (  str(self.currentBalanceQuote) + "," + Asset(str(QuoteAsset))['symbol'] , end="," )
        print ( str( self.baseAssetPrice )  + "," + str( self.quoteAssetPrice), end=","  )
        print ()
        #print ( str( self.base ) + ","  )


json_data_fills = json.loads(response.text)
#Reversing to match chronological
json_data_fills.reverse()


fillEventLog = []
setBaseAndQuoteStartPrice = False



for i in range(0, len(json_data_fills)):
    #print (json_data_fills[i]['operation_history']['op_object']['is_maker']) #Todo feature add ability to see how many trades are maker

    fillDate = json_data_fills[i]['block_data']['block_time']

    payAsset =   json_data_fills[i]['operation_history']['op_object']['pays']['asset_id']
    payAssetAmount = json_data_fills[i]['operation_history']['op_object']['pays']['amount'] / \
                     10**Asset(  json_data_fills[i]['operation_history']['op_object']['pays']['asset_id'] )['precision']  #Thanks paasila


    receiveAsset =  json_data_fills[i]['operation_history']['op_object']['receives']['asset_id']
    receiveAssetAmount = json_data_fills[i]['operation_history']['op_object']['receives']['amount'] / \
                         10**Asset(  json_data_fills[i]['operation_history']['op_object']['receives']['asset_id'] )['precision']  #Thanks paasila

    if ( ) # Need to handle case where non-pair fills happen
    fillData = FillEvent(fillDate, receiveAsset , receiveAssetAmount , payAsset , payAssetAmount  )
    fillEventLog.append(fillData)

    #fillData.csvFullPrintOut2()




    # Prints output in CSV form, I used to validate
    #print(fillDate + "," + str(receiveAssetAmount) + "," + str(receiveAsset) , end=",")
    #print( str(payAssetAmount) + "," + str(payAsset) )

    ''' # Good to print out for it to make sense but not needed
    print( "Paid Assest: " + str(payAsset) + " At this Amount: " + str(payAssetAmount) )
    print("Received Assest: " + str(receiveAsset) + " At this Amount: " + str(receiveAssetAmount) )
    print( "Receive Asset Price: " + str( receiveAsset ) + " " +  str( receiveAssetAmount / payAssetAmount  )  )
    print("Paid Asset Price: " + str(payAsset) + " " + str(payAssetAmount / receiveAssetAmount))
    '''

    # Good to print out for it to make sense but not needed
    #print( "Receive Asset Price: " + str( receiveAsset ) + " " +  str( receiveAssetAmount / payAssetAmount  )  )
    #print("Paid Asset Price: " + str(payAsset) + " " + str(payAssetAmount / receiveAssetAmount))


for i in range(0, len(fillEventLog)):
    fillEventLog[i].csvFullPrintOut2()

    




print ("hi")



