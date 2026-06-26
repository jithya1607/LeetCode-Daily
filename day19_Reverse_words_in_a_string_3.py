#19 Reverse words in a string-3
# Given an input string s, reverse each word while maintaining the order of words.
def reverseWords(self, s: str) -> str:
    a=s.split()
    return ' '.join([i[::-1] for i in a])