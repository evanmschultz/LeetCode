/*
Given an integer x, return true if x is a palindrome, and false otherwise.
*/

function isPalindrome(num) {
    let str = num.toString()
    let split = str.split("")
    let reverse = split.reverse()
    let reversed = reverse.join("")

    let isPalindrome = false

    if (str == reversed) {
        isPalindrome = true
    }

    return isPalindrome
}

console.log(isPalindrome(44344))
console.log(isPalindrome(121))
