#shan
import math
n,m=map(int,input().split())
c=n*m
x=math.sqrt(c)
a=int(x)
if x==a:
    print("yes")
else:
    print("no")

