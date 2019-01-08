def rev(n):
    s=0
    while n!=0:
        r=n%10
        n=n//10
        s=s*10+r
    return s

n=int(input())
p=rev(n)
if p==n:
    print("yes")
else:
    print("no")
