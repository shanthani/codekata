n=int(input())
a=list(map(int,input().split()))
c=0
s=sorted(a)
for i in range(0,len(s)):
    if c==0:
        print(s[i],end="")
        c=c+1
    else:
        print("",s[i],end="")
