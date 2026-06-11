#4.Valid Parentheses
#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid if the brackets are closed in the correct order.
class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        b=[]
        c,d,e,f,g,h=0,0,0,0,0,0
        if len(s)%2!=0:
            return False
        else:
            for i in range(len(s)):
                if s[i]=='(' or s[i]=='[' or s[i]=='{':
                    a.append(s[i])
                    b.append(s[i])
                else:
                    if len(a)!=0:
                        if s[i]==')' and a[-1]=='(':
                            a.pop()
                        elif  s[i]==']' and a[-1]=='[':
                            a.pop()
                        elif  s[i]=='}' and a[-1]=='{':
                            a.pop()
                        else:
                            break
        for i in range(len(s)):
            match s[i]:
                case '(':
                    c+=1
                case ')':
                    d+=1
                case '[':
                    e+=1
                case ']':
                    f+=1
                case '{':
                    g+=1
                case '}':
                    h+=1
        if c!=d or e!=f or g!=h:
            return False
        if len(s)>0 and len(b)==0:
            return False
        if len(a)==0:
            return True
        else:
            return False