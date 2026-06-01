#3.Longest common prefix
#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string "".
from typing import List


def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        else:
            a=''
            b=[]
            flag=0
            for i in strs:
                b.append(len(i))
            c=min(b)
            for i in range(c):
                d=strs[0][i]
                for j in range(1,len(strs)):
                    if d==strs[j][i]:
                        flag=1
                    else:
                        flag=0
                        break
                if flag==1:
                    a+=d
                else:
                    break
            return a