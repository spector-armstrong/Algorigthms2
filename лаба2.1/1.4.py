f = open('input.txt')
c_otrezki = int(f.readline())
otrezki = []
for i in range(c_otrezki):
   k = f.readline()
   s = [int(x) for x in k.split()]
   otrezki.append(s)


def min_tochki(A, l):
   A.sort()
   c = 0
   for j in range(l-1):
       if A[j][1] >= A[j+1][0]:
           A[j+1] = [max(A[j][0], A[j+1][0]), min(A[j][1], A[j+1][1])]
           A[j] = '*'
   return A


rez = min_tochki(otrezki, c_otrezki)
g = open('output.txt', 'w')
g.write(str(len(rez) - rez.count('*')) + '\n')
for i in rez:
   if i != '*':
       g.write(str(i[0]) + ' ')
