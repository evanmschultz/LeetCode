"""
    Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

    Return the running sum of nums.
"""


class Solution(object):
    def runningSum(self, nums):
        output_array = []
        running_sum = 0

        for num in nums:
            running_sum += num
            output_array.append(running_sum)

        return output_array


solution = Solution()
print(solution.runningSum([1, 2, 3, 4]))
