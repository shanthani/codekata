#shanu
n,k=map(int,input().split())
a=list(map(int,input().split()))
if k in a:
    print(a.count(k))
else:
    print("0")
