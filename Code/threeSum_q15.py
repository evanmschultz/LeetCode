"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""


def threeSum(nums):  # brute force
    nums.sort()
    results = []

    for i, num in enumerate(nums):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if num + nums[j] + nums[k] == 0:
                    temp = [num, nums[j], nums[k]]
                    temp.sort()
                    if temp not in results:
                        results.append(temp)

    return results


def threeSum2(nums):
    nums.sort()
    results = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        left, right = i + 1, len(nums) - 1

        while left < right:
            temp_sum = nums[i] + nums[left] + nums[right]

            if temp_sum == 0:
                temp_res = [nums[i], nums[left], nums[right]]
                temp_res.sort()

                if temp_res not in results:
                    results.append(temp_res)

                left += 1
                right -= 1
            elif temp_sum < 0:
                left += 1
            else:
                right -= 1

    return results


print(threeSum2([-1, 0, 1, 2, -1, -4]))  # [-4, -1, -1, 0, 1, 2]
