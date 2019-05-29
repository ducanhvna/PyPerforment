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
