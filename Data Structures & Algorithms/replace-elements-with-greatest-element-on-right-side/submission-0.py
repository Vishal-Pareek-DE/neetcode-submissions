class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            if i==len(arr)-1:
                arr[i]=-1
                break;
            elif i==(len(arr)-1):
                arr[i]=arr[i] if arr[i]>arr[-1] else arr[-1]
            else:
                m=max(arr[i+1:])
                arr[i]=m
        return arr