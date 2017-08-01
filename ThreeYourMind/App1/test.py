import requests

path = 'block100.stl'
myfile = open(path)
showname = 'Johnsshipmodel'
url = 'https://api.3yourmind.com/v1/uploads/'
files = {'file': myfile}
fields = {"origin": "python_test"}


api_key = "9f5f00e6-d25b-482f-96b2-7860e9eaeea7"
header = {"Authorization": "ApiKey " + api_key}

# upload file
response = requests.post(url, files=files, headers=header, data=fields).json()
mydic = response

print(mydic['uuid'])


# url = "https://api.3yourmind.com/v1/uploads/" + mydic['uuid']
# response = requests.get(url, headers=header).json()

# #get volume
# print( response['parameter']['volume'])


#get material prices
# url = "http://api.3yourmind.com/v1/material-prices/"
# fields = {'uuid': mydic['uuid'], 'country': 'DE', 'scale':1.0, 'currency':'EUR'}
# response = requests.get(url, params=fields, headers=header)
#
# print( response.text)