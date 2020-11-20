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

correct_id = '359afb0c-b870-4610-9233-524db1d5a029'

search = 'Максим'
page_size = '5'
page_index ='1'
sort_direction ='1'

try:
   r = requests.get(urls[1] + '/api/v1/couriers/get-couriers' + '?Search=%D0%9C%D0%B0%D0%BA%D1%81%D0%B8%D0%BC',
                    headers = {'Authorization': 'Bearer ' + tok}, params = {'PageIndex': page_index,
                   'PageSize': page_size, 'SortDirection' : sort_direction, 'Search': search})
except:
   print('Error: Searching failed')
   driver.close()

if  r.status_code != 200:
    print('Error ',r.status_code)
    driver.close()

try:
   ans = json.loads(r.text)
except:
   print('Error: Can not find name of the courier')
   driver.close()

result = ans['result']['items']

if  len(result) != 5:
    print('Number of people is not 5')
    driver.close()

a1 = result[0]
a2 = result[1]
a3 = result[2]
a4 = result[3]
a5 = result[4]

if  a1['firstName'] != 'Максим' or a2['firstName'] != 'Максим' or a3['firstName'] != 'Максим' or a4['firstName'] != 'Максим' or a5['firstName'] != 'Максим':
    print('Not all the people are Maksimes')
    driver.close()


print ('OK')
driver.close()
