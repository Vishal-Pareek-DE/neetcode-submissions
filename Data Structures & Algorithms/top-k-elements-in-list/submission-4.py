from collections import Counter
from typing import List
class Solution:
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic=defaultdict(int)
        j=[]
        for i in nums:
            dic[i]+=1
        jj=set(sorted(list(dic.values()),reverse=True)[:k])
        for key,value in dic.items():
            if value in jj:
                j.append(key)
        return j
    """


    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        return [num for num, freq in counts.most_common(k)]
  