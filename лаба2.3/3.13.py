from collections import deque


def bfs(grid, visited, row, col):
    rows = len(grid)
    cols = len(grid[0])
    queue = deque([(row, col)])
    visited[row][col] = True
    while queue:
        r, c = queue.popleft()
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '#' and not visited[nr][nc]:
                visited[nr][nc] = True
                queue.append((nr, nc))


def count_gardens(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '#' and not visited[i][j]:
                bfs(grid, visited, i, j)
                count += 1
    return count


with open('input.txt', 'r') as file:
    n, m = map(int, file.readline().split())
    garden = [list(file.readline().strip()) for _ in range(n)]
garden_count = count_gardens(garden)
with open('output.txt', 'w') as file:
    file.write(str(garden_count))