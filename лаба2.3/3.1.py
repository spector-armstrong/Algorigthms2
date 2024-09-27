f = open("input_1.txt")
a = f.readline().split()
vertexes, ribs = int(a[0]), int(a[1])
gr = [[] for _ in range(vertexes)]
for i in range(ribs):
   s = f.readline().split()
   curr_v1, curr_v2 = int(s[0]), int(s[1])
   gr[curr_v1-1].append(curr_v2)
   gr[curr_v2-1].append(curr_v1)
f1, f2 = [int(x) for x in f.readline().split()]




def are_ribs_together(versh1, versh2, graph, pr):
   if int(versh2) in graph[versh1-1]:
       return 1
   else:
       for j in range(len(graph[versh1 - 1])):
           pr.append(versh1)
           if graph[versh1-1][j] not in pr:
               return are_ribs_together(graph[versh1 - 1][j], versh2, graph, pr)
       return 0




pr = []
with open('output.txt', 'w') as z:
   z.write(str(are_ribs_together(f1, f2, gr, pr)))

