f = open('input.txt')
s = f.readline().split()
apples, rost = int(s[0]), int(s[1])
z_apples = []
for i in range(apples):
   s2 = f.readline().split()
   x = [int(i) for i in s2]
   z_apples.append(x)


def funny_apples(A, h):
   m = A.copy()
   rez = ''
   while A:
       for i in A:
           if h-i[0] > 0:
               h = h + i[1] - i[0]
               A.remove(i)
               r0 = m.index(i) + 1
               rez = rez + str(r0) + ' '
               break
           elif A.index(i) == len(A)-1:
               return '-1'
   return rez


z = open('output.txt', 'w')
z.write(funny_apples(z_apples, rost))
