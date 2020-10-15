import collections
import copy
from typing import List


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        s = []
        for i in edges:
            s += i
        yuan = s
        jianzhi = []  # 待剪的分支
        while 1:
            d = dict(collections.Counter(s))

            for k, v in d.items():
                if v == 1:
                    index = s.index(k)
                    if index % 2 == 0:
                        index += 1
                    s = s[:index - 1] + s[index + 1:]

                    # pint(s)

            if 1 not in d.values():
                isOk = []
                #print(s)
                for i in range(1, len(s), 2):
                    kill = [int(s[i - 1]), int(s[i])]
                    edge = copy.deepcopy(edges)
                    #print(kill)
                    edge.remove(kill)
                    # print(len(self.has_root(edge)))
                    if len(self.has_root(edge)) == 1:
                        isOk.append(kill)
                return isOk[-1]

    def has_root(self, s: List[List[int]]) -> set:  # 判断有几个根节点
        root = set()
        child = set()
        for i in s:
            root.add(i[0])
            child.add(i[1])
        return root - child