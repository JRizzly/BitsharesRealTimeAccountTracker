import requests
import json

#modify Request: https://wrapper.elasticsearch.bitshares.ws/apidocs/#!/wrapper/get_account_history
#Translate Request to Python: https://curl.trillworks.com/#


headers = {
    'Accept': 'application/json',
}

params = (
    ('account_id', '1.2.1612456'),
    ('operation_type', '4'),
    ('size', '100'),
    ('to_date', 'now'),
    ('sort_by', '-block_data.block_time'),
    ('type', 'data'),
    ('agg_field', 'operation_type'),
)

response = requests.get('https://wrapper.elasticsearch.bitshares.ws/get_account_history', headers=headers, params=params)

json_data = json.loads(response.text)

IdTable = { #Will need to have this look up via python-bitshares later , Using Table for quick checks
    '1.3.0' : "BTS",
    '1.3.850' : "OPEN.ETH",
    '1.3.121' : "USD",
}





for i in range(0, len(json_data)):
    #print (json_data[i]['operation_history']['op_object']['is_maker'])

    payAsset = json_data[i]['operation_history']['op_object']['pays']['asset_id']
    payAssetAmount = json_data[i]['operation_history']['op_object']['pays']['amount']/100000

    receiveAsset = json_data[i]['operation_history']['op_object']['receives']['asset_id']
    receiveAssetAmount = json_data[i]['operation_history']['op_object']['receives']['amount']/10000

    print( "Paid Assest: " + str(payAsset) + " At this Amount: " + str(payAssetAmount) )
    print("Received Assest: " + str(receiveAsset) + " At this Amount: " + str(receiveAssetAmount) )
    print( "Price: " + str( payAssetAmount / receiveAssetAmount  ) )


    #print (json_data[i]['operation_history']['op_object']['pays']['asset_id'] + " " + str(json_data[i]['operation_history']['op_object']['pays']['amount'])   )
    print()



print ("hi")

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://wrapper.elasticsearch.bitshares.ws/get_account_history?account_id=1.2.1586454&size=1000&from_date=2015-10-10&to_date=now&sort_by=-block_data.block_time&type=data&agg_field=operation_type', headers=headers)
