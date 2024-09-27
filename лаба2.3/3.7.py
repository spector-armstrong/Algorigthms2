from collections import deque
file = open('input7.txt')
vert, ribs = file.readline().split()
graph = {}
for i in range(int(ribs)):
   first, second = file.readline().split()
   f, s = int(first), int(second)
   if f in graph:
       graph[f].append(s)
   else:
       graph[f] = [s]
   if s in graph:
       graph[s].append(f)
   else:
       graph[s] = [f]




def is_bipartite(graph):
   colors = {}
   visited = set()
   queue = deque()


   def bfs(node):
       colors[node] = 1
       visited.add(node)
       queue.append(node)
       while queue:
           current = queue.popleft()
           for neighbor in graph[current]:
               if neighbor not in visited:
                   colors[neighbor] = 1 - colors[current]
                   visited.add(neighbor)
                   queue.append(neighbor)
               elif colors[neighbor] == colors[current]:
                   return False
       return True


   for node in graph:
       if node not in visited:
           if not bfs(node):
               return False
   return True




z = open('output.txt', 'w')
if is_bipartite(graph):
   z.write(str(1))
else:
   z.write((str(0)))
