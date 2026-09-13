n = int(input())
s = int(n ** 0.5)

for i in range(2, s+1):
    while(n % i == 0):
        print(i, end=" ")
        n //= i

if(n > 1):
    print(n)
