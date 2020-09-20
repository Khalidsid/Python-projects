n=int(input("Enter number of rows:"))
for i in range(n+1):
	for j in range(1,i+1):
		print("*",end=" ")
	print()
for i in range(n+1):
    for k in range(i,n-1):
        print("*",end=" ")
    print()    
    
    
'''
Output
*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * *
* * * *
* * *
* *
*
'''    