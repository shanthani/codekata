def arm(n):
    b=n
    sum1=0 
    while n!=0:
        r=n%10
        n=n//10
        sum1=sum1+r*r*r
    if b==sum1:
        return True
    else:
        return False
n,k=map(int,input().split())
c=0
for i in range(n+1,k):
    if arm(i):
        if c==0:
            print(i,end="")
            c=c+1
        else:
            print("",i,end="")
