class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res,area=0,0
        l,r=0,len(heights)-1
        while l<r:
            area=max(area,min(heights[l],heights[r])*(r-l))
            if heights[l+1]>heights[l]:
                l+=1
            elif heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        print(heights[l],heights[r])
        return area
        