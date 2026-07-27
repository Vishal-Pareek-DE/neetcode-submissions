class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        lst=[]
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        for i in range(len(s)):
            if s[i] in closeToOpen.values():
                lst.append(s[i])
            elif lst and s[i] in closeToOpen and lst[-1] == closeToOpen[s[i]]:
                lst.pop()
            else:
                return False

        return not lst