#39 Check if Two String Arrays are Equivalent
# Given two string arrays word1 and word2, return True if the two arrays represent the same string, and False otherwise.
# The string represented by an array is the concatenation of all the strings in the array in order.
def checkIfTwoStringArraysAreEquivalent(word1, word2):
    return ''.join(word1) == ''.join(word2)