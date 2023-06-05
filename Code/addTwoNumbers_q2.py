"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single 
digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 
0 itself.
"""


# def addTwoNumbers(list1, list2):
#     num1 = 0
#     num2 = 0
#     final = []

#     for i in range(len(list1) - 1, -1, -1):
#         multiple = 10 ** i

#         num1 += list1[i] * multiple

#     for i in range(len(list2) - 1, -1, -1):
#         multiple = 10 ** i

#         num2 += list2[i] * multiple

#     string = str(num1 + num2)

#     for char in string:
#         final.append(int(char))

#     return final


# print(addTwoNumbers([2, 4, 3], [5, 6, 4]))

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def addTwoNumbers(list1, list2):
    print("function call\n")
    dummy = ListNode()
    current = dummy
    carry = 0

    while list1 or list2:
        # Get the values of the current nodes
        num1 = list1.value if list1 else 0
        num2 = list2.value if list2 else 0

        # Compute the sum and carry
        total = num1 + num2 + carry
        carry = total // 10
        digit = total % 10

        # Create a new node with the digit and update the current node
        current.next = ListNode(digit)
        current = current.next

        # Move to the next nodes, if available
        if list1:
            list1 = list1.next
        if list2:
            list2 = list2.next

    # If there is a remaining carry, create a new node
    if carry > 0:
        current.next = ListNode(carry)

    return dummy.next


# Example usage
# list1: 2 -> 4 -> 3 (represents the number 342)
# list2: 5 -> 6 -> 4 (represents the number 465)
list1 = ListNode(2)
list1.next = ListNode(4)
list1.next.next = ListNode(3)

list2 = ListNode(5)
list2.next = ListNode(6)
list2.next.next = ListNode(4)

result = addTwoNumbers(list1, list2)

# Print the resulting linked list
while result:
    print(result.value, end=" ")
    result = result.next

# Output: 7 0 8 (which represents the number 807)
