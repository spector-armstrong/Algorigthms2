f = open("input1.txt")
n = int(f.readline())
rez = []
z = open("output.txt", "w")
for i in range(n):
   s = f.readline().split()
   if s[0] == "+1":
       rez.append(int(s[1]))
       rez.sort()
   elif s[0] == "0":
       z.write(str(rez[len(rez)-int(s[1])]) + "\n")
   elif s[0] == "-1":
       rez.remove(int(s[1]))
