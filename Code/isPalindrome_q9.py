"""
Given an integer x, return true if x is a palindrome, and false otherwise.
"""
"""
    - First thought, convert to string, reverse, compare
    - Should set variable to False, only change if reversed string equals original string
"""


def isPalindrome(num):
    str_num = str(num)  # convert int to string
    reverse_str = str_num[::-1]  # reverses string for comparison

    isPalindrome = False

    if str_num == reverse_str:
        isPalindrome = True

    return isPalindrome


print(isPalindrome(121))
print(isPalindrome(991))
