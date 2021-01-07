# DSA
## Status
[![Build Status](https://travis-ci.org/thisisshub/DSA.png)](https://travis-ci.org/thisisshub/DSA)
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

## Ugh, not another DSA repository but anyway. What the fork is this?
This repository is the implementation of the contents DSA self paced series by yours truly but in Python

## Aren't we supposed to learn DSA in say C++?
YOU SHOULD but we both know you can't write or don't want to write C++

## So, what's up with your code? Why should I look into it?

Yours truly has written code which is written in 1-2 or more than 2 methods which perform the exact same task

### So what's the difference between method 1 and 2?
Well, if you look closely, I mean really closely you could see the `timeit` module in `__main__` which shows the time taken by that particular function to run

```python

def method1(n: int) -> int:
    return len(str(n)) if n >= 0 else len(str(n)) - 1


def method2(n: int) -> int:
    import math

    return int(math.log10(n) + 1 if n > 0 else (1 if n == 0 else math.log10(-n) + 1))


if __name__ == "__main__":
    """
    from timeit import timeit
    print(timeit(lambda: method1(1234567890), number=10000)) # 0.0022839140001451597
    print(timeit(lambda: method2(1234567890), number=10000)) # 0.004222848001518287
    """
```

## So is the time taken by `timeit` reliable?
Fork no, but still for the best result I ran the methods 10 thousand times each. My machine is Asus-UX425JA with Fedora 33 on kernel 5.9 with several stackoverflow tabs and a spotify tab open when I ran each `timeit`