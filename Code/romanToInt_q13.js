/*
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
*/

/* 
What do we know:
    - Roman numerals are strings that represent an integer
    - They are ordered from large to small expect in the special cases that it is a multiple of (10-1)
    - We will need to add up all the values in the string to get the arabic representation of the integer

What we can assume:
    - The string will be written correctly as a roman numeral (following all the rules)
    - The string will be written in only uppercase letters, no "ix"

What methodologies can we use:
    - We can create a key containing key: value pairs to use for translation into integers
    - We will need to loop through the string adding the translated value to a variable storing the total
    - We can create conditionals for the exceptions like (10-1)
    - Or, we can find a method to rewrite the string such that those exceptions are represented in a way
        that doesn't require subtraction, so we can simplify a loop without conditionals

What we need to do:
    - Find a method to replace elements in a string without otherwise changing the string
        - Will we need a temporary string?
    - Figure out how to get the value from an array based only on the key
*/

function romanToInt(str) {
    let conversions = {
        I: 1,
        V: 5,
        X: 10,
        L: 50,
        C: 100,
        D: 500,
        M: 1000,
    }
    let total = 0

    let tempStr = ""

    tempStr = str.replace("IV", "IIII").replace("IX", "VIIII")
    tempStr = tempStr.replace("XL", "XXXX").replace("XC", "LXXXX")
    tempStr = tempStr.replace("CD", "CCCC").replace("CM", "DCCCC")

    for (char of tempStr) {
        total += conversions[char]
    }

    return total
}

/* 
    Updated after seeing another person's elegant solution using one conditional
*/

function romanToInt2(str) {
    let conversions = {
        I: 1,
        V: 5,
        X: 10,
        L: 50,
        C: 100,
        D: 500,
        M: 1000,
    }
    let total = 0

    for (i = 0; i < str.length; i++) {
        if (conversions[str[i]] < conversions[str[i + 1]]) {
            total -= conversions[str[i]]
        } else {
            total += conversions[str[i]]
        }
    }

    return total
}

console.log("CMLXXIV equals:", romanToInt2("CMLXXIV"))
