# Works perfectly here, but leetcode says it produces the wrong answer at test 78/79


"""
    You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. 
    Check if these points make a straight line in the XY plane.
"""

# y = mx + b -> m = (y - b) / x ignore b
# find the slope (y2 - y1) / (x2 - x1) -> 5 / 5 slope = 1

"""
    check if length of list is == 2, if so return true
    solve for m using the first two coordinates
    solve for b using the first coordinate
    for loop:
        evaluate if 0 == mx - b - y, if not, return false

    return true

    - how do I do it if it is a vertical line?
        - vertical lines have the same x value for everything

    check if the the first two points have the same x value
        if yes, set variable vertical to True
        use vertical variable inside loop to check if the x value is the same for all points

"""


class Solution(object):
    def checkStraightLine(self, list):
        if len(list) == 2:
            return True

        vertical = False
        slope = 0
        intercept = 0

        if list[1][0] == list[0][0]:
            vertical = True
        else:
            slope = (list[1][1] - list[0][1]) / (list[1][0] - list[0][0])
            intercept = list[0][1] - slope * list[0][0]

        for point in list:
            if vertical:
                if point[0] == list[0][0]:
                    continue
                else:
                    return False
            if 0 != slope * point[0] + intercept - point[1]:
                return False

        return True


solution = Solution()


print(solution.checkStraightLine([[2, 1], [4, 2], [6, 3]]))
