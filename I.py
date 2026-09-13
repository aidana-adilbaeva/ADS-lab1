from collections import deque

def func(a):
    d = deque()
    while a > 0:
        d.appendleft(a)
        i = a
        a -= 1
        M = len(d)
        k = i % M
        d.rotate(k)
    return d    

x = int(input())
for i in range(x):
    print(*func(int(input())))
