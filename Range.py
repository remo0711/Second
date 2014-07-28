'''Max-Min Script
@author karthik
'''

import requests
import json

url = 'http://175.126.103.50:8080/api/v1/datapoints/query'

names = ["proc.stat.cpu","proc.net.bytes"]
''' Append the metric names for getting the same '''

resp1 = []

for i in range(0,len(names)):
    values1 = '{"metrics": [{"tags": {},"name": "%s","aggregators": [{"name": "max","align_sampling": true,"sampling": {"value": "1","unit": "days"}}]}],"cache_time": 0,"start_absolute": 1405494000000,"end_absolute": 1405753200000}'%(names[i])
    resp1.append(requests.post(url,data=values1, headers={"Content-Type": "application/json"}))

del i

resp2 = []

for i in range(0,len(names)):
    values2 = '{"metrics": [{"tags": {},"name": "%s","aggregators": [{"name": "min","align_sampling": true,"sampling": {"value": "1","unit": "days"}}]}],"cache_time": 0,"start_absolute": 1405494000000,"end_absolute": 1405753200000}'%(names[i])
    resp2.append(requests.post(url,data=values2, headers={"Content-Type": "appllication/json"}))

del i

list = []

for i in range(0,len(resp1)):
    for j in range(0,len(json.loads(resp1[i].text)['queries'][0]['results'][0]['values'])):
        list.append(json.loads(resp1[i].text)['queries'][0]['results'][0]['values'][i][1])
    print "max for %s is %i"%(names[i],(sum(list)/len(list)))
    for k in range(0,len(json.loads(resp1[i].text)['queries'][0]['results'][0]['values'])):
        list.pop()

del i,j,k

for i in range(0,len(resp2)):
    for j in range(0,len(json.loads(resp2[i].text)['queries'][0]['results'][0]['values'])):
        list.append(json.loads(resp2[i].text)['queries'][0]['results'][0]['values'][i][1])
    print "min for %s is %i"%(names[i],(sum(list)/len(list)))
    for k in range(0,len(json.loads(resp2[i].text)['queries'][0]['results'][0]['values'])):
        list.pop()
