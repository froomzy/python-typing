# Installing MyPy

I have chofsen to use [MyPy](http://mypy-lang.org/) for this. There is also the option of [Pyre](https://pyre-check.org/). They seem much of a much.

## Getting MyPy
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
examples/step01.py:12: error: Argument 1 to "fib" has incompatible type "float"; expected "int"
examples/step01.py:13: error: Argument 1 to "fib" has incompatible type "str"; expected "int"
```

So this is the basics of getting typing working with python. Useful, but there is more that we want to do.
