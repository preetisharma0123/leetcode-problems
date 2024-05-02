"""
#286. Walls and Gates

You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

"""

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        from collections import deque

        EMPTY = 2147483647
        GATE = 0
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        q = deque()
        m = len(rooms)
        n = len(rooms[0])
        if not rooms:
            return
        for row in range(m):
            for col in range(n):
                if rooms[row][col] == GATE:
                    q.append((row,col))

        while q:
            row, col = q.popleft()
            print("row, col",row, col)
            for rd,cd in DIRECTIONS:
                print("rd, rd",rd,cd)
                r, c = row+rd, col+cd
                print("r,c",r,c)
                if 0<=r<m and 0<=c<n:
                    print("val", rooms[r][c])
                    if rooms[r][c]== EMPTY:
                        rooms[r][c] = rooms[row][col] + 1
                        q.append((r,c))
        
    
#Time complexity : O(mn)

#Space complexity : O(mn)
                    