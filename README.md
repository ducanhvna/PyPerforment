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

### BenchMarking
Làm sao để biết đoạn thuật toán này của mình đã đủ nhanh, đoạn code này của mình chạy nhanh hơn đoạn code cũ, sử dụng hàm này sẽ tối ưu hơn hàm kia...bla bla. Đó là khi ta nói tới benchmark - đo đạc xem code ta viết chạy nhanh như thế nào, tắc nghẽn chỗ nào. Trong python có nhiều công cụ khác nhau để thực hiện việc đo đạc này và bài này sẽ giới thiếu tới một vài công cụ đó.



## reference

[bench marking in python](https://viblo.asia/p/benchmarking-trong-python-m68Z0R1M5kG)


[Pylint tutorial](https://www.youtube.com/watch?v=fFY5103p5-c)

[Python code quality](https://realpython.com/python-code-quality/)