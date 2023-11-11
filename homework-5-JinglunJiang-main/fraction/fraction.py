import math


class Fraction:
    def __init__(self, numerator, denominator):
        """
        Initiate a new Fraction instance
        Input: the object itself, the numerator and denominator of the fraction
        Output: the simplest form of the fraction
        """
        # this ensures the denominator cannot be zero
        if denominator == 0:
            raise ZeroDivisionError()
        # TODO: finish implementing this function
        gcd = math.gcd(numerator, denominator)
        # new numerator and denominator should be divided by the greatest common divisor
        self._numerator = (numerator // gcd)  # only the int type is needed
        self._denominator = (denominator // gcd)

    @property
    def numerator(self):
        """
        The getter of the numerator, setter not needed
        Input: the fraction object
        Output: the numerator of the fraction
        """
        return self._numerator

    @property
    def denominator(self):
        """
        The getter of the denominator, setter not needed
        Input: the fraction object
        Output: the denominator of the fraction
        """
        return self._denominator

    def __eq__(self, other):
        """
        Function to compare two numbers(Integer or Fraction)
        Input: The fraction object itself, another number either integer or fraction as well
        Output: If the two numbers have the same value
        """
        if type(other) == int:
            other = Fraction(other, 1)  # Change the type to fraction if not
        return (self.numerator == other.numerator) and (self.denominator == other.denominator)

    def __neg__(self):
        """
        Method to negate the fraction
        Input: only the fraction itself
        Output: The reverse value of the fraction
        """
        return Fraction(-self.numerator, self.denominator)

    def __repr__(self):
        """
        Repr method for checking the fraction
        Input: The fraction itself only
        Output: A string of the information of the fraction
        """
        return f"Fraction({self.numerator}, {self.denominator})"

    def __add__(self, other):
        """
        Add method add two numbers together
        Input: the fraction itself and another number
        Output: a Fraction that is the sum of the two numbers
        """
        if type(other) == int:
            other = Fraction(other, 1)  # Same as above
        new_denominator = self.denominator * other.denominator
        new_numerator = self.numerator * other.denominator + \
            other.numerator * self.denominator
        return Fraction(new_numerator, new_denominator)

    def __radd__(self, other):
        """
        Reverse adding method to handle the cases when the object is on the right hand side
        Input: the fraction itself and another number
        Output: Calling the normal adding method
        """
        return self.__add__(other)

    def __sub__(self, other):
        """
        Subtraction method
        Input: the Fraction itself, and another number to be subtracted
        Output: a Fraction after subtracting the other from the object
        """
        if type(other) == int:
            other = Fraction(other, 1)
        new_denominator = self.denominator * other.denominator
        new_numerator = self.numerator * other.denominator - \
            other.numerator * self.denominator
        return Fraction(new_numerator, new_denominator)

    def __rsub__(self, other):
        """
        Reverse method to handle subtraction if the self object need to be subtracted
        Input: the two numbers
        Output: return the reverse use of the subtraction method
        """
        # Necessary to turn the other into fraction first
        return Fraction(other, 1).__sub__(self)

    def __mul__(self, other):
        """
        Multiplication method
        Input: the two numbers
        Output: A fraction after multiplication calculation
        """
        if type(other) == int:
            other = Fraction(other, 1)
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __rmul__(self, other):
        """
        Reverse method used to handle the cases when self is on the right hand side
        Input: the two numbers (self and another number)
        Output: the same as the not reversed multiplication
        """
        return self.__mul__(other)

    def __truediv__(self, other):
        """
        Division method
        Input: the object itself and another number as divisor
        Output: A fraction after division calculation
        """
        if other == 0:
            raise ZeroDivisionError()  # handle the case when the other number is 0
        if type(other) == int:
            other = Fraction(other, 1)
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __rtruediv__(self, other):
        """
        A reverse division method to reverse the input of the above function
        Input: the object itself, and another number
        Output: A fraction after calculation
        """
        if self.numerator == 0:  # Consider when the object itself is 0
            raise ZeroDivisionError()
        return Fraction(other, 1).__truediv__(self)
