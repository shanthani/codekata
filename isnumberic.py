n=input()
num=['0','1','2','3','4','5','6','7','8','9','.']
for i in n:
    if i in num:
        d="yes"
    else:
        d="No"
        break
print(d)
