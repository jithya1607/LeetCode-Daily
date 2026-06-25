#18 Student Attendance Record I
#Return true if the student could be rewarded according to the following criteria:
#The student was absent ('A') for strictly fewer than 2 days total.
#The student was never late ('L') for 3 or more consecutive days.
def checkRecord(self, s: str) -> bool:
    if s.count('A')<2 and 'LLL' not in s:
        return True
    else:
        return False