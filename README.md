# Đo performent cho python

## Pylint
Giống static code checking trong C++ (Parasoft)
### Trước khi check

```bash
class car:
    def __init__(self, color):
        self.color = color

my_car = car('Blue')
def crash(car1, car2):
    car1.color = 'burnt'
    
crash(car('red'), my_car)

```
### Sau khi check

```bash
class Car:
    """ This is test version for pylint
    """
    def __init__(self, color):
        """ Initialize
        """
        self.color = color

MY_CAR = Car('Blue')
def crash(car1, car2): #pylint: disable = unused-argument
    """ An example funtion
    """
    car1.color = 'burnt'

crash(Car('red'), MY_CAR)

```