n=int(input())
fact1=1
if n==0:
    print(fact1)
else:
    for i in range(1,n+1):
        fact1=fact1*i
    print(fact1)
