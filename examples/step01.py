from typing import Iterator, List, Optional


def fib(n: int) -> Iterator[int]:
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b


def convert_string(string: str) -> Optional[str]:
    if string:
        return string * 5
    return None


def load_file(file_name: str) -> List[str]:
    results = []
    with open(file_name) as f:
        for line in f.readlines():
            string = convert_string(string=line)
            if string is not None:
                results.append(string)
    return results


results = load_file('lines.txt')

fib(1)  # Good
fib(1.0)  # Float is bad
fib("this wont work")  # String is also bad