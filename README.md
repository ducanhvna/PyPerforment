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

## BenchMarking
Làm sao để biết đoạn thuật toán này của mình đã đủ nhanh, đoạn code này của mình chạy nhanh hơn đoạn code cũ, sử dụng hàm này sẽ tối ưu hơn hàm kia...bla bla. Đó là khi ta nói tới benchmark - đo đạc xem code ta viết chạy nhanh như thế nào, tắc nghẽn chỗ nào. Trong python có nhiều công cụ khác nhau để thực hiện việc đo đạc này và bài này sẽ giới thiếu tới một vài công cụ đó.

### Module timeit
Python có một module có sẵn là timeit. Bạn có thể sử dụng nó để đo cho những đoạn mã nhỏ của mình. Module timeit sử dụng các chức năng thời gian dành riêng cho nền tảng để bạn có được thời gian chính xác nhất. Module timeit có giao diện dòng lệnh, nhưng cũng có thể import được

### Sử dụng decorator
Chúng ta có thể tự tạo một bộ đếm thời gian riêng từ những module sẵn có trong python, tuy độ chính xác không cao nhưng cũng sẽ rất thú vị

### Timing Context Manager
Nâng cao hơn cách số 2 là ta sẽ khai báo một class, còn phương pháp thì vẫn như vậy thôi. Chúng ta sử dụng thêm các method init để khởi tạo, enter để trả về chính nó và exit để tính toán, in ra thời gian đã sử dụng.

### Module cProfile
Python đi kèm với trình biên dịch đã tích hợp sẵn. Có module profile và cProfile. Module profile là thuần tùy để sử dụng nhưng nó tiêu tốn nhiều chi phí cho bất kỳ thứ gì bạn cấu hình, nên nó luôn được recommended sử dụng cProfile có các phương thức tương tự nhưng nhanh hơn nhiều

### Module line_profiler
Một module bên thứ 3, cài đặt qua pip như sau:

```bash
pip install line_profiler
```

### Module memory_profiler


### Module profilehooks

# Kết luận

# reference

[bench marking in python](https://viblo.asia/p/benchmarking-trong-python-m68Z0R1M5kG)


[Pylint tutorial](https://www.youtube.com/watch?v=fFY5103p5-c)

[Python code quality](https://realpython.com/python-code-quality/)