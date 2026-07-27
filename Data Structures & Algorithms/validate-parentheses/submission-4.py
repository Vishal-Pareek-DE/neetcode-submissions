class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        lst=[]
        for i in range(len(s)):
            if i==0 and s[i] in (']','}',')'):
                return False
            elif s[i] in ('(','{','['):
                lst.append(s[i])
            elif lst and s[i] in (']','}') and ord(s[i])-2==ord(lst[-1]):
                lst.pop()
            elif lst and s[i] in (')') and ord(s[i])-1==ord(lst[-1]):
                lst.pop()
            else:return False
        if lst:
            return False
        else:return True