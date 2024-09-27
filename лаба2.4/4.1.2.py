def z_f(s):
   zf = [0] * len(s)
   left, right = 0, 0
   for i in range(1, len(s)):
       zf[i] = max(0, min(right - i, zf[i - left]))
       while i + zf[i] < len(s) and s[zf[i]] == s[i + zf[i]]:
           zf[i] = zf[i] + 1
       if i + zf[i] > right:
           left = i
           right = i + zf[i]
   return zf




def main():
   f = input()
   s = input()
   f += '#' + s
   z = z_f(f)
   r = 0
   l = f.find('#') + 1
   v = []
   for i in range(f.find('#') + 1, len(f)):
       if z[i] == 0:
           if i > r:
               print("Yes")
               return
       else:
           if z[i] + i - 1 > r:
               r = z[i] + i - 1
               if i != l:
                   v.append(f[l:i])
               l = i
   v.append(f[l:])
   print("No")
   first = s[0]
   if len(v[len(v)-1])>1 and (v[len(v)-1][len(v[len(v)-1])-1]) == first:
       v[len(v)-1] = v[len(v)-1][:len(v[len(v)-1])-1]
       v.append(first)
   for sub_str in v:
       print(sub_str, end=' ')