class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # row length = len(board)
        # col length = len(board[0])
        ROWS, COLS = len(board), len(board[0])

        # when explored, mark as visited (hash set)
        visited_path = set()
        
        # backtracking => use recursion
        def dfs(r, c, i):
            if i == len(word):
                return True
            
            # cases failing to form word
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r, c) in visited_path):
                return False
            # but if these satisfy => try 4 directions for next char
            else: 
                # backtracking: add
                visited_path.add((r, c))
                res = (dfs(r+1, c, i+1)
                        or dfs(r, c+1, i+1)
                        or dfs(r-1, c, i+1)
                        or dfs(r, c-1, i+1))
                # backtracking: remove
                visited_path.remove((r,c)) # for different cell start
                
                return res
        
        # for every cell, we try to start the word there
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False