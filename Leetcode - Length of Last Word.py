class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s= s.split()
        index = len(s)-1
        return(len(s[index]))

        