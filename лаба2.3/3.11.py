from collections import defaultdict, deque




def min_reactions(reactions, start, target):
   graph = defaultdict(list)
   for reaction in reactions:
       reactant, product = reaction.split(' -> ')
       graph[reactant].append(product)
   visited = set()
   queue = deque([(start, 0)])
   while queue:
       substance, steps = queue.popleft()
       if substance == target:
           return steps
       visited.add(substance)
       for product in graph[substance]:
           if product not in visited:
               queue.append((product, steps + 1))
   return -1




with open("input11.txt", "r") as file:
   m = int(file.readline().strip())
   reactions = [file.readline().strip() for _ in range(m)]
   start = file.readline().strip()
   target = file.readline().strip()
result = min_reactions(reactions, start, target)
with open("output.txt", "w") as file:
   file.write(str(result))