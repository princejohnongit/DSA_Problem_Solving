class Solution:
    def intToRoman(self, num: int) -> str:
        #lets make a tuple set
        value_symbols=[(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),
                        (100,'C'),(90,'XC'),(50,'L'),(40,'XL'),
                        (10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
        res=[]
        for value,symbol in value_symbols:
            if num==0:
                break
            count=num//value
            res.append(count*symbol)
            num=num-count*value
        return ''.join(res)
