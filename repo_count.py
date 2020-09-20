from __future__ import print_function
import requests,json,urllib3
import sys
from requests.auth import HTTPBasicAuth
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

repo_count = requests.get("https://infra.omegatooling.com/bitbucket/rest/api/1.0/repos?limit=1000", verify=False, auth=HTTPBasicAuth('sadamshafi','Adam@shafi@1234'))


jsn1=repo_count.json() 
dct={}
print(jsn1)
'''
for repo in jsn1['values']:
    if repo['project']['name'] not in dct.keys():
        dct[repo['project']['name']] = []
    dct[repo['project']['name']].append(repo['slug'])
    
#print("<head><style>{table-layout:auto;width:100%;}table#t01{margin: 0 auto;} table#t01 tr:nth-child(even) {  background-color: #eee;}table#t01 tr:nth-child(odd) { background-color: #fff;}table#t01 th { background-color: SteelBlue;  color: white;}</style></head>")
    
print("<table id=\"t01\"<tbody><tr><th class=\"highlight-green\" title=\"Background colour : Green\" data-highlight-colour=\"green\">Bitbucket Project Name</th><th class=\"highlight-green\" title=\"Background colour : Green\" data-highlight-colour=\"green\">No. of ReposCount</th></tr><head><style>{table-layout:auto;width:100%;}table#t01{margin: 0 auto;} table#t01 tr:nth-child(even) {  background-color: #eee;}table#t01 tr:nth-child(odd) { background-color: #fff;}table#t01 th { background-color: SteelBlue;  color: white;}</style></head>",end='')    
    
for projt in dct.keys():
  print("<tr>",end='') 
  print("<td>"+projt+"</td>",end='')
  print("<td>"+str(len(dct[projt]))+"</td>",end='')
  print("</tr>",end='')
print("</table>",end='')
'''