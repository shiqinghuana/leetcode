import itertools
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l = []
        for i in range(len(nums)+1):
            z = itertools.combinations(nums,i)
            for b in z:
                l.append(b)
        return l