from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.append("L")
        n =0
        while 1:
            lindex = nums.index("L")
            if nums[n] == "L":
                break
            elif nums[n] == 2:
                nums.append(2)
                nums.pop(n)
            elif nums[n] ==1:
                nums.insert(lindex+1,1)
                nums.pop(n)
            else:
                n += 1
        nums.remove("L")