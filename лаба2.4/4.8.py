s = input()
s1 = sorted(s)
if s1 == list(set(s1)):
   print(0)
else:
   otvet = 0
   for i in range(len(s)):
       for j in range(len(s) - 1, -1, -1):
           if s[i] == s[j]:
               jj = j
               break
       sum = jj - i
       if sum > otvet:
           otvet = sum
   print(otvet)