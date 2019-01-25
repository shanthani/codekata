#shanu
n=input()
c=0
for i in n:
    i=int(i)
    if c==0:
        if i%2==1:
            print(i,end='')
            c=c+1
    else:
        if i%2==1:
            print("",i,end='')
    
