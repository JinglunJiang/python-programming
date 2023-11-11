import math
from abc import ABC, abstractmethod
from PIL import Image


class Drawable(ABC):
    @abstractmethod
    def __contains__(self, point):
        """
        An abstract method for later use
        """
        pass

    def __and__(self, other):
        """
        In order to use and operator
        """
        return Intersection(self, other)

    def __or__(self, other):
        """
        In order to use the or operator
        """
        return Union(self, other)

    def __sub__(self, other):
        """
        To find the difference
        """
        return Difference(self, other)

    def draw(self, img):
        """
        A drawing method that color the pixel in the self object
        Input: the Drawable object, an image
        Output: None
        """
        for x in range(img.width):
            for y in range(img.height):
                point = (x, y)
                if point in self:
                    img.putpixel((x, y), 0)


class Circle(Drawable):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def __contains__(self, point):
        """
        Override the contains method to find if the point is inside the circle
        Input: the object and another point
        Output: a boolean represent if the point is inside the circle
        """
        x, y = point
        distance = math.pow(math.pow(self.x - x, 2) +
                            math.pow(self.y - y, 2), 0.5)
        return distance < self.radius  # should not be < according to the testcases


class Rectangle(Drawable):
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

    def __contains__(self, point):
        """
        Overrides the contains method, to see if the point is inside the rectangle
        Input: the object and another point
        Output: a boolean represent if the point is inside the rectangle
        """
        x, y = point
        return x > self.x0 and x < self.x1 and y > self.y0 and y < self.y1


class Intersection(Drawable):
    def __init__(self, shape1, shape2):
        self.shape1 = shape1
        self.shape2 = shape2

    def __contains__(self, point):
        """
        Overrides the contains method to see if the point is inside both shapes
        Input: the object and a point
        Output: boolean represent if the point is in both shapes
        """
        return point in self.shape1 and point in self.shape2


class Union(Drawable):
    def __init__(self, shape1, shape2):
        self.shape1 = shape1
        self.shape2 = shape2

    def __contains__(self, point):
        """
        Overrides the contains method with union logic
        Input: the object and another point
        Output: a boolean true if the point is in either of the shapes
        """
        return point in self.shape1 or point in self.shape2


class Difference(Drawable):
    def __init__(self, shape1, shape2):
        self.shape1 = shape1
        self.shape2 = shape2

    def __contains__(self, point):
        """
        Overrides the contains method with difference logic
        Input: the object and another point
        Output: a boolean true if the point is in the first shape and not in the second
        """
        return point in self.shape1 and point not in self.shape2


def main():
    # You may modify this method as you see fit.
    # Remember to draw a happy face before submitting!

    # create a blank white image
    width = 500
    height = 500
    img = Image.new("RGB", (width, height), "white")

    # build a drawable here
    face = Circle(250, 250, 200) - Circle(250, 250, 195)
    left_eye = Circle(180, 180, 20)
    right_eye = Circle(320, 180, 20)
    mouth = Circle(250, 280, 100) - Circle(250, 275, 98)

    # draw drawables to img and then save to output.png
    face.draw(img)
    left_eye.draw(img)
    right_eye.draw(img)
    mouth.draw(img)
    img.save("output.png")


if __name__ == "__main__":
    main()
