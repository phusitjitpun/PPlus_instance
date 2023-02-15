import json
import xlsxwriter

jsonString = open('log-instant.txt', 'r', encoding='utf-8-sig').read()
jsonData = json.loads(jsonString)

workbook = xlsxwriter.Workbook('Output.xlsx')
worksheet = workbook.add_worksheet()
row = 0
worksheet.write(row, 0, 'instance-name')
worksheet.write(row, 1, 'instance-type')
worksheet.write(row, 2, 'interface')
worksheet.write(row, 3, 'route-distinguisher')
worksheet.write(row, 4, 'vrf-target')
worksheet.write(row, 5, 'protocals')
row +=1

instanceName = ''
instanceType = ''
interfaceName = ''
vrfTarget = ''
routeDistinguisher = ''
protocolsName = ''
for key in jsonData:
    for dict in jsonData[key]:
        for routes in dict['instance']:
            instanceName = routes['name']
            instanceType = routes['instance-type']
            routeDistinguisher = routes['route-distinguisher']['rd-type']
            worksheet.write(row, 0, instanceName)
            worksheet.write(row, 1, instanceType)
            worksheet.write(row, 3, routeDistinguisher)
            
            if 'vrf-target' in routes:
                vrfTarget == None
                vrfTarget = routes['vrf-target']['community']
                worksheet.write(row, 4, vrfTarget)

            if 'protocols' in routes:
                protocolsName == None
                for i in routes['protocols']:
                    protocolsName = i
                    worksheet.write(row, 5, protocolsName)

            if 'interface' in routes:
                interfaceName == None
                for countName in routes['interface']:
                    interfaceName = countName['name']
                    worksheet.write(row, 2, interfaceName)
                    row +=1
          
workbook.close()