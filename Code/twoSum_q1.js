/*
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order. 
*/

function twoSum(nums, target) {
    let seen = {}

    for (i = 0; i < nums.length; i++) {
        let num2 = target - nums[i]
        if (num2 in seen) {
            return [seen[num2], i]
        }
        seen[nums[i]] = i
    }
}

console.log(twoSum([6, 2, 3, 4, 5], 5))
console.log(twoSum([6, 2, 3, 4, 5], 6))
