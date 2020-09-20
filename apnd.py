import requests,json,urllib3
import sys
from requests.auth import HTTPBasicAuth
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


x = requests.get("https://infra.omegatooling.com/confluence/rest/api/content/98140479?expand=body.storage", verify=False, auth=HTTPBasicAuth('sfraz','Note@1234'))

output = json.loads(x.text)

old_content = output['body']['storage']['value']

new_content = sys.argv[1]

content = old_content + new_content

version_num = sys.argv[2]

#body = "{\"type\":\"page\",\"version\": { \"number\": "+version_num+"},\"title\":\"ALM Stats Table\",\"body\":{\"storage\":{\"value\":"+content+"}}}"

body = output['body']
body['storage']['value']=content
body['version']=version_num

headers['content-type'] = 'application/json'

y = requests.put("https://infra.omegatooling.com/confluence/rest/api/content/98140479?expand=body.storage", headers=headers, data=body, verify=False, auth=HTTPBasicAuth('sfraz','Note@1234'))

print(y.text)