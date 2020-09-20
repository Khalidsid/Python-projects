s=input("Enter Main String:")
subs=input("Enter Substring:")
flag=False
pos=-1
count=0
n=len(s)
while True:
    pos=s.find(subs,pos+1,n)
    if pos==-1:
        break
    print("Found at index: ",pos)
    flag=True
    count=count+1
if flag==False:
    print("Not Found ")
print("Total Occurance", count)