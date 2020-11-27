from selenium import webdriver

import requests
import json

import pathes


driver_path = pathes.driverpath
driver = webdriver.Firefox(executable_path=driver_path)
driver.get

def authorization():
   headers = {'Content-Type': 'application/x-www-form-urlencoded'}
   data = {'username': pathes.login,
           'password': pathes.password,
           'grant_type': 'password',
           'scope': 'pegasus',
           'client_id': 'pegasus-v2',
           'client_secret': 'secret'}
   url = "http://srv-pnew-01-test:1001/auth/connect/token"
   r = requests.post(url, data = data, headers = headers)
   answer = json.loads(r.text)
   return answer["access_token"]

urls = [
'http://configurations-backend-edu.pegasus.ponyex.local/',
'http://couriers-backend-edu.pegasus.ponyex.local/',
'http://delivery-edu.pegasus.ponyex.local/',
'http://delivery-backend-edu.pegasus.ponyex.local/',
'http://enumerations-backend-edu.pegasus.ponyex.local/',
'http://events-edu.pegasus.ponyex.local/',
'http://events-backend-edu.pegasus.ponyex.local/',
'http://geography-edu.pegasus.ponyex.local/',
'http://geography-backend-edu.pegasus.ponyex.local/',
'http://localizations-backend-edu.pegasus.ponyex.local/',
'http://organization-backend-edu.pegasus.ponyex.local/',
'http://warehouses-edu.pegasus.ponyex.local/',
'http://warehouses-backend-edu.pegasus.ponyex.local/',
'http://waybills-backend-edu.pegasus.ponyex.local/']

try:
   tok = authorization()
except:
   print('Error: Authorization failed')
   driver.close()

url='http://srv-pnew-01-test.ponyex.local:1001/api/v1/user-profile-groups/post-item'
data = {'displayName': "Group0"}

try:
   r = requests.post(url, data = json.dumps(data), headers = {'Content-Type': 'application/json','Authorization': 'Bearer ' + tok})
except:
   print('Error: Post fail')
   driver.close()

if  r.status_code != 200:
    print('Error ',r.status_code)
    driver.close()

answer=json.loads(r.text)

id=answer['result']['id']


url='http://srv-pnew-01-test.ponyex.local:1001/api/v1/user-profile-groups/delete-item'
params = {'id': id}

try:
   r = requests.delete(url, params = params, headers = {'Authorization': 'Bearer ' + tok})
except:
   print('Error: Deleting failed')
   driver.close()

if  r.status_code != 200:
    print('Error ',r.status_code)
    driver.close()

print ('OK')
driver.close()

