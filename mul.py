n=int(input())
c=0
for i in range(1,n+1):
    if c==0:
        print(n*i,end="")
        c=c+1
    else:
        print("",n*i,end="")
