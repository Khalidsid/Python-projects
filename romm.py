from datetime import datetime
print("Month =  ",datetime.now().month)
rent = 15300
internet = 1250
maid = 2500
print(" Room Rent= 15300")
print(" Internet Bill = 1250 ")
print(" Maid Bill = 2500" )
water=int(input("Enter Water Bill = "))
total=(rent + water + internet + maid)
print(total)

mem=int(input("Enter number of members to be divided = "))

if mem == 5:
  print("Each share is = ", total/mem)
elif mem == 4:
  print("Each share is = ", total/mem)
else:
  each = total/mem
  print("Each Share is = ", each)  

#Food List
s=int(input("Enter saquib share = "))
j=int(input("Enter jaffar share = "))
f=int(input("Enter faiyaz share = "))
i=int(input("Enter imran share = "))

#Final price
def finalPrice():
 saq = each - s
 jaf = each - j
 faz = each - f
 imr = each - i
 print(saq)
 print(jaf)
 print(faz)
 print(imr)


finalPrice()

