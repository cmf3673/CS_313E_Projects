## Problem: This assignment is on object oriented programming. You will be developing 
# several classes that are fundamental in Solid Geometry - Point, Sphere, Cube, and Cylinder. 
# In main() you will test the various functions that you have written for the classes.


import math

class Point(object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0):
      self.x = x
      self.y = y
      self.z = z

  # create a string representation of a Point
  # returns a string of the form (x, y, z)
  def __str__(self):
      return '({}, {}, {})'.format(self.x, self.y, self.z)

  # get distance to another Point object
  # other is a Point object
  # returns the distance as a floating point number
  def distance(self, other):
      return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)

  # test for equality between two points
  # other is a Point object
  # returns a Boolean
  def __eq__(self, other):
      tol = 1.0e-6
      return (abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol) and (abs(self.z - other.z) < tol)

  # Helper fucntion.
  # Takes one 3D point and calulates the distance on the x-y plane to the center of sphere. 
  def xy_distance(self, other):
      return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

class Sphere(object):
  # constructor with default values
  def __init__(self, x = 0, y = 0, z = 0, radius = 1):
      self.center = Point(x, y, z)
      self.r = radius

  # returns string representation of a Sphere of the form:
  # Center: (x, y, z), Radius: value
  def __str__(self):
      return 'Center: ({}, {}, {}), Radius: {}'.format(self.center.x, self.center.y, self.center.z, self.radius)

  # compute surface area of Sphere
  # returns a floating point number
  def area(self):
      return 4 * math.pi * self.r**2

  # compute volume of a Sphere
  # returns a floating point number
  def volume(self):
      return (4/3) * math.pi * self.r**3

  # determines if a Point is strictly inside the Sphere
  # p is Point object
  # returns a Boolean
  def is_inside_point(self, p):
      return self.center.distance(p) < self.r # Maybe need to add self.center as argument

  # determine if another Sphere is strictly inside this Sphere
  # other is a Sphere object
  # returns a Boolean
  def is_inside_sphere(self, other):
    d_centers = self.center.distance(other.center)
    return d_centers + other.r < self.r

  # determine if a Cube is strictly inside this Sphere
  # determine if the eight corners of the Cube are strictly 
  # inside the Sphere
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube(self, a_cube):
    # Get verticies of cube.
    verticies = []
    deltas = [(.5, -.5, -.5), 
             (.5, .5, -.5), 
             (.5, .5, .5),
             (.5, -.5, .5),
             (-.5, -.5, -.5),
             (-.5, .5, -.5),
             (-.5, .5, .5),
             (-.5, -.5, .5)]

    for delta in deltas:
        verticies.append(Point(a_cube.center.x + (delta[0] * a_cube.side), a_cube.center.y + (delta[1] * a_cube.side), a_cube.center.z + (delta[2] * a_cube.side)))
    
    # Check if all verticies are in sphere. 
    for i in range(8):
        if self.center.distance(verticies[i]) > self.r:
            return False
    return True

  # determine if a Cylinder is strictly inside this Sphere
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cyl(self, a_cyl):
    # 1. Check if rectangle projection verticies are within sphere's circle projection (y-z plane).
    # Get verticies.
    verticies = []
    # y,z change (collapsing onto y-z plane to get rectange)
    deltas = [(1, .5),(1, -.5),(-1, .5),(-1, -.5)]
    for delta in deltas:
        pair = (a_cyl.center.y + a_cyl.r * delta[0], a_cyl.center.z + a_cyl.h * delta[1])
        if (pair[0]**2 + pair[1]**2) >= self.r**2:
            return False

    # 2. Check if cylinder's circle projection is within sphere's circle projection (x-y plane).
    distance_between_centers = self.center.xy_distance(a_cyl.center) # Maybe make new distance method in point.
    if distance_between_centers + a_cyl.r >= self.r:
        return False

    return True


  # determine if another Sphere intersects this Sphere
  # other is a Sphere object
  # two spheres intersect if they are not strictly inside
  # or not strictly outside each other
  # returns a Boolean
  def does_intersect_sphere(self, other):
      # Check if sphere is strictly outside.
      sphere_outside = self.r + other.r < self.center.distance(other.center)
      return not self.is_inside_sphere(other) and not sphere_outside

  # determine if a Cube intersects this Sphere
  # the Cube and Sphere intersect if they are not
  # strictly inside or not strictly outside the other
  # a_cube is a Cube object
  # returns a Boolean
  def does_intersect_cube(self, a_cube):
      # Check if cube is strictly outside. # FIXME: Maybe change OG fucntion so not repetative.
    verticies = []
    cube_outside = True
    deltas = [(.5, -.5, -.5), 
             (.5, .5, -.5), 
             (.5, .5, .5),
             (.5, -.5, .5),
             (-.5, -.5, -.5),
             (-.5, .5, -.5),
             (-.5, .5, .5),
             (-.5, -.5, .5)]

    for delta in deltas:
        verticies.append(Point(a_cube.center.x + (delta[0] * a_cube.side), a_cube.center.y + (delta[1] * a_cube.side), a_cube.center.z + (delta[2] * a_cube.side)))
    
    # Check if all verticies are in sphere. 
    for i in range(8):
        if self.center.distance(verticies[i]) <= self.r:
            cube_outside = False
    
    return not self.is_inside_cube(a_cube) and not cube_outside

  # return the largest Cube object that is circumscribed
  # by this Sphere
  # all eight corners of the Cube are on the Sphere
  # returns a Cube object
  def circumscribe_cube(self):
      return Cube(self.center.x, self.center.y, self.center.z, math.sqrt(2) * self.r)


  

class Cube (object):
  # Cube is defined by its center (which is a Point object)
  # and side. The faces of the Cube are parallel to x-y, y-z,
  # and x-z planes.
  def __init__(self, x = 0, y = 0, z = 0, side = 1):
      self.center = Point(x, y, z)
      self.side = side

  # string representation of a Cube of the form: 
  # Center: (x, y, z), Side: value
  def __str__(self):
      return 'Center: ({}, {}, {}), Side: {}'.format(self.center.x, self.center.y, self.center.z, self.side)

  # compute the total surface area of Cube (all 6 sides)
  # returns a floating point number
  def area(self):
      return (self.side**2) * 6

  # compute volume of a Cube
  # returns a floating point number
  def volume(self):
      return self.side**3

  # determines if a Point is strictly inside this Cube
  # p is a point object
  # returns a Boolean
  def is_inside_point(self, p):
        vertices = get_vertices(self)
        maxi_x = vertices[0].x
        mini_x = vertices[0].x
        maxi_y = vertices[0].y
        mini_y = vertices[0].y
        maxi_z = vertices[0].z
        mini_z = vertices[0].z
        for tupl in vertices:
                if tupl.x > maxi_x:
                    maxi_x = tupl.x
                elif tupl.x < mini_x:
                    mini_x = tupl.x
                if tupl.y > maxi_y:
                    maxi_y = tupl.y
                elif tupl.y < mini_y:
                    mini_y = tupl.y
                if tupl.z > maxi_z:
                    maxi_z = tupl.z
                elif tupl.z < mini_z:
                    mini_z = tupl.z
        return (mini_x < p.x < maxi_x) and (mini_y < p.y < maxi_y) and (mini_z < p.z < maxi_z)
        

  # determine if a Sphere is strictly inside this Cube 
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere(self, a_sphere):
        radius = a_sphere.r
        center = a_sphere.center
        deltas = [[0, 0, 1], 
                [0, 1, 0], 
                [0, 0, -1], 
                [0, -1, 0], 
                [-1, 0, 0], 
                [1, 0, 0]]
        points = []
        for delta in deltas:
            points.append(Point(a_sphere.center.x + (delta[0] * radius), a_sphere.center.y + (delta[1] * radius), a_sphere.center.z + (delta[2] * radius)))
        
        for point in points:
            if not self.is_inside_point(point):
                return False
        return True


  # determine if another Cube is strictly inside this Cube
  # other is a Cube object
  # returns a Boolean
  def is_inside_cube(self, other):
        # vertices_A = get_vertices(self) Do we fucking need this shit?
        vertices_B = get_vertices(other)
        # Use max and min function on each vertice.
        #   maxi_A, mini_A = get_max_min(vertices_A) Do we even fucking need this?

        # return true if they ya
        for vertice in vertices_B:
            if not self.is_inside_point(vertice):
                return False
        return True
      

  # determine if a Cylinder is strictly inside this Cube
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cylinder(self, a_cyl):
        # These are for getting the top 4 points.
        deltas = [[1, 0, .5],
                [0, 1, .5],
                [-1, 0, .5],
                [0, -1, .5]]
        cyl_points = []
        for delta in deltas:
            coord_x = a_cyl.center.x + (delta[0] * a_cyl.r)
            coord_y = a_cyl.center.y + (delta[1] * a_cyl.r)
            coord_z = a_cyl.center.z + (delta[2] * a_cyl.h)
            cyl_points.append(Point(coord_x, coord_y, coord_z))
            cyl_points.append(Point(coord_x, coord_y, coord_z - a_cyl.h))

        for point in cyl_points:
            if not self.is_inside_point(point):
                return False
        return True

        
  # determine if another Cube intersects this Cube
  # two Cube objects intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cube object
  # returns a Boolean
  def does_intersect_cube(self, other):
        #Figure out if all points are outside.
        vertices_B = get_vertices(other)
        points_outside = True
        for vertice in vertices_B:
            if self.is_inside_point(vertice):
                points_outside = False
        return not (points_outside) and not self.is_inside_cube(other)


  # determine the volume of intersection if this Cube 
  # intersects with another Cube
  # other is a Cube object
  # returns a floating point number
  def intersection_volume(self, other):
        if self.does_intersect_cube(other):
            vertices_A = get_vertices(self)
            vertices_B = get_vertices(other)
            maxi_A, mini_A = get_max_min(vertices_A)
            maxi_B, mini_B = get_max_min(vertices_B)
            intersect_dim = []
            total_side = self.side + other.side

            for i in range(3):
                if maxi_A[i] > maxi_B[i]:
                    higher_max = maxi_A[i]
                    lower_max = maxi_B[i]
                else:
                    higher_max = maxi_B[i]
                    lower_max = maxi_B[i]
                
                if mini_A[i] > mini_B[i]:
                    higher_min = mini_A[i]
                    lower_min = mini_B[i]
                else:
                    higher_mini = mini_B[i]
                    lower_mini = mini_B[i]
                difference = total_side - abs(higher_max - lower_mini)
                intersect_dim.append(difference)

            x_y_area = intersect_dim[0] * intersect_dim[1]
            area_of_intersection = x_y_area * intersect_dim[2]
            return area_of_intersection
        else:
            return 0


  # return the largest Sphere object that is inscribed
  # by this Cube
  # Sphere object is inside the Cube and the faces of the
  # Cube are tangential planes of the Sphere
  # returns a Sphere object
  def inscribe_sphere(self):
        inscribed_sphere = Sphere(self.center.x, self.center.y, self.center.z, 0.5 * self.side)
        return inscribed_sphere


class Cylinder(object):
  # Cylinder is defined by its center (which is a Point object),
  # radius and height. The main axis of the Cylinder is along the
  # z-axis and height is measured along this axis
  def __init__(self, x = 0, y = 0, z = 0, radius = 1, height = 1):
      self.center = Point(x, y, z)
      self.r = radius 
      self.h = height

  # returns a string representation of a Cylinder of the form: 
  # Center: (x, y, z), Radius: value, Height: value
  def __str__(self):
      return 'Center: ({}, {}, {}), Radius: {}, Height: {}'.format(self.center.x, self.center.y, self.center.z, self.r, self.h)

  # compute surface area of Cylinder
  # returns a floating point number
  def area(self):
      return (2 * math.pi * self.r * self.h) + 2 * math.pi * self.r**2

  # compute volume of a Cylinder
  # returns a floating point number
  def volume(self):
      return math.pi * self.h * self.r**2

  # determine if a Point is strictly inside this Cylinder
  # p is a Point object
  # returns a Boolean
  def is_inside_point(self, p):
      radius = self.r
      height = self.h
      maxi_z = self.center.z + height
      mini_z = self.center.z - height
      return (p.x ** 2 + p.y ** 2 < radius ** 2) and (mini_z < p.z < maxi_z)
    

  # determine if a Sphere is strictly inside this Cylinder
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere(self, a_sphere):
      height = self.h
      maxi_z = self.center.z + height
      mini_z = self.center.z - height
      sphere_max_z = a_sphere.center.z + a_sphere.r
      sphere_min_z = a_sphere.center.z - a_sphere.r


      distance_between_centers = self.center.xy_distance(a_sphere.center)
      return (abs(distance_between_centers) + a_sphere.r < self.r) and (mini_z < sphere_min_z < maxi_z) and (mini_z < sphere_max_z < maxi_z)

  # determine if a Cube is strictly inside this Cylinder
  # determine if all eight corners of the Cube are inside
  # the Cylinder
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube(self, a_cube):
        vertices = get_vertices(a_cube)
        for vertice in vertices:
            if not self.is_inside_point(vertice):
                return False
        return True
    
  # determine if another Cylinder is strictly inside this Cylinder
  # other is Cylinder object
  # returns a Boolean
  def is_inside_cylinder(self, other):
    distance_between_centers = self.center.xy_distance(other.center)
    is_inside_xy = distance_between_centers + other.r < self.r

    # Get max and min of self cyl and other cyl
    self_maxi_z = self.center.z + self.h
    self_mini_z = self.center.z - self.h
    other_max_z = other.center.z + other.h
    other_min_z = other.center.z - other.h

    is_inside_z = (self_mini_z < other_max_z < self_maxi_z) and (self_mini_z < other_min_z < self_maxi_z)

    return is_inside_xy and is_inside_z

  # determine if another Cylinder intersects this Cylinder
  # two Cylinder object intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cylinder object
  # returns a Boolean
  def does_intersect_cylinder(self, other):
      cyl_points = get_cyl_points(other)
      # Check if all points are outside 
      all_outside = True
      for point in cyl_points:
          if self.is_inside_point(point):
              all_outside = False


      # Returns true if all_outside false and is_inside_cyl false.
      return (not all_outside) and (not self.is_inside_cylinder(other))

def get_cyl_points(a_cyl):
    deltas = [[1, 0, .5],
                [0, 1, .5],
                [-1, 0, .5],
                [0, -1, .5]]
    cyl_points = []
    for delta in deltas:
        x_coord = a_cyl.center.x + (delta[0] * a_cyl.r)
        y_coord = a_cyl.center.y + (delta[1] * a_cyl.r)
        z_coord = a_cyl.center.z + (delta[2] * a_cyl.h)
        cyl_points.append(Point(x_coord, y_coord, z_coord))
        cyl_points.append(Point(x_coord, y_coord, z_coord - a_cyl.h))
    return cyl_points

def point_distance_difference(point_p, point_q):
    origin = Point(0,0,0)
    str_modify = ''
    if point_p.distance(origin) > point_q.distance(origin):
        str_modify = 'is'
    else:
        str_modify = 'is not'
    return f'Distance of Point p from the origin {str_modify} greater than the distance of Point q from the origin'


def get_vertices(a_cube):
    vertices = []
    deltas = [(.5, -.5, -.5), 
            (.5, .5, -.5), 
            (.5, .5, .5),
            (.5, -.5, .5),
            (-.5, -.5, -.5),
            (-.5, .5, -.5),
            (-.5, .5, .5),
            (-.5, -.5, .5)]
    for delta in deltas:
        vertices.append(Point(a_cube.center.x + (delta[0] * a_cube.side), a_cube.center.y + (delta[1] * a_cube.side), a_cube.center.z + (delta[2] * a_cube.side)))
    return vertices

def get_max_min(vertices):
    maxi = [vertices[0].x, vertices[0].y, vertices[0].y]
    mini= [vertices[0].x, vertices[0].z, vertices[0].z]
    
    for point in vertices:
        if point.x > maxi[0]:
            maxi[0] = point.x
        elif point.x < mini[0]:
            mini[0] = point.x
        if point.y > maxi[1]:
            maxi[1] = point.y
        elif point.y < mini[1]:
            mini[1] = point.y
        if point.z > maxi[2]:
            maxi[2] = point.z
        elif point.z < mini[2]:
            mini[2] = point.z
    return maxi, mini
        
    

def main():
  # read data from standard input
    p_input = input().split()
  # read the coordinates of the first Point p
    for i in range(len(p_input)):
        p_input[i] = float(p_input[i])

  # create a Point object
    point_p = Point(p_input[0], p_input[1], p_input[2])


  # read the coordinates of the second Point q
    q_input = input().split()
    for i in range(len(q_input)):
        q_input[i] = float(q_input[i])
  # create a Point object 
    point_q = Point(q_input[0], q_input[1], q_input[2])

  # read the coordinates of the center and radius of sphereA
    sphereA_input = input().split()
    for i in range(len(sphereA_input)):
        sphereA_input[i] = float(sphereA_input[i])
    

  # create a Sphere object 
    sphereA = Sphere(sphereA_input[0], sphereA_input[1], sphereA_input[2], sphereA_input[3])
  # read the coordinates of the center and radius of sphereB
    sphereB_input = input().split()
    for i in range(len(sphereB_input)):
        sphereB_input[i] = float(sphereB_input[i])

  # create a Sphere object
    sphereB = Sphere(sphereB_input[0], sphereB_input[1], sphereB_input[2], sphereB_input[3])

  # read the coordinates of the center and side of cubeA
    input_A = input().split()
    for i in range(len(input_A)):
        input_A[i] = float(input_A[i])

  # create a Cube object 
    cubeA = Cube(input_A[0], input_A[1], input_A[2], input_A[3])

  # read the coordinates of the center and side of cubeB
    input_B = input().split()
    for i in range(len(input_B)):
        input_B[i] = float(input_B[i])
  # create a Cube object 
    cubeB = Cube(input_B[0], input_B[1], input_B[2], input_B[3])
  # read the coordinates of the center, radius and height of cylA
    cylA_input = input().split()
    for i in range(len(cylA_input)):
        cylA_input[i] = float(cylA_input[i])

  # create a Cylinder object 
    cyl_A = Cylinder(cylA_input[0], cylA_input[1], cylA_input[2], cylA_input[3], cylA_input[4])

  # read the coordinates of the center, radius and height of cylB
    cylB_input = input().split()
    for i in range(len(cylB_input)):
        cylB_input[i] = float(cylB_input[i])

  # create a Cylinder object
    cyl_B = Cylinder(cylB_input[0], cylB_input[1], cylB_input[2], cylB_input[3], cylB_input[4])



  # print if the distance of p from the origin is greater 
  # than the distance of q from the origin
    print(point_distance_difference(point_p, point_q))
    print()



  # print if Point p is inside sphereA # THIS WORKS
    if sphereA.is_inside_point(point_p):
        print('Point p is inside sphereA')
    else:
        print('Point p is not inside sphereA')

  # print if sphereB is inside sphereA # THIS WORKS
    if sphereA.is_inside_sphere(sphereB):
        print('sphereB is inside sphereA')
    else:
        print('sphereB is not inside sphereA')

  # print if cubeA is inside sphereA # THIS WORKS
    if cubeA.is_inside_sphere(sphereA):
        print('cubeA is inside sphereA')
    else:
        print('cubaA is not inside sphereA')

  # print if cylA is inside sphereA **WORKS
    if sphereA.is_inside_cyl(cyl_A):
        print('cylA is inside sphereA')
    else:
        print('cylA is not inside sphereA')

  # print if sphereA intersects with sphereB **WORKS
    if sphereA.does_intersect_sphere(sphereB):
        print('sphereA does intersect sphereB')
    else:
        print('sphereA does not intersect with Sphere B')
    
  # print if cubeB intersects with sphereB ** WORKS
    if sphereB.does_intersect_cube(cubeB):
        print('cubeB does intersect sphereB')
    else:
        print('cubeB does not intersect sphereB')

  # print if the volume of the largest Cube that is circumscribed **WORKS
  # by sphereA is greater than the volume of cylA
    if sphereA.circumscribe_cube().volume() > cyl_A.volume():
        print('Volume of the largest Cube that is circumscribed by sphereA is greater than the volume of cylA')
    else:
        print('Volume of the largest Cube that is circumscribed by sphereA is not greater than the volume of cylA')
    print()

  # print if Point p is inside cubeA **not done, expect to not be inside.
    if cubeA.is_inside_point(point_p):
        print('Point p is inside cubeA')
    else:
        print('Point p is not inside cubeA')



  # print if sphereA is inside cubeA
    if cubeA.is_inside_sphere(sphereA):
        print('sphereA is inside cubeA')
    else:
        print('sphereA is not inside cubeA')


  # print if cubeB is inside cubeA
    if cubeA.is_inside_cube(cubeB):
        print('cubeB is inside cubeA')
    else:
        print('cubeB is not inside cubeA')

  # print if cylA is inside cubeA
    if cubeA.is_inside_cylinder(cyl_A):
        print('cylA is inside cubeA')
    else:
        print('cylA is not inside cubeA')
    
    
  # print if cubeA intersects with cubeB
    if cubeA.does_intersect_cube(cubeB):
        print('cubeA does intersect cubeB')
    else:
        print('cubeA does not intersect cubeB')



  # print if the intersection volume of cubeA and cubeB
  # is greater than the volume of sphereA
    if cubeA.intersection_volume(cubeB) > sphereA.volume():
        print('Intersection volume of cubeA and cubeB is greater than the volume of sphereA')
    else:
        print('Intersection volume of cubeA and cubeB is not greater than the volume of sphereA')

  # print if the surface area of the largest Sphere object inscribed 
  # by cubeA is greater than the surface area of cylA
    if cubeA.inscribe_sphere().area() > cyl_A.area():
        print('Surface area of the largest Sphere object inscribed by cubeA is greater than the surface area of cylA')
    else:
        print('Surface area of the largest Sphere object inscribed by cubeA is not greater than the surface area of cylA')
    print()

  # print if Point p is inside cylA
    if cyl_A.is_inside_point(point_p):
        print('Point p is inside cylA')
    else:
        print('Point p is not inside cylA')
    
  # print if sphereA is inside cylA
    if cyl_A.is_inside_sphere(sphereA):
        print('sphereA is inside cylA')
    else:
        print('sphereA is not inside cylA')


  # print if cubeA is inside cylA
    if cyl_A.is_inside_cube(cubeA):
        print('cubeA is inside cylA')
    else:
        print('cubeA is not inside cylA')
    

  # print if cylB is inside cylA
    if cyl_A.is_inside_cylinder(cyl_B):
        print('cylB is inside cylA')
    else:
        print('cylB is not inside cylA')

  # print if cylB intersects with cylA
    if cyl_A.does_intersect_cylinder(cyl_B):
        print('cylB does intersect cylA')
    else:
        print('cylB does not intersect cylA')

if __name__ == "__main__":
  main()