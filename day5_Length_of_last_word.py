#5.Length of last word
#Given a string s consisting of words and spaces, return the length of the last word in the string.
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a=s.split()
        return len(a[-1])