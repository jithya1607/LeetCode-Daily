#23 Occurrences after bigram
# Given words first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.
# For each such occurrence, add "third" to the answer, and return the answer.
def findOcurrences(text, first, second):
    try:
        a=text.split()
        b=[]
        for i in range(len(a)):
            if a[i]==first and a[i+1]==second:
                b.append(a[i+2])
    except:
        pass
    return b