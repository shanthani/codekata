def sort1(n):
    if len(n)>1:
        mid = len(n)//2
        left = n[:mid]
        right = n[mid:]
        sort1(left)
        sort1(right)
        i=j=s=0       
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                n[s]=left[i]
                i=i+1
            else:
                n[s]=right[j]
                j=j+1
            s=s+1

        while i < len(left):
            n[s]=left[i]
            i=i+1
            s=s+1

        while j < len(right):
            n[s]=right[j]
            j=j+1
            s=s+1
    return n

n= [1,6,23,45,12,89,4,89,10]
sort1(n)
print(n)
