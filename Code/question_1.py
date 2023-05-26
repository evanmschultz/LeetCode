"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order. 
"""

"""
    - Create a function takes two parameters, an arr and a target number
    - Use the difference of the target number and the current number to search through the list for the complement
"""


def twoSum(list, target):
    for i in range(len(list)):
        if list[i] >= target:
            continue
        num_2 = target - list[i]
        if num_2 in list:
            i_2 = list.index(num_2)
            return i, i_2


list = [6, 2, 3, 4, 5]
print(twoSum(list, 5))

"""
    Solution 2: using a set to store numbers that have been "seen" in the list and enumeration to avoid having to find the index
"""


def twoSum2(list, target):
    seen = set()

    for i, num in enumerate(list):
        if target - num in seen:
            comp_i = list.index(target - num)
            return comp_i, i
        seen.add(num)


print(twoSum2(list, 5))
