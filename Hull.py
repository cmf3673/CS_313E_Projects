## Problem: A convex hull is the smallest convex polygon that will enclose a set of points. 
# In a convex polygon a line joining any two points in the polygon will lie completely within 
# the polygon. One way to visualize a convex hull is as follows: imagine there are nails sticking 
# out over the distribution of points. Place a rubber band such that it encircles all the nails.

# Input: You will read your data from standard input.  
# The first line will be a single integer n denoting the 
# number of points, where n will be in the range 3 to 100 
# inclusive. It will be followed by n lines of data. Each line 
# will have the x and y coordinates of a point. The coordinates 
# of the points will be integers in the range (-200, 200).

# Output: For the given input you will print the vertices of the convex 
# hull starting at the extreme left point and going clockwise around the convex hull. 
# You will print your output to standard out as given in the following format hull.out.



import math
class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # string representation of a Point
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # equality tests of two Points
  def __eq__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

  def __ne__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

  def __lt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y < other.y)
    return (self.x < other.x)

  def __le__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y <= other.y)
    return (self.x <= other.x)

  def __gt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y > other.y)
    return (self.x > other.x)

  def __ge__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y >= other.y)
    return (self.x >= other.x)


# Returns a point list sorted by increasing x-coord. Inserstion sort.
def sort_points(point_list):
    for i in range(1, len(point_list)):
        j = i
        while j > 0 and point_list[j].x < point_list[j - 1].x:
            point_list[j], point_list[j - 1] = point_list[j - 1], point_list[j]
            j -= 1
    return point_list
    

# Input: p, q, r are Point objects
# Output: compute the determinant and return the value
def det (p, q, r):
    det = ((q.x * r.y) - (q.y * r.x)) - ((p.x * r.y) - (p.y * r.x)) + ((p.x * q.y) - (p.y * q.x))
    return det


# Input: sorted_points is a sorted list of Point objects
# Output: computes the convex hull of a sorted list of Point objects
#         convex hull is a list of Point objects starting at the
#         extreme left point and going clockwise in order
#         returns the convex hull
def convex_hull (sorted_points):
    # Upper Hull
    upper_hull = []
    # Add first two points .
    upper_hull.append(sorted_points[0])
    upper_hull.append(sorted_points[1])
    # Gets the Upper Hull ls.
    upper_hull = get_hull(sorted_points, upper_hull, True)

    # Lower Hull
    lower_hull = []
    # Adds the first two points.
    lower_hull.append(sorted_points[-1])
    lower_hull.append(sorted_points[-2])
    # Gets the Lower Hull ls.
    lower_hull = get_hull(sorted_points, lower_hull, False)

    # Takes out the first and last elements of lower_hull to avoid duplication.
    del lower_hull[0]
    del lower_hull[-1]
    
    hull = upper_hull + lower_hull
    return hull


# Gets either the upper or lower hull list.
def get_hull(sorted_points, hull_ls, upper):
    start = 2 if upper else len(sorted_points) - 3
    end = len(sorted_points) if upper else -1
    step = 1 if upper else -1

    for i in range(start, end, step):
        hull_ls.append(sorted_points[i])
        while (len(hull_ls) >= 3) and det(hull_ls[-3], hull_ls[-2], hull_ls[-1]) >= 0:
            del hull_ls[-2]
    return hull_ls


# Input: convex_poly is  a list of Point objects that define the
#        vertices of a convex polygon in order
# Output: computes and returns the area of a convex polygon
def area_poly (convex_poly): 
    n = len(convex_poly) - 1
    sum1 = 0
    sum2 = 0

    for i in range(0, len(convex_poly)):
        sum1 += (convex_poly[i].x * convex_poly[i + 1 if i != n else 0].y)

    for i in range(0, len(convex_poly)):
        sum2 += (convex_poly[i].y * convex_poly[i + 1 if i != n else 0].x)

    det = sum1 - sum2
    area = (1/2) * abs(det)
    return area


# Print the points.
def print_points(points):
    for point in points:
        print(point)


def main():
    # create an empty list of Point objects
    points = []
    num_points = eval(input())
    # read data from standard input
    # read line by line, create Point objects and store in a list
    for i in range(num_points):
        xy = input().split()
        points.append(Point(eval(xy[0]), eval(xy[1])))
    # sort the list according to x-coordinates
    sorted_points = sort_points(points)
    # get the convex hull
    c_hull = convex_hull(sorted_points)  
    # print your results to standard output
    print('Convex Hull')
    # print the convex hull
    print_points(c_hull)
    # get the area of the convex hull
    area = area_poly(c_hull)
    # print the area of the convex hull
    print()
    print(f'Area of Convex Hull = {area}')


if __name__ == "__main__":
  main()