n=int(input())
n1=1
n2=1
s=0
print(n1,n2,end=" ")
for i in range(2,n):
    s=n1+n2
    print(s,end=" ")
    n1,n2=n2,s
    
