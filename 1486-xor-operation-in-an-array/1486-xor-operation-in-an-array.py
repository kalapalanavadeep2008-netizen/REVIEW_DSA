class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        l=[]
        for i in range(n):
            
            l.append(start)
            start+=2
        x=0
        for num in l:
            x^=num
        return x