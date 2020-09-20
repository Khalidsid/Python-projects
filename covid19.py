# importing libraries 

import requests 
from bs4 import BeautifulSoup 
from tabulate import tabulate 
import os 
import numpy as np 
import matplotlib.pyplot as plt 


extract_contents = lambda row: [x.text.replace('\n', '') for x in row] 

URL = 'https://www.mohfw.gov.in/'

SHORT_HEADERS = ['SNo', 'State','Indian-Confirmed', 'Foreign-Confirmed','Cured','Death','fets'] 

response = requests.get(URL).content 

soup = BeautifulSoup(response, 'html.parser') 
header = extract_contents(soup.tr.find_all('th')) 

stats = [] 
all_rows = soup.find_all('tr') 

for row in all_rows: 
	stat = extract_contents(row.find_all('td'))
#print("Printing Stats : ",stat)
	if stat: 
		if len(stat) == 5: 
			# last row    
			stat = ['', *stat] 
            print(stat)
			#stats.append(stat) 
		elif len(stat) == 6: 
			stats.append(stat) 

stats[-1][1] = "Total Cases"
#print("Total case : ", stats)
stats.remove(stats[-1]) 
'''
objects = [] 
for row in stats : 
	objects.append(row[-1]) 

y_pos = np.arange(len(objects)) 
#print(y_pos)
#print(row[1])
#print(SHORT_HEADERS)
performance = [] 
for row in stats : 
  performance.append((row[1]) + (row[2]))

print(performance)
 

table = tabulate(stats, headers=SHORT_HEADERS) 
print(table) 
...