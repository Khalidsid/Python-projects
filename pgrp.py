import requests,json,urllib3
import sys
from requests.auth import HTTPBasicAuth
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


pipeline_group = requests.get("https://infra.omegatooling.com/go/api/config/pipeline_groups", verify=False, auth=HTTPBasicAuth('almbot','Corona@2019'))

#print(pipeline_group.text)

jsn1=pipeline_group.json() 

#print("<head><style>table#t01{table-layout:auto;width:50%;}table#t01{margin: 0 auto;}table#t01 tr:nth-child(even) {  background-color: #eee;}table#t01 tr:nth-child(odd) { background-color: #fff;}table#t01 th { background-color: LightBlue;  color: white;}</style></head>")

print("<table id=\"t01\"><tbody><tr><th class=\"highlight-green\" title=\"Background colour : Green\" data-highlight-colour=\"green\">GoCD-Pipeline Group Name</th><th class=\"highlight-green\" title=\"Background colour : Green\" data-highlight-colour=\"green\">No. of Pipeline</th></tr><head><style>table#t01{table-layout:auto;width:50%;}table#t01{margin: 0 auto;}table#t01 tr:nth-child(even) {background-color: #eee;}table#t01 tr:nth-child(odd){background-color: #fff;}table#t01 th {background-color: LightBlue;  color: white;}</style></head>",end='')
for grp in jsn1: 
        print("<tr>",end='') 
        print("<td>"+grp['name']+"</td>",end='')
        print("<td>"+str(len(grp['pipelines']))+"</td>",end='')
        print("</tr>",end='')
print("</table>",end='')       



