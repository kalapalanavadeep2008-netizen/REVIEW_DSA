class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        freq={}
        for num in arr:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        lst=[]
        for val in freq.values():
            lst.append(val)
        if len(lst)==len(set(lst)):
            return True
        else:
            return False 
            