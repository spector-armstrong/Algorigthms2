f = open("input.txt")
rast_B = int(f.readline())
max_km = int(f.readline())
c_stop = int(f.readline())
a = f.readline().split()
stop = [0] + [int(x) for x in a] + [rast_B]


def min_stops(m, A, r):
   num, cr = 0, 0
   while cr <= r:
       lr = cr
       while cr <= r and A[cr+1] - A[lr] < m:
           cr += 1
       if lr == cr:
           return -1
       if cr <= r:
           num += 1
   return num


p = min_stops(max_km, stop, c_stop)
s = open("output.txt", "w")
s.write(str(p))
s.close()
