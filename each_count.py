'''s =input("Enter a string : ")
v=input("Enter a char to search : ")
#d = chr(v)

#s="faraz"
print ("total times of occurance of " ,s.count(v))
count = 0
#for x in s:
 #  count = count +1
  #  print("No. of occurance of s ",count)
  
'''  
def multi_repeat():
    s =input("Enter a string : ")
    all_freq = ()
    for i in s:
        if i in all_freq:
            print(i)
            all_freq[i] +=1
            print("if part",all_freq)
        else:
            all_freq[i] = 1
            print("else part",i)
    print("Count of occurrence :\n" + str(all_freq)) 

multi_repeat()