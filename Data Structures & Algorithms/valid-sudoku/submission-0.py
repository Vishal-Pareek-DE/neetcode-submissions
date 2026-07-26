class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       
        if len(board)!=9:return False
        for i in range(9):
            dictr=defaultdict(int)
            dictc=defaultdict(int)
            if len(board[i])!=9 :return False
            for j in range(9):
                if board[i][j] not in '123456789.':return False
                if board[j][i] not in '123456789.':return False
                dictr[board[i][j]]=dictr[board[i][j]]+1 if board[i][j]!='.' else 0
                dictc[board[j][i]]=dictc[board[j][i]]+1 if board[j][i]!='.' else 0
            for i in dictr.values():
                if i>1:return False
            for i in dictc.values():
                if i>1:return False
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True
            