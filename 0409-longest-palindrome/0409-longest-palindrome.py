class Solution(object):
    def longestPalindrome(self, s):
        freq = {}
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1


        count = 0
        flag = []
        for k,v in freq.items():
            count += (v//2)*2   #
            if v%2 == 1:
               flag = 1
        if flag:

            return count+1
        else:
            return count
        