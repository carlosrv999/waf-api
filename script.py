import requests
import json

url = 'https://iam.la-south-2.myhuaweicloud.com/v3/auth/tokens'

# CONFIGURAR PARA CUENTA

domain_name = 'xxxxxxxxxxxxxxxxx'
username = 'xxxxxxxxxxxxxxx'
password = 'xxxxxxxxx'
project_id = 'xxxxxxxxxxxxxxxxxxxxxx'

body = {'auth': {'identity': {'methods': ['password'],'password': {'user': {'name': username,'password': password,'domain': {'name': domain_name}}}},'scope':{'project':{'id': project_id}}}}

jsonData = json.dumps(body)
headers = {'Content-Type': 'application/json'}

x = requests.post(url, data=jsonData, headers=headers)

data = x.json()

token = x.headers['X-Subject-Token']

# print(token)

# EJEMPLO OBTENER LISTA DE IPS PUBLICAS POR APIS

url2 = 'https://vpc.la-south-2.myhuaweicloud.com/v1/'+project_id+'/publicips'
headers2 = {'Content-Type': 'application/json', 'X-Auth-Token': token}

x = requests.get(url2, headers = headers2)

dataget = x.json()

print("test1\n");
print(dataget);