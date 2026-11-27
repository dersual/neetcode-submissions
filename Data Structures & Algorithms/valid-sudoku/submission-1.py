from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool: 
        rows = defaultdict(set) 
        cols = defaultdict(set) 
        boxes = defaultdict(set) 

        for row in range(len(board)): 
            for col in range(len(board[row])): 
                if board[row][col] == ".": 
                    continue  
                num = board[row][col] 

                if num in rows[row]: 
                    return False 
                if num in cols[col]:
                    return False   
                
                coords = (row//3, col//3) 
                if num in boxes[coords]: 
                    return False 
                
                rows[row].add(num) 
                cols[col].add(num) 
                boxes[coords].add(num) 
        
        return True
        