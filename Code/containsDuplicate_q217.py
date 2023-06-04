"""
    Given an integer array nums, return true if any value appears at least twice in the array, 
    and return false if every element is distinct.
"""


class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        has_dulplicates = False

        for num in nums:
            if num in seen:
                has_dulplicates = True
                return has_dulplicates
            seen.add(num)

        return has_dulplicates


solution = Solution()
print(solution.containsDuplicate([1, 0, 1]))
