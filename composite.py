#shanu
def isprime(n):
    c=0
    for i in range(2,n):
        if n%i==0:
            c=c+1
    if c==0:
        return False
    else:
        return True

n=int(input())
if isprime(n):
    print("yes")
else:
    print("no")

