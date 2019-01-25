#shan
n=int(input())
c=0
for i in range(1,n+1):
    if c==0:
        if n%i==0:
            print(i,end='')
            c=c+1
    else:
        if n%i==0:
            print('',i,end='')
    
    
