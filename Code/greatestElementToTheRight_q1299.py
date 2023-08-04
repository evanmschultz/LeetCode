'''
Given an array arr, replace every element in that array with the 
greatest element among the elements to its right, and replace the 
last element with -1.

After doing so, return the array.
'''


class Solution(object):
    def replaceElements(self, arr: list[int]) -> list[int]:
        """
        This function replaces every element in an array with the maximum element 
        among the elements to its right, and replaces the last element with -1.

        :type arr: List[int]
        :rtype: List[int]
        """
        # Initialize max value, will be used to set the last element to -1
        max_val: int = -1
        # Loop through the array by starting from the last element
        for i in range(len(arr) - 1, -1, -1):
            # Temporarily store the current element
            temp: int = arr[i]
            # Replace the current element with the max value
            arr[i] = max_val
            # Update max value
            max_val = max(max_val, temp)
        return arr


solution = Solution()
print(solution.replaceElements([17, 18, 5, 4, 6, 1]))
