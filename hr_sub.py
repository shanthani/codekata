a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=a[0]*60+a[1]
d=b[0]*60+b[1]
s=abs(c-d)
print(s//60,s%60)
