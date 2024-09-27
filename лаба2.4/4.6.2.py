a = input()
b = input()


if a == b:
   print(0)
   exit()


x = len(a)
for z in range(1, x):
   c = a[x - z:] + a[:x - z]
   if b == c:
       print(z)
       exit()


print(-1)