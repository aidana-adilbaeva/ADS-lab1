def func(a, n, m):
    a %= m
    res = 1 % m
    while n > 0:
        if n % 2 == 1:
            res = (res * a ) % m
        a = ( a * a ) % m
        n //= 2 
    return res     

a, n, m = map(int, input().split())
print(func(a, n, m))  
