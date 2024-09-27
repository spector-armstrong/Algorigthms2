f = open('input.txt')
days = int(f.readline())
lunches = []
for i in range(days):
   a = int(f.readline())
   lunches.append(a)




def min_cost(l, d):
   dp = [[500]*(d+1) for _ in range(d+1)]
   dp[0][0] = 0
   for i in range(1, d+1):
       for j in range(i):
           dp[i][j] = min(dp[i][j], dp[i-1][j] + l[i-1])
           if l[i-1] > 100:
               dp[i][j+1] = min(dp[i][j+1], dp[i-1][j] + l[i-1])
           if j >= 1:
               dp[i][j-1] = min(dp[i][j-1], dp[i-1][j])
   m = min(dp[d])
   mm = m
   not_used = dp[d].index(m)
   kyponi = []
   for i in range(d-1, 0, -1):
       for j in range(d):
           if m == (dp[i][j] + l[i]):
               m = dp[i][j]
               break
           elif m == dp[i][j]:
               kyponi.append(i+1)
               break
   print(dp)
   print(l)
   return(mm, kyponi, not_used)




p = min_cost(lunches, days)
z = open('output.txt', 'w')
z.write(str(p[0]) + '\n')
z.write(str(p[2]) + ' ' + str(len(p[1])) + '\n')
p[1].reverse()
for i in p[1]:
   z.write(str(i) + '\n')