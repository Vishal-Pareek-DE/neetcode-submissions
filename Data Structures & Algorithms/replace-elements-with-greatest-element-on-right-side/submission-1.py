class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l=len(arr)
        max_right=-1
        for i in range(l-1,-1,-1):
            new=max_right
            max_right=max(max_right,arr[i])
            arr[i]=new
        return arr