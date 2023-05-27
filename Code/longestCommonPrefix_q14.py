'''
    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".
'''


'''
    - loop through list of words create a variable to store the current prefix character in the first word in the list
        - only loop through the first word as the common prefix cannot be longer than any of the words in the list
    - loop through each word in the list
        - make sure i is not equal to the length of the word checking for the end of the word
        - also check, using 'or', if the current character in the word is not equal to the character stored from the first word in the list
        - if those conditions are met exit the function by returning the longest common prefix
    - inside the main for loop add the charactert to the longest common prefix variable
'''




import time
def longestCommonPrefix(list):
    longestCommonPrefix = ''

    for i in range(len(list[0])):
        char = list[0][i]
        # print(f'i = {i}, char = {char}')
        for word in list:
            # print(f'word = {word}')
            if i == len(word) or word[i] != char:
                return longestCommonPrefix
        # print(f'adding {char} to longestCommonPrefix\n')
        longestCommonPrefix += char

    return longestCommonPrefix


# print('the longest common prefix is: ' +
#       longestCommonPrefix(["flower", "flower", "flower"]))

# print('the longest common prefix is: ' +
#       longestCommonPrefix(["flower", "flow", "flight"]))

# print('the longest common prefix is: ' +
#       longestCommonPrefix(["flower", "dove", "flight"]))

'''
    Updated version using built in functions to speed it up, should still have O(nk) time complexity
'''


def longestCommonPrefix2(list):
    prefix = min(list, key=len)

    for word in list:
        # count = 1
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            # print(f'while loop count: {count}')
            # count += 1

    return prefix


# print('the longest common prefix is: ' +
#       longestCommonPrefix2(["flower", "flower", "flower"]))

# print('the longest common prefix is: ' +
#       longestCommonPrefix2(["flower", "flow", "flight"]))

# print('the longest common prefix is: ' +
#       longestCommonPrefix2(["flower", "f", "flight"]))

start = time.time()
longestCommonPrefix2(["flower", "flower", "flower"])
end = time.time()

print(f'Runtime of longestCommonPrefix2() is {end - start} seconds')
