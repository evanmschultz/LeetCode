"""
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
    typically using all the original letters exactly once.
"""

"""
    check if length is the same (if not return false) - is this needed?
    need a list of letters from the first word with their count - use a dictionary
    need run through the second word, creating a new dictionary with letter and count pairs
    
    check if the next letter is in the first dictionary and if the count doesn't exceed first word count
"""

# set two dictionaries
# loop through first word
# for each letter (index) add key (letter) += 1 to dictionary
# nevermind

# sort both strings and make casing the same
# check if they are equal


# class Solution(object):
#     def isAnagram(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """

#         string1 = sorted(s, key=str.lower)
#         string2 = sorted(t, key=str.lower)

#         if string1 == string2:
#             return True
#         return False
"""
    I found the counter method which will help my first method work easier and better
"""


# class Solution(object):
#     def isAnagram(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         from collections import Counter

#         word1 = Counter(s)
#         word2 = Counter(t)

#         return word1 == word2

"""
    method using sets and count
"""


class Solution(object):
    def isAnagram(self, s, t):
        dictionary1 = {}
        dictionary2 = {}

        for letter in set(s):
            dictionary1[letter] = s.count(letter)

        for letter in set(t):
            dictionary2[letter] = t.count(letter)

        return dictionary1 == dictionary2


solution = Solution()
print(solution.isAnagram('cat', 'cat'))
