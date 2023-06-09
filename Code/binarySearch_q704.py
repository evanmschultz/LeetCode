"""
    Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search 
    target in nums. If target exists, then return its index. Otherwise, return -1.

    You must write an algorithm with O(log n) runtime complexity.
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1

        while low <= high:
            middle = low + (high - low) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                low = middle + 1
            else:
                high = middle - 1

        return -1


solution = Solution()
print(solution.search([-1, 0, 3, 5, 9, 12], 2))
print(solution.search([-1, 0, 3, 5, 9, 12], 9))
