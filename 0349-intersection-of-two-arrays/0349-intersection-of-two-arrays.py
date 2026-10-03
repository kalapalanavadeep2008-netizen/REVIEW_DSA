class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst=[]
        for val1 in nums1:
            for val2 in nums2:
                if val1==val2:
                    lst.append(val1)
                    
        return list(set(lst))