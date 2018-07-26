from typing import Iterator


def fib(n: int) -> Iterator[int]:
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b


fib(1)  # Good
fib(1.0)  # Float is bad
fib("this wont work")  # String is also bad