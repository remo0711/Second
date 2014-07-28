'''Max-Min Script
@author karthik
'''

import requests
import json

url = 'http://175.126.103.50:8080/api/v1/datapoints/query'

names = ["proc.stat.cpu","proc.net.bytes"]
''' Append the metric names for getting the same '''

resp = []

for i in range(0,len(names)):
    values = '{"metrics":[{"tags": {},"name": "%s"}],"cache_time": 0,"start_absolute": 1405494000000,"end_absolute": 1405580400000}'%(names[i])
    resp.append(requests.post(url,data=values, headers={"Content-Type": "application/json"}))

del i

'''
for i in range(0,len(resp)):
    print json.loads(resp[j].text)['queries'][0]['results'][0]['values']

del i
'''
maxm = []

for i in range(0,len(resp)):
    for j in range(0,len(json.loads(resp[i].text)['queries'][0]['results'][0]['values'])):
        for k in range(0,len(json.loads(resp[i].text)['queries'][0]['results'][0]['values'])):
            maxm.append(json.loads(resp[i].text)['queries'][0]['results'][0]['values'][i][j])         
        maxm.sort()
        print "max for %s: %l, min for %s: %l"%(names[i],maxm[1],names[i],maxm[len(maxm)])
