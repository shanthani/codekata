n,k=map(int,input().split())
c=0
for i in range(n+1,k):
    if i%2==1:
        if c==0:
            print(i,end="")
            c=c+1
        else:
            print("",i,end="")
    
