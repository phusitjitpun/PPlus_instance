import json
import xlsxwriter

jsonString = open('test.txt', 'r', encoding='utf-8-sig').read()
jsonData = json.loads(jsonString)
routing = ''
name = ''
nexthop = ''
for key in jsonData:
    for dict in jsonData[key]:
        for routes in dict['instance']:
                for i in routes['routing-options']:
                    if 'static' in i: 
                        i = routes['routing-options']['static']
                        routing = i['route'][0]
                        name = routing['name']
                        print(routing, name)