import urllib
import json
url = "https://www.powes.in/blog/how-get-json-da"
def getResponse(url):
    operUrl = urllib.request.urlopen(url)
    if(operUrl.getcode()==200):
       data = operUrl.read()
       print("hello")
    else:
       print("Error receiving data", operUrl.getcode())
    return data