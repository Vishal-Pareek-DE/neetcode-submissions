class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n,m=len(s),len(t)
        j=0
        """
        def subseq(i:int,j:int) -> int:
            if m==j:
                return 0
            if n==i:
                return m-j
            if s[i]==t[j]:
                return subseq(i+1,j+1)
            else:
                return subseq(i+1,j)
        return subseq(0,0) 
        """
        for i in range(n):
            if m==j:
                return 0  
            if s[i]==t[j]:
                j+=1
        return m-j