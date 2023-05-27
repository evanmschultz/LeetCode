'''
    Given a sorted array of distinct integers and a target value, return the index if the target is found. 
    If not, return the index where it would be if it were inserted in order.

    You must write an algorithm with O(log n) runtime complexity.
'''


def searchInsert(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (high + low) // 2
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            return mid

    return low


print(searchInsert([1, 3, 5, 6], 7))
