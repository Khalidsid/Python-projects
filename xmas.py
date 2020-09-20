n=int(input("number"))
for i in range (n):
  for j in range(n-1-i,0,-1):
    print(" ",end="")
  for j in range(i+1):
    print("* ", end="")
   for j in range(n-1-i,0,-1):
    print(" ",end="")
   for j in range(i+1):
    print("* ", end="")
  print()

