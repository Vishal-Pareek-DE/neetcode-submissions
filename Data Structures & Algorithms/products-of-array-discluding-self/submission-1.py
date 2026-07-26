class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        zero_cnt=0
        n=len(nums)
        res=[0]*n
        for num in nums:
            if num!=0:
                prod*=num 
            else:zero_cnt+=1
        if zero_cnt>1:return [0]*n
        for i,c in enumerate(nums):
            if zero_cnt:
                print(c,prod)
                res[i]=prod if c==0 else 0
            else:res[i]=prod//c
        return res
