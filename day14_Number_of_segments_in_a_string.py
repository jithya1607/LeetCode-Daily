#14. Number of Segments in a String
# Given a string s, return the number of segments in the string.
def countSegments(s: str) -> int:
    return len(s.split())