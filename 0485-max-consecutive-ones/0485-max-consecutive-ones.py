class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count=0
        max_count=0
        for i in nums:
            if i==1:
                count+=1
                if count>max_count:
                    max_count=count
            else:
                count=0
        return max_count