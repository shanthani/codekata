n=int(input())
b=n
sum=0
while n!=0:
    r=n%10
    n=n//10
    sum=sum*r*r*r
if b==sum:
    print("yes")
else:
    print("no")
