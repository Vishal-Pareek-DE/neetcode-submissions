class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        maxl,seq=0,0
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]==1:                
                maxl=maxl+1
            elif nums[i]-nums[i-1]==0:
                continue
            else:
                maxl=0
            seq=max(seq,maxl)
        if len(set(nums))==1:
            return 1
        elif len(nums)==0:
            return 0
        else: return seq+1 
        