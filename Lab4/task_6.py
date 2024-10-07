f1 = open('Lab4\Input6.txt', 'r')
f2 = open("Lab4\Output6.txt", "w")
rows, cols = map(int, f1.readline().split())
grid = [list(f1.readline().strip()) for _ in range(rows)]

def dfs(grid, row, col, visited, diamonds):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == '#' or visited[row][col]:
        return 0
    visited[row][col] = True
    if grid[row][col] == 'D':
        diamonds += 1
    count = diamonds
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        count = max(count, dfs(grid, row + dr, col + dc, visited, diamonds))
    visited[row][col] = False
    return count

def max_diamonds(grid):
    max_diamonds = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '.':
                visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
                diamonds = dfs(grid, row, col, visited, 0)
                max_diamonds = max(max_diamonds, diamonds)
    return max_diamonds

print(max_diamonds(grid), file=f2)
