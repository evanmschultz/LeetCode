'''
    Problem 139: Word Break
    Given a string s and a dictionary of strings wordDict, return true if s can 
    be segmented into a space-separated sequence of one or more dictionary words.

    Note that the same word in the dictionary may be reused multiple times in the 
    segmentation.
'''


class Solution(object):
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        This function uses Dynamic Programming (dp) to determine if the input string 's' 
        can be segmented into a space-separated sequence of one or more dictionary words.
        """
        # Initialize a boolean list 'dp' of length len(s) + 1, set all indices to False initially
        dp: list[bool] = [False] * (len(s) + 1)

        # Set dp[len(s)] to True as an empty string can always be segmented
        dp[len(s)] = True

        # Iterate over 's' from the end towards the beginning
        for i in range(len(s) - 1, -1, -1):
            # Iterate over all the words in the word dictionary
            for word in wordDict:
                # Check if the word fits into the remaining substring from the index 'i'
                # and if it matches the current slice of the string
                if (i + len(word)) <= len(s) and s[i: i + len(word)] == word:
                    # If the above conditions are met, that means we can segment the string
                    # at this index, so we mark it as True
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    # If the current index is marked as True, we don't need to check the remaining words
                    # and we can break out of the inner loop to move to the next index
                    break

        # If the string can be segmented, dp[0] would have been set to True
        return dp[0]


solution = Solution()
print(solution.wordBreak("leetcode", ["leet", "code"]))
