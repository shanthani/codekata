#shanu
n=input()
c=0
a=['a','e','i','o','u']
for i in n:
    if i in a:
        c=c+1
        break
if c==1:
    print("yes")
else:
    print("no")
