import collections
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        b = sorted(collections.Counter(nums).items(), key=lambda x: x[1],reverse=True)[:k]
        return [i[0] for i in b]