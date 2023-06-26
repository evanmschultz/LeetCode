'''
    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
    removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric 
    characters include letters and numbers.

    Given a string s, return true if it is a palindrome, or false otherwise.
'''


class Solution(object):
    def isPalindrome(self, string):
        # split the string and rejoin without special characters using method `isalnum()` and turn to lowercase
        alpha_num = ''.join(char for char in string if char.isalnum()).lower()

        # compare alpha_num with its reversed string and return true if equal or false if not
        return alpha_num == alpha_num[::-1]


solution = Solution()
print(solution.isPalindrome('A man, a plan, a canal: Panama'))
