#8 Valid anagram
#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
def isAnagram(self, s: str, t: str) -> bool:
       if len(s)==len(t):
           a=sorted(list(s))
           b=sorted(list(t))
           if a==b:
               return True
           else:
               return False
       else:
           return False