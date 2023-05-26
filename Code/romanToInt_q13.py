"""
LeetCode question 13. 

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, 
which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four 
is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract 
it making four. The same principle applies to the number nine, which is written as IX. There are six 
instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
"""


def romanToInt(s):
    total = 0

    for i in range(len(s)):
        if s[i] == "I":
            if i + 1 < len(s):
                if s[i + 1] != "I":
                    total -= 1
                else:
                    total += 1
            else:
                total += 1

        if s[i] == "V":
            total += 5

        if s[i] == "X":
            if i + 1 < len(s):
                if s[i + 1] == "L" or s[i + 1] == "C":
                    total -= 10
                else:
                    total += 10
            else:
                total += 10

        if s[i] == "L":
            total += 50

        if s[i] == "C":
            if i + 1 < len(s):
                if s[i + 1] == "D" or s[i + 1] == "M":
                    total -= 100
                else:
                    total += 100
            else:
                total += 100

        if s[i] == "D":
            total += 500

        if s[i] == "M":
            total += 1000

    return total


print(romanToInt("CMLXXIV"))
print(romanToInt("IV"))


"""
New solution after looking at someone else's work
"""


# type hinting, showing what the expected outcome is, it is not enforcing the type
def romanToInt2(s: str) -> int:
    # dictionary to convert letter to int
    conversions = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    # use replace() method to convert to usable characters
    # convert 4 and 9
    s = s.replace("IV", "IIII")
    s = s.replace("IX", "VIIII")
    # convert 40 and 90
    s = s.replace("XL", "XXXX")
    s = s.replace("XC", "LXXXX")
    # convert 400 and 900
    s = s.replace("CD", "CCCC")
    s = s.replace("CM", "DCCCC")

    total = 0

    # loop through the characters in the string and compare with dict then add to the total
    for char in s:
        total += conversions[char]

    return total


print(romanToInt2("CMLXXIV"))
print(romanToInt2("IV"))
