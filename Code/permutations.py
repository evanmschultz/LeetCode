"""
    Problem 46: Permutations
    
    Given an array nums of distinct integers, return all the possible permutations. 
    You can return the answer in any order.
"""


class Solution(object):
    def permute(self, nums: list[int]) -> list[list[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results: list[list[int]] = []

        # Base case
        if len(nums) == 1:
            return [nums.copy()]

        for i in nums:
            num: int = nums.pop(0)
            permutations: list[list[int]] = self.permute(nums)

            for permutation in permutations:
                permutation.append(num)

            results.extend(permutations)
            nums.append(num)

        return results


solution = Solution()
nums: list[int] = [1, 2, 3]
result: list[list[int]] = solution.permute(nums)
print(result)
