class Solution:
    def romanToInt(self, s: str) -> int:
        rom_to_int={'I':1,
                    'V':5,
                    'X':10,
                    'L':50,
                    'C':100,
                    'D':500,
                    'M':1000}
        value=0
        n=len(s)
        for i in range(n-1):
            
            if rom_to_int[s[i]]<rom_to_int[s[i+1]]:
                value-=rom_to_int[s[i]]
            else:
                value+=rom_to_int[s[i]]
        value+=rom_to_int[s[n-1]]
        return value
