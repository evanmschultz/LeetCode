/* 
    Given a sorted array of distinct integers and a target value, return the index if the target is found. 
    If not, return the index where it would be if it were inserted in order.

    You must write an algorithm with O(log n) runtime complexity.
*/

function searchInsert(nums, target) {
    low = 0
    high = nums.length - 1

    while (low <= high) {
        mid = Math.floor((low + high) / 2)

        if (nums[mid] < target) {
            low = mid + 1
        } else if (nums[mid] > target) {
            high = mid - 1
        } else {
            return mid
        }
    }

    return low
}

console.log(searchInsert([1, 3, 5, 6], 2))
