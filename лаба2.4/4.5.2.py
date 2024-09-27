n = input()
s = input()
res = []
for i in range(len(n) - len(s) + 1):
   if n[i:].startswith(s):
       res.append(i)
print(*sorted(res))