def isprime(x):
    s = int(x ** 0.5)
    for i in range(2, s + 1):
        if x % i == 0:
            return False
    return True    

n = int(input())
i = 2
while n > 1:
    i += 1
    if isprime(i):
        n -= 1

print(i)
