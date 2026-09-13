boris = list(map(int, input().split()))
nursik = list(map(int, input().split())) 
x = 0
while nursik and boris:
   b = boris.pop(0)
   n = nursik.pop(0)
   x += 1
   if (b == 0 and n == 9) or (b > n and not(b == 9 and n == 0)):
      boris.append(b)
      boris.append(n)   
   else:
      nursik.append(b)
      nursik.append(n)    
print(("Boris" if boris else "Nursik"), x)  
