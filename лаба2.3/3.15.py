from collections import deque




def bfs(garden, start, destination, time_limit):
   rows, cols = len(garden), len(garden[0])
   queue = deque([(start, 0)])
   visited = set([start])
   while queue:
       (x, y), time = queue.popleft()
       if (x, y) == destination:
           return time <= time_limit
       for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
           nx, ny = x + dx, y + dy
           if 1 <= nx < rows - 1 and 1 <= ny < cols - 1 and garden[nx][ny] == '0' and (nx, ny) not in visited:
               visited.add((nx, ny))
               queue.append(((nx, ny), time + 1))
   return False




with open('input.txt', 'r') as file:
   n, m = map(int, file.readline().split())
   garden = [file.readline().strip() for _ in range(n)]
   qx, qy, l = map(int, file.readline().split())
   musketeers = [tuple(map(int, file.readline().split())) for _ in range(4)]
total= 0
destination = (qx - 1, qy - 1)
for mx, my, pendants in musketeers:
   if bfs(garden, (mx - 1, my - 1), destination, l):
       total += pendants
with open('output.txt', 'w') as file:
   file.write(str(total))