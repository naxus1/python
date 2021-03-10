import unittest

class RomanToArabic:
    """This class changes an integer number
    to a roman number"""

    def __init__(self, n=1):
        """Initialize a number"""
        self.n = n

    def conver_integer_number(self, integer_number):
        """This method change an integer 
        number to roman number"""
        options = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C':100,
            'D': 500,
            'M': 1000
        }
        total, actual_roman_number = 0, options.get(integer_number[0])


        for number in integer_number:
            # iterate over str roman numbers
            if number in options.keys():
                # Is roman number exist in dictionary
                if options.get(number) <= actual_roman_number:
                    #Check that current number is less that actual_roman_number
                    total += options.get(number)
                else:
                    total += (options.get(number) - (2 * actual_roman_number))
                actual_roman_number = options.get(number)
        return abs(total)



class RomanNumberTest(unittest.TestCase):

    def setUp(self):
        self.roman_number = RomanToArabic()

    def test_one_to_arabic(self):
        arabic_number = self.roman_number.conver_integer_number('I')
        self.assertEqual = (1, arabic_number)

    def test_two_to_arabic(self):
        arabic_number = self.roman_number.conver_integer_number('II')
        self.assertEqual = (2, arabic_number)

    def test_three_to_arabic(self):
        arabic_number = self.roman_number.conver_integer_number('III')
        self.assertEqual = (3, arabic_number)

    def test_four_to_arabic(self):
        arabic_number = self.roman_number.conver_integer_number('IV')
        self.assertEqual = (4, arabic_number)

    def test_nine_to_arabic(self):
        arabic_number = self.roman_number.conver_integer_number('IX')
        self.assertEqual = (9, arabic_number)
    
    def test_nineteen_to_arabic(self):
        arabic_number = self.roman_number.conver_integer_number('XIX')
        self.assertEqual = (19, arabic_number)


if __name__ == '__main__':
    unittest.main()