import unittest

class Temperature:
    def __init__(self, kelvin=None, celsius=None, fahrenheit=None):
        values = [x for x in [kelvin, celsius, fahrenheit] if x]

        if len(values) < 1:
            raise ValueError('Need Argument')

        if len(values) > 1:
            raise ValueError('Only one argument')

        if celsius is not None:
            self.kelvin = celsius + 273.15
        
        elif fahrenheit is not None:
            self.kelvin = (fahrenheit - 32) * 5 / 9 + 273.15
        
        else:
            self.kelvin = kelvin

        if self.kelvin < 0:
            raise ValueError('Temperature in Kelvin cannot be negative')
    
    def __str__(self):
        return f'Temperature = {self.kelvin} Kelvins'

class PrelimSkillsExam(unittest.TestCase):
    def test_1(self):
        Temperature(29)

    def test_2(self):
        Temperature(10, 29, 99) #This will raise a ValueError which will be shown in the Terminal

    def test_3(self):
        Temperature(celsius = 29)
        print("The Kelvin is Equals to " + str(Temperature(celsius = 29).kelvin))
        print("This One Answered the 3rd if else statement \n")

    def test_4(self):
        Temperature(fahrenheit = 99)
        print("The Kelvin is Equals to " + str(Temperature(fahrenheit = 99).kelvin))
        print("This One Answered the 4th if else statement")

if __name__ == '__main__':
    unittest.main()