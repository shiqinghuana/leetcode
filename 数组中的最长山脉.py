from typing import List


class Solution:
    def longestMountain(self, A: List[int]) -> int:

        z = [0, 0]  # 初始化山，左右两侧必须都存在
        l = 0  # 山的长度
        for i in range(len(A) - 1):
            if A[i] < A[i + 1]:
                # 山的左侧
                if z[0] and z[1]:
                    l = max(l, z[0] + z[1] + 1)
                    z = [0, 0]  # 初始化山，左右两侧必须都存在
                z[0] += 1
            elif A[i] > A[i + 1] and z[0] != 0:
                z[1] += 1
            elif A[i] == A[i + 1]:
                if z[0] and z[1]:
                    l = max(l, z[0] + z[1] + 1)
                z = [0, 0]  # 初始化山，左右两侧必须都存在
        if z[0] and z[1]:
            l = max(l, z[0] + z[1] + 1)
        return l
