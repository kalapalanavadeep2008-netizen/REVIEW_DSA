class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        c=0
        l=[]
        for i in range(len(nums)):
            c+=nums[i]
            l.append(c)
        return l