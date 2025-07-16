class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        edge_len=len(matrix)
        top=0
        bottom=edge_len-1
        while top<bottom:
            for col in range(edge_len):
                temp=matrix[top][col]
                matrix[top][col]=matrix[bottom][col]
                matrix[bottom][col]=temp
            top+=1
            bottom-=1
        for r in range(edge_len):
            for c in range(r+1,edge_len):
                temp=matrix[r][c]
                matrix[r][c]=matrix[c][r]
                matrix[c][r]=temp
        '''   print(*matrix[0])
          print(*matrix[1])
          print(*matrix[2])'''
        
