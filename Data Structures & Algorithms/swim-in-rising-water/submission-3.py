class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # 把Dijkstra's从shortest path改成track min/max，但本质相同
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        minHeap = [[grid[0][0],0,0]]
        directions = [[0,1], [1,0], [0,-1], [-1,0]]

        visit.add((0,0))
        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            # visit.add((r,c))
            if r == ROWS -1 and c == COLS -1:
                return t
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr < 0 or nc < 0) or (nr == ROWS or nc == COLS) or (nr, nc) in visit:
                    continue
                visit.add((nr,nc))
                heapq.heappush(minHeap, (max(t, grid[nr][nc]), nr, nc))

        