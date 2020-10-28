from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        n = sorted(nums)
        l = []
        for i in nums:
            l.append(n.index(i))
        return l

from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        n = sorted(nums)

        k = {}
        l = []
        for i in nums:
            if i not in k:
                k[i] = n.index(i)
            l.append(k[i])
        return l