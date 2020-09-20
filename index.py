s=input("Enter string ")
i=0
for x in s:
	print("The character present at positive index:{} and at negative index: {} is :{}".format(i,i-len(s),x))
	i=i+1