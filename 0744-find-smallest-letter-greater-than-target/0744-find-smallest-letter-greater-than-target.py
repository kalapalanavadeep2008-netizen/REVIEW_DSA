class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        for ch in range(len(letters)):
            if ord(target)<ord(letters[ch]):
                return letters[ch]
                
        return letters[0]

