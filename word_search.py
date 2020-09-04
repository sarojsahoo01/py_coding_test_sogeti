from typing import List

def findWords(board: List[List[str]], words: List[str]) -> List[str]:
    
    words = set(words)
    trie = {}
    
    for word in words:
        curr = trie
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        curr['-'] = {}
    
    output = set()
    visited = set()
    def dfs(r,c,path,currDict):
        nonlocal output

        if '-' in currDict:
            output.add(path)
        
        visited.add((r,c))
        
        offsets = [(0,-1),(0,1),(-1,0),(1,0)]
        
        for offset in offsets:
            newR = r + offset[0]
            newC = c + offset[1]
            
            if newR >= 0 and newR < len(board) and newC >= 0 and newC <len(board[0]) and (newR,newC) not in visited and board[newR][newC] in currDict:
                dfs(newR,newC,path+board[newR][newC],currDict[board[newR][newC]])
        visited.remove((r,c))
        
        
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] in trie:
                curr = trie
                dfs(row,col,board[row][col],curr[board[row][col]])
    
    return list(output)
