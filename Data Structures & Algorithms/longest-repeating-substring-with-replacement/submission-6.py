class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        maxf=l=res=0
        for r in range(len(s)):
            count[s[r]]=1+count.get(s[r],0)
            maxf=max(maxf,count[s[r]])
            if r-l+1-maxf>k:
                count[s[l]]-=1
                l+=1
                print(r-l+1-maxf)
            res=max(res,r-l+1)
            print(f'count:{count},r:{r},l:{l},res:{res}')
        return res
            
