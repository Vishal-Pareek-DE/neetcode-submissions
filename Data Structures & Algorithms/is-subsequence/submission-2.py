class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        sl,tl=len(s),len(t)
        j=0
        if tl<sl:
            return False
        elif sl==0:
            return True
        for i in range(tl):
            if s[j]==t[i]:
                j+=1
            if j==sl:
                return True
        else:
            return False