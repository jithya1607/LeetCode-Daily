#6.Valid palindrome
#Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=''
        for i in s:
            if i.isalnum():
                a+=i.lower()
        if a==a[::-1]:
            return True
        else:
            return False