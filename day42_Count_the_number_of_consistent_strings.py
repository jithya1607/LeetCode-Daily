#42 Count the number of consistent strings
#Return the number of consistent strings in the array words. The strings in words are consistent if every character in the string appears in the string allowed.
def countConsistentStrings(allowed, words):
    a=0
    for i in words:
        b=0
        for j in range(len(i)):
            if i[j] in allowed:
                b+=1
        if b==len(i):
            a+=1
    return a