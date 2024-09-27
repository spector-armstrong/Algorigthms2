f = open("input.txt")
n = int(f.readline())
s = f.readline().split()
u = [int(i) for i in s]


def check_split_array(x):
   if sum(x) % 3 == 0:
       fl = 1
       tmp = sum(x) / 3
       x.sort()
       x.reverse()
       for _ in range(3):
           y = []
           j = 0
           while sum(y) != tmp and j < len(x):
               if (sum(y) + x[j]) <= tmp:
                   y.append(x[j])
                   del (x[j])
               else:
                   j += 1
           if sum(y) != tmp:
               fl = 0
               return fl
       return fl
   else:
       fl = 0
       return fl


z = open("output.txt", "w")
z.write(str(check_split_array(u)))
