#2.Roman to integer
#Given a roman numeral, convert it to an integer.
def romanToInt(self, s: str) -> int:
        a=0
        d={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        for i in range(len(s)):
            if i+1<len(s):
                if d[s[i]]>=d[s[i+1]]:
                    a+=d[s[i]]
                else:
                    a-=d[s[i]]
            else:
                a+=d[s[i]]
        return a