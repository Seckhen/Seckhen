class Solution:
    def isValid(self, s: str) -> bool:
        if "(]" in s:
            return false 
        if "(}" in s:
            return false 
        if "[)" in s:
            return false 
        if "[}" in s:
            return false 
        if "{)" in s:
            return false 
        if "{]" in s:
            return false 
        else:
            return True
        