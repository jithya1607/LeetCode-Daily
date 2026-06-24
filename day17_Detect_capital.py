#17 Detect Capital
# Given a string word, return True if the string is a valid capitalization.
# A valid capitalization is defined as follows:
# 1. All letters are uppercase (e.g., "USA")
# 2. All letters are lowercase (e.g., "leetcode")
# 3. Only the first letter is uppercase and the rest are lowercase (e.g., "Google")
def detectCapitalUse(word):
        return word.isupper() or word.islower() or word.istitle()