f = open("input1.txt")
n = int(f.readline())
tree = []
for i in range(n):
   a = f.readline().split()
   x = [int(i) for i in a]
   tree.append(x)


def if_correct(tr, size):
   for j in range(size):
       if tr[j][1] != -1 and tr[tr[j][1]][0] >= tr[j][0]:
           return False
       if tr[j][2] != -1 and tr[tr[j][2]][0] < tr[j][0]:
           return False
   return True


z = open("output.txt", "w")
fact = if_correct(tree, n)
if fact:
   z.write("CORRECT")
else:
    z.write("INCORRECT")