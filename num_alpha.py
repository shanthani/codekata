#shanu
n=input()
c=0
for i in n:
    if i.isnumeric():
        c=c+1
        break
for j in n:
    if j.isalpha():
        c=c+1
        break
if c==2:
    print("yes")
else:
    print("no")
