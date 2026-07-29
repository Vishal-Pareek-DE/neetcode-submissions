import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #brute force
        res=[]
        temp=[]
        for i in range(len(nums)-k+1):
            temp=nums[i:k+i]
            res.append(max(temp))
        return res
                