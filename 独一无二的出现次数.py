import collections
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        l = set()
        for i in set(arr):
            a = arr.count(i)
            if a in l:
                return False
            l.add(a)
        return True


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        a = dict(collections.Counter(arr)).values()
        b = dict(collections.Counter(a)).values()
        return all(i ==1 for i in b)