class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell=0
        buy=float('inf')
        i,r=0,1
        l=len(prices)
        ans=0
        while r<l and i<l:
            if buy>=prices[i]:
                buy=min(buy,prices[i])
                sell=0
            if prices[r]>buy:
                sell=max(sell,prices[r])
            i+=1
            r+=1
            ans=max(ans,sell-buy)
        return ans


        
        