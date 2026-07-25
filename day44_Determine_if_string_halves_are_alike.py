#44 Determine if String Halves Are Alike
# Divide a string into two halves and check if they are alike based on the number of vowels in each half.
def halvesAreAlike(s):
    a=s[:len(s)//2]
    a1=0
    b=s[len(s)//2:]
    b1=0
    for i in range(len(a)):
        if a[i] in 'aeiouAEIOU':
            a1+=1
    for i in range(len(a)):
        if b[i] in 'aeiouAEIOU':
            b1+=1
    return a1==b1