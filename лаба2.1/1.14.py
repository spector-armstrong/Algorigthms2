f = open('input.txt')
s = f.readline()
n = []
operations = []
for i in range(len(s)):
   if i % 2 == 0:
       n.append(int(s[i]))
   else:
       operations.append(s[i])




def Maxx(op, m1, m2):
   if op == '-':
       return m1-m2
   elif op == '+':
       return m1 + m2
   elif op == '*':
       return m1 * m2




def max_itog(op, ch, nt):
   Max = [[0]*(nt) for i in range(nt)]
   Min = [[0]*(nt) for i in range(nt)]
   for i in range(nt):
       Max[i][i] = ch[i]
       Min[i][i] = ch[i]
   for i in range(nt-1):
       for s in range(nt-1):
           b = []
           for k in range(s, i+1+s):
               b.append(Maxx(op[k], Max[s][k], Max[k + 1][s + 1 + i]))
               b.append(Maxx(op[k], Min[s][k], Min[k + 1][s + 1 + i]))
           Min[s][i + 1 + s] = min(b)
           Max[s][i + 1 + s] = max(b)
       nt-=1
   return Max[0][len(Max)-1]