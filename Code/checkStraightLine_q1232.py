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


"""
    three points (x,y), (x1,y1), (x2,y2)
    assume the intercepts are the same
    y - mx = y1 - mx1 -> y - y1 = m(x - x1) -> m = (y - y1) / (x - x1) - assuming slope is equal
    y - mx = y2 - mx2 -> y - y2 = m(x - x2) -> m = (y - y2) / (x - x2) 
    (y - y1) / (x - x1) = (y - y2) / (x - x2) 

    formuala
    (y - y1) * (y - y2) = (x - x1) * (x - x2)

    assume all points are co-linear, if any are not return false
"""


class Solution(object):
    # simply use the slope to check if they are co-linear
    def checkStraightLine(self, coordinates):
        (x0, y0), (x1, y1) = coordinates[0], coordinates[1]
        for x, y in coordinates:
            if (x1 - x0) * (y - y1) != (x - x1) * (y1 - y0):
                return False
        return True


# Works perfectly here, but leetcode says it produces the wrong answer at test 78/79 / still not optimal or simple enough
# class Solution(object):
#     def checkStraightLine(self, list):
#         if len(list) == 2:
#             return True

#         vertical = False
#         slope = 0
#         intercept = 0

#         if list[1][0] == list[0][0]:
#             vertical = True
#         else:
#             slope = (list[1][1] - list[0][1]) / (list[1][0] - list[0][0])
#             intercept = list[0][1] - slope * list[0][0]

#         for point in list:
#             if vertical:
#                 if point[0] == list[0][0]:
#                     continue
#                 else:
#                     return False
#             if 0 != slope * point[0] + intercept - point[1]:
#                 return False

#         return True

solution = Solution()


print(solution.checkStraightLine([[2, 1], [4, 2], [6, 3]]))
