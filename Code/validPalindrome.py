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

    # method using pointers so that it has constant space complexity, still has linear time complexity
    def isPalindrome_2(self, string):
        left, right = 0, len(string) - 1  # set the pointers

        while left < right:
            # check if the character at the left pointer is alphanumeric and left is less than right
            while left < right and not self.alphaNum(string[left]):
                left += 1  # increment left pointer

            # check if the char at the right pointer is alphanumeric and left is less than right
            while right > left and not self.alphaNum(string[right]):
                right -= 1  # decrement right pointer

            # return false if the characters do not match
            if string[left].lower() != string[right].lower():
                return False

            left, right = left + 1, right - 1  # move both pointers

        return True  # full string analyzed, must be a valid palindrome

    # helper function to check if a character is alphanumeric
    def alphaNum(self, char):
        if ord('A') <= ord(char) <= ord('Z') or ord('a') <= ord(char) <= ord('z') or ord('0') <= ord(char) <= ord('9'):
            return True
        return False


solution = Solution()
print(solution.isPalindrome_2('A man, a plan, a canal: Panama'))
