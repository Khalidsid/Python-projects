import requests,json,urllib3
import sys
from requests.auth import HTTPBasicAuth
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



pipeline_group = requests.get("https://infra.omegatooling.com/go/api/config/pipeline_groups", verify=False, auth=HTTPBasicAuth('sfraz','Note@1234'))

#print(pipeline_group.text)

jsn1=pipeline_group.json() 
y=""

y=y+"<table>"
for grp in jsn1: 
        y=y+"<tr>"
        y=y+"<td>"+grp['name']+"</td>"
        y=y+"<td>"+str(len(grp['pipelines']))+"</td>"
        y=y+("</tr>")
y=y+"</table>"

'''
body = {}
#body["type"]="page"
#body["version"]= {"number": '7'}
#body["title"]="ALM Stats Table"
#body["representation"]="storage"
#body[]={}
body['storage']={}
body['storage']['value']='y'
#body['body']['version']= 7
'''
headers={'content-type': 'application/json'}

y = requests.put("https://infra.omegatooling.com/confluence/rest/api/content/102998056?expand=body.storage", headers=headers, data=body, verify=False, auth=HTTPBasicAuth('sfraz','Note@1234'))

print(y.text)
