s=input("Enter string ")
count = 0
for x in range(0,len(s)):
    for z in range(0, len(s)):
        if s[x] == s[z]:
            count = count +1
    print(s[x],end='=')
    print(count)
    count = 0
    