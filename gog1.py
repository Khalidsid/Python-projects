T = input()
for x in range(0, 2):
    M,N = input().split()
    print(type(M))
    M,N = [int(M), int(N)]
    sum=int(M)+int(N)
    #print(type(sum))
    if len(str(sum)) == len(str(N)):
        print(N)
    else:
        print(sum)
        
#hum space lein, or 2 input lein         