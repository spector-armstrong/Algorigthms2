def shortest_dist(graph, n, m, s):
   path = [float('inf')] * (n + 1)
   path[s] = 0
   for _ in range(n - 1):
       for u, v, w in graph:
           if path[u] != float('inf') and path[u] + w < path[v]:
               path[v] = path[u] + w


   for u, v, w in graph:
       if path[u] != float('inf') and path[u] + w < path[v]:
           path[v] = float('-inf')
   return path




with open('input10.txt', 'r') as file:
   n, m = map(int, file.readline().split())
   graph = [list(map(int, file.readline().split())) for _ in range(m)]
   s = int(file.readline())


distances = shortest_dist(graph, n, m, s)
with open('output.txt', 'w') as file:
   for i in range(1, n + 1):
       if distances[i] == float('-inf'):
           file.write("-\n")
       elif distances[i] == float('inf'):
           file.write("*\n")
       else:
           file.write(str(distances[i]) + "\n")