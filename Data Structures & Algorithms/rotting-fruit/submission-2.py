class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        ROWS, COLS = len(grid), len(grid[0])
        time = 0
        fresh = 0
        q = collections.deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        if fresh == 0: return 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                
                for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    nr = r + dr
                    nc = c + dc
                    if nr in range(len(grid)) and nc in range(len(grid[0])) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        fresh -= 1
            time += 1
            if fresh == 0: break
        
        return time if fresh == 0 else -1
                    


                



