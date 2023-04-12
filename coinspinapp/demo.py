import requests

url = 'http://localhost:8000/add_post/'
data = {'detail':"dasdasd", 'link': "sfsaasfsf", 'title': "saffsasffs"}
response = requests.post(url, data=data)
print(response.content)
print('URL already exists in database')
