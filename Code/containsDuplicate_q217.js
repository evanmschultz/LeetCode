/* 
    Given an integer array nums, return true if any value appears at least twice in the array, 
    and return false if every element is distinct.
*/

function containsDuplicate(nums) {
    let seen = new Set()

    for (i = 0; i < nums.length; i++) {
        if (seen.has(nums[i])) {
            return true
        }
        seen.add(nums[i])
    }

    return false
}

console.log(containsDuplicate([1, 2, 3, 1]))
console.log(containsDuplicate([1, 2, 3, 4]))
