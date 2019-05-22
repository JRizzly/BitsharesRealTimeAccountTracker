import requests
import json

#modify Request: https://wrapper.elasticsearch.bitshares.ws/apidocs/#!/wrapper/get_account_history
#Translate Request to Python: https://curl.trillworks.com/#


headers = {
    'Accept': 'application/json',
}

params = (
    ('account_id', '1.2.1610610'),
    ('operation_type', '4'),
    ('size', '1000'),
    ('to_date', 'now'),
    ('sort_by', '-block_data.block_time'),
    ('type', 'data'),
    ('agg_field', 'operation_type'),
)

response = requests.get('https://wrapper.elasticsearch.bitshares.ws/get_account_history', headers=headers, params=params)

json_data = json.loads(response.text)

for i in range(0, len(json_data)):
    print (json_data[i]['operation_history']['op_object']['is_maker'])


print ("hi")

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://wrapper.elasticsearch.bitshares.ws/get_account_history?account_id=1.2.1586454&size=1000&from_date=2015-10-10&to_date=now&sort_by=-block_data.block_time&type=data&agg_field=operation_type', headers=headers)
