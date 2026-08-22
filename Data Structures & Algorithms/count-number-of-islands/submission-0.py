class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        nIslands = 0
        visited = set()

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]

                for x, y in directions:
                    if (x in range(rows) and y in range(cols) and grid[x][y] == "1" and (x, y) not in visited):
                        q.append((x, y))
                        visited.add((x, y))


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    visited.add((i, j))
                    nIslands += 1
                    bfs(i, j)

        return nIslands

        