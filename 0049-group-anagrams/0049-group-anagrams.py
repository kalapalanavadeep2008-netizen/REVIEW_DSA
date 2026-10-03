class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        freq={}
        for word in strs:
            key="".join(sorted(word))
            
            if key not in freq:
                freq[key]=[]
            freq[key].append(word)
        return list(freq.values())