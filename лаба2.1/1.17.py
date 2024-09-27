f = open('input.txt')
n = int(f.readline())
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['.', 0, '.']]
x = [[]*i for i in range(10)]
b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(a)):
   for j in range(len(a[i])):
       if a[i][j] != '.':
           if i >= 2:
               if j > 0:
                   if a[i-2][j-1] != '.':
                       x[a[i][j]].append(a[i-2][j-1])
               if j != 2:
                   if a[i - 2][j + 1] != '.':
                       x[a[i][j]].append(a[i - 2][j + 1])
           if i > 0:
               if j == 2:
                   if a[i - 1][j - 2] != '.':
                       x[a[i][j]].append(a[i-1][j-2])
               if j == 0:
                   if a[i - 1][j + 2] != '.':
                       x[a[i][j]].append(a[i - 1][j + 2])
           if i != 3:
               if j == 2:
                   if a[i + 1][j - 2] != '.':
                       x[a[i][j]].append(a[i+1][j-2])
               if j == 0:
                   if a[i + 1][j + 2] != '.':
                       x[a[i][j]].append(a[i + 1][j + 2])
           if i <= 1:
               if j > 0:
                   if a[i + 2][j - 1] != '.':
                       x[a[i][j]].append(a[i+2][j-1])
               if j != 2:
                   if a[i + 2][j + 1] != '.':
                       x[a[i][j]].append(a[i + 2][j + 1])


def hod_konem(s, l, o):
   if s == 1:
       return(1)
   else:
       summ = 0
       for i in range(len(l[o])):
           summ += hod_konem(s-1, l, i)
       return summ


print(x)
summ = 0
for i in b:
   if i != 0 and i != 8:
       summ += hod_konem(n, x, i)
print(summ)
