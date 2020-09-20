cart=[10,30,600,50,90]	
for item in cart:
	if item>500:
		print("item above 500 cannot be processed, kindly remove that")
		break
	print("Processing item:", item)