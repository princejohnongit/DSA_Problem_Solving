class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n=numRows
        if n==1 or len(s)<n:
            return s
        res=[[] for _ in range(n)]
        print(res)
        going_down=False
        current_row=0
        for char in s:
            res[current_row].append(char)
            if current_row==0:
                going_down=True
            elif current_row==n-1:
                going_down=False
            if going_down:
                current_row+=1
            else:
                current_row-=1           
        return ''.join(''.join(each_list) for each_list in res)
        
