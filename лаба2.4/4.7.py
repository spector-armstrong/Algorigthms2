def longest_common_subsequence(s1, s2):
   dp = [[0] * (len(s2)+1) for _ in range(len(s1)+1)]
   max_len = 0
   start_index = 0
   st_ind = 0
   for i in range(1, len(s1)+1):
       for j in range(1, len(s2)+1):
           if s1[i-1] == s2[j-1]:
               dp[i][j] = dp[i-1][j-1] + 1
               if dp[i][j] > max_len:
                   max_len = dp[i][j]
                   start_index = i - max_len
                   st_ind = j - max_len
           else:
               dp[i][j] = 0


   return max_len, start_index, st_ind




f = open('input.txt')
s1, s2 = f.readline().split()
length, start_index, s_i = longest_common_subsequence(s1, s2)
z = open('output.txt', 'w')
z.write(str(start_index) + ' ' + str(s_i) + ' ' + str(length))