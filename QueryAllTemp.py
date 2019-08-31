
# import statements
import requests  

# group ID as 4-5 digit number. ex: 4352
group_id = 
#api token as string - can be found on Samsara Dashboard
api_token = ''
api_url = 'https://api.samsara.com/v1'

# Function to retrieve sensor list
def getApi(endpoint):
    endpoint_url = api_url + str(endpoint)

    # query params for the request
    my_params = {"access_token": api_token}

    # body data to send with the request
    my_data = {"groupId": group_id}

    # send POST request to endpoint
    resp = requests.post(url=endpoint_url, params=my_params, json=my_data)

    # pull out the json
    resp_j = resp.json()
    #return list "sensors" dictionary
    return resp_j['sensors']

# Function to return sensor temperature
def getApi2(endpoint,sensor_id):
    endpoint_url = api_url + str(endpoint)

    # query params for the request
    my_params = {"access_token": api_token}

    # body data to send with the request
    my_data = {"groupId": group_id, "sensors": [sensor_id]}

    # send POST request to endpoint
    resp = requests.post(url=endpoint_url, params=my_params, json=my_data)

    # pull out the json
    resp_j = resp.json()
    #return "sensors" dictionary
    return resp_j['sensors']


#store list of sensors in result variable
result = getApi('/sensors/list')

results = []
results2 = []
#iterate through list and return 'id'
for i in range(len(result)):
    results = result[i]['id']
    results2.append(results)
    # call the API for each sensor. Limitation of API prevents sending list 
    print(getApi2('/sensors/temperature',results))
