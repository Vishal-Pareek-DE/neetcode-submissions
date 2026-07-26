class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l=len(strs)
        if l<=1:return [strs]
        dic=defaultdict(list)
        for i in range(l):
            dic["".join(sorted(strs[i]))].append(strs[i])
            
        return list(dic.values())
