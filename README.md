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
#### Danh sách warning
```bash
************* Module example
example.py:8:0: C0303: Trailing whitespace (trailing-whitespace)
example.py:9:0: C0304: Final newline missing (missing-final-newline)
example.py:1:0: C0111: Missing module docstring (missing-docstring)
example.py:1:0: C0103: Class name "car" doesn't conform to PascalCase naming style
(invalid-name)
example.py:1:0: C0111: Missing class docstring (missing-docstring)
example.py:1:0: R0903: Too few public methods (0/2) (too-few-public-methods)
example.py:5:0: C0103: Constant name "my_car" doesn't conform to UPPER_CASE naming
style (invalid-name)
example.py:6:0: C0111: Missing function docstring (missing-docstring)
example.py:6:16: W0613: Unused argument 'car2' (unused-argument)
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