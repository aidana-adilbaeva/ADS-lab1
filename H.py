n = int(input())
a = list(map(int, input().split()))
b = []
c = []

for i in range(n):
    while c and c[-1] >= a[i]:
        c.pop()
    if c:
        b.append(c[-1])
    else:
        b.append(-1)        
    c.append(a[i])    

print(*b)            
