

from math import *

# Points class
class Points:
    def __init__(self, x, y):
        # ami aykhane constructor use korci ja x ar y assign kore
        self.x = x
        self.y = y

    def quadrant(self):
        # ay function bolbe point kon quadrant e ache
        if self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        else:
            return 4

    def distance_from_origin(self):
        # origin theke distance ber korar function
        return sqrt(self.x ** 2 + self.y ** 2)

    def distance(self, p):
        # dui point er distance ber korar jonno
        return sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2)

    def midpoint(self, p):
        # midpoint ber korar function
        return Points((self.x + p.x) / 2, (self.y + p.y) / 2)

    def reflect_x(self):
        # x-axis er upor reflect kora
        return Points(self.x, -self.y)

    def reflect_y(self):
        # y-axis er upor reflect kora
        return Points(-self.x, self.y)

    def slope(self, p):
        # ekta point theke arekta point er slope
        if self.x != p.x:
            return (self.y - p.y) / (self.x - p.x)
        else:
            print('x-axis er sathe perpendicular')

    def angle_with_x_axis(self):
        # x-axis er sathe angle
        if self.x != 0:
            return degrees(atan(self.y / self.x))
        else:
            return 0

    def translation(self, dx, dy):
        # point ke translate korar function
        return Points(self.x + dx, self.y + dy)

    def is_same(self, p):
        # dui point same kina check
        return self.x == p.x and self.y == p.y

    def is_colinear(self, p1, p2):
        # tin point ek line e ache kina check
        return self.slope(p1) == p1.slope(p2)

    def rotate(self, angle_degree):
        # point ke rotate korar function
        angle_rad = radians(angle_degree)
        x1 = self.x * cos(angle_rad) - self.y * sin(angle_rad)
        y1 = self.x * sin(angle_rad) + self.y * cos(angle_rad)
        return Points(x1, y1)

    def __repr__(self):
        # point ke string e represent korar jonno
        return f'({self.x},{self.y})'


# Vectors class
class Vectors:
    def __init__(self, x, y):
        # vector er constructor
        self.x = x
        self.y = y

    def magnitude(self):
        # vector er magnitude ber korar function
        return sqrt(self.x ** 2 + self.y ** 2)

    def x_axis_angle(self):
        # x-axis er sathe vector er angle
        return degrees(atan2(self.y, self.x))

    def add(self, other):
        # dui vector jog korar function
        return Vectors(self.x + other.x, self.y + other.y)

    def subtract(self, other):
        # dui vector minus korar function
        return Vectors(self.x - other.x, self.y - other.y)

    def scale(self, k):
        # vector ke scalar diye multiply korar function
        return Vectors(k * self.x, k * self.y)

    def dot_product(self, other):
        # dot product ber korar function
        return self.x * other.x + self.y * other.y

    def cross_product(self, other):
        # cross product (2D scalar form)
        return self.x * other.y - self.y * other.x

    def angle_btwn(self, other):
        # dui vector er moddhe angle
        dot = self.dot_product(other)
        mag1 = self.magnitude()
        mag2 = other.magnitude()
        if mag1 == 0 or mag2 == 0:
            return None
        return degrees(acos(dot / (mag1 * mag2)))

    def is_parallel(self, other):
        # vector duita parallel kina
        return self.cross_product(other) == 0

    def is_perpendicular(self, other):
        # vector duita perpendicular kina
        return self.dot_product(other) == 0

    def __repr__(self):
        return f'<{self.x}, {self.y}>'


# Straight Line class
class Line2D:
    def __init__(self, A, B, C):
        # ami aykhane line er constructor use korci
        self.A = A
        self.B = B
        self.C = C

    def line_slope(self):
        # line er slope ber korar function
        try:
            return -self.A / self.B
        except ZeroDivisionError:
            print('line ta vertical')
            return None

    def y_intercept(self):
        # line er y-intercept ber korar function
        try:
            return -self.C / self.B
        except ZeroDivisionError:
            print('line y-axis ke cut kore na')
            return None

    def is_parallel(self, other):
        # dui line parallel kina check
        return self.line_slope() == other.line_slope() and self.y_intercept() != other.y_intercept()

    def is_perpendicular(self, other):
        # dui line perpendicular kina check
        m1 = self.line_slope()
        m2 = other.line_slope()
        return m1 * m2 == -1

    def angle_betwn(self, other):
        # dui line er moddhe angle
        m1 = self.line_slope()
        m2 = other.line_slope()
        if self.is_perpendicular(other):
            return 90
        return degrees(atan(abs((m1 - m2) / (1 + m1 * m2))))

    def distance_from_point(self, x0, y0):
        # ekta point theke line er distance
        numerator = abs(self.A * x0 + self.B * y0 + self.C)
        denominator = sqrt(self.A ** 2 + self.B ** 2)
        return numerator / denominator

    def is_colinear(self, other):
        # dui line colinear kina
        return self.is_parallel(other) and self.y_intercept() == other.y_intercept()

    def intersection_point(self, other):
        # dui line er intersection point
        if self.is_parallel(other):
            return None
        D = self.A * other.B - self.B * other.A
        Dx = self.B * other.C - other.B * self.C
        Dy = other.A * self.C - self.A * other.C
        return (Dx / D, Dy / D)

    def __repr__(self):
        return f"{self.A}x + {self.B}y + {self.C} = 0"


# test part
if __name__ == '__main__':
    # Points test
    p1 = Points(2, 3)
    p2 = Points(4, 5)
    print('p1 quadrant:', p1.quadrant())
    print('p1 distance from origin:', p1.distance_from_origin())
    print('distance between p1 and p2:', p1.distance(p2))
    print('midpoint:', p1.midpoint(p2))
    print('reflect x:', p1.reflect_x())
    print('reflect y:', p1.reflect_y())

    # Vectors test
    v1 = Vectors(3, 4)
    v2 = Vectors(1, 2)
    print('v1 magnitude:', v1.magnitude())
    print('v1 angle with x-axis:', v1.x_axis_angle())
    print('v1 + v2:', v1.add(v2))
    print('v1 - v2:', v1.subtract(v2))
    print('v1 dot v2:', v1.dot_product(v2))
    print('v1 cross v2:', v1.cross_product(v2))
    print('angle between v1 and v2:', v1.angle_btwn(v2))
    print('v1 parallel v2:', v1.is_parallel(v2))
    print('v1 perpendicular v2:', v1.is_perpendicular(v2))

    # Line test
    l1 = Line2D(1, -1, -2)
    l2 = Line2D(2, 1, -4)
    print('l1:', l1)
    print('l1 slope:', l1.line_slope())
    print('l1 y-intercept:', l1.y_intercept())
    print('l1 parallel l2:', l1.is_parallel(l2))
    print('l1 perpendicular l2:', l1.is_perpendicular(l2))
    print('angle between l1 and l2:', l1.angle_betwn(l2))
    print('distance from point (3,4) to l1:', l1.distance_from_point(3, 4))
    print('intersection point of l1 and l2:', l1.intersection_point(l2))
