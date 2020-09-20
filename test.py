import requests,json,os
import urllib3
from requests.auth import HTTPBasicAuth
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

x = requests.get("https://infra.omegatooling.com/go/api/config/pipeline_groups", verify=False, auth=HTTPBasicAuth(os.environ['username'],os.environ['pass']))
#print(x.text)
output = json.loads(x.text)

for grp in output: 
    print("\n#############################") 
    print(grp['name']) 
    print(len(grp['pipelines'])) 
    print('#############################') 
      
    for pipln in grp['pipelines']: 
        print(pipln['name'])

#print(out['id','type'])