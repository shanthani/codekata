def isprime(n):
    c=0
    for j in range(2,n):
        if n%j==0:
            c=c+1
    if c==0:
        return True
    else:
        return False

n,k=map(int,input().split())
c=0
for i in range(n+1,k):
    if isprime(i):
        if c==0:
            print(i,end="")
            c=c+1
        else:
            print("",i,end="")
    
