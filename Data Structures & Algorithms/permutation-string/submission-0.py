class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1=len(s1)
        l2=len(s2)
        l=0
        sn1=sorted(s1)
        r=l1
        if l1>l2:
            return False
        while r <=l2:
            if sorted(s2[l:r])==sn1:
                return True
            print(s2[l:r])
            l+=1
            r+=1
            
        return False