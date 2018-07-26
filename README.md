# Installing MyPy

I have chofsen to use [MyPy](http://mypy-lang.org/) for this. There is also the option of [Pyre](https://pyre-check.org/). They seem much of a much.

## Getting MyPy
This is best done with python3.6 or greater.
```
virtualenv .venv
. ./.venv/bin/activate
pip install mypy
```
From here on in it is assumed that you will be running in the virtualenv.
This should be enough for you to run mypy.
```
mypy --version
```
You should see the version show up, which means your good to go.

## Getting some simple examples going

Create a file, step01.py, in the src folder. Include the following code (borrowed from MyPy website)
```python
def fib(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b
```
Save it, and lets see if we can run mypy over it.

```
mypy src/step01.py
```
And it runs, and nothing happens. Oh well, lets actually add some typing stuff.

```python
from typing import Iterator

def fib(n: Int) -> Iterator[int]:
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b
```
Run mypy again, and still nothing seems to happen. Lets do something silly with it. Add the following to the bottom of the step01.py

```python
fib(1)  # Good
fib(1.0)  # Float is bad
fib("this wont work")  # String is also bad
```
Once more to mypy. You should get a couple of errors now.
```
src/step01.py:12: error: Argument 1 to "fib" has incompatible type "float"; expected "int"
src/step01.py:13: error: Argument 1 to "fib" has incompatible type "str"; expected "int"
```

So this is the basics of getting typing working with python. Useful, but there is more that we want to do.

Lets try a couple of other things.
Add the following to step01.py
```python
from typing import Iterator, List


def convert_string(string: str) -> str:
    if string:
        return string * 5


def load_file(file_name: str) -> List[str]:
    results = []
    with open(file_name) as f:
        for line in f.readlines():
            results.append(convert_string(string=line))
    return results


results = load_file('lines.txt')
```
If you run mypy now, you will get a useful error
```
src/step01.py:11: error: Missing return statement
```
This is telling us that our code doesn't actually meet its contract. There are situations that don't return a string. So lets fix that.
Update step01.py to be like this
```python
def convert_string(string: str) -> str:
    if string:
        return string * 5
    return ''
```
But what if we don't want to return a string in this case? We could do something like the following
```python
from typing import Iterator, List, Optional


def convert_string(string: str) -> Optional[str]:
    if string:
        return string * 5
    return None
```
```
src/step01.py:22: error: Incompatible return value type (got "List[Optional[str]]", expected "List[str]")
```
This tells mypy that the return can be potentially a string or None. This fixes our initial issue, but makes new ones. Because our
contract changed, there are flow on effects where those that are expecting the result to be of a particular type need to be updated
to handle that change.

```python
def load_file(file_name: str) -> List[str]:
    results = []
    with open(file_name) as f:
        for line in f.readlines():
            string = convert_string(string=line)
            if string is not None:
                results.append(string)
    return results
```
We now handle the none case, and everyone is happy. But this shows why the typing stuff can be really helpful.

Next up, we are going to look at getting this to run with Django, because that is of value to us. But first, for more details on actually
using this stuff in the real world, see this [talk by Carl Meyer](https://www.youtube.com/watch?v=pMgmKJyWKn8). Its a good, quick, talk about some of the things that you can do with typing.