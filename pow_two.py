#shanu
n=int(input())
for i in range(1,n+1):
    if (2**i)==n:
        print("yes")
        break
else:
    print("no")
