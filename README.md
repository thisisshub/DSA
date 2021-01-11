# DSA
## Status
![Travis (.org)](https://img.shields.io/travis/thisisshub/DSA?style=flat-square)
![Codacy grade](https://img.shields.io/codacy/grade/28b16c91194349b4baa13779c57de794?style=flat-square)
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg?logo=paypal&style=flat-square)](https://www.paypal.com/paypalme/thisisshub/100)&nbsp;
![GitHub repo size](https://img.shields.io/github/repo-size/thisisshub/DSA?style=flat-square)
![Lines of code](https://img.shields.io/tokei/lines/github/thisisshub/DSA?style=flat-square)
![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/thisisshub/DSA?style=flat-square)
![GitHub issues](https://img.shields.io/github/issues/thisisshub/DSA?style=flat-square)    
![GitHub forks](https://img.shields.io/github/forks/thisisshub/DSA?style=flat-square)
![GitHub Repo stars](https://img.shields.io/github/stars/thisisshub/DSA?style=flat-square)
![GitHub watchers](https://img.shields.io/github/watchers/thisisshub/DSA?style=flat-square)


## Ugh, not another DSA repository but anyway. What the fork is this?
This repository is the implementation of the contents DSA self paced series by yours truly but in Python

## Aren't we supposed to learn DSA in say C++?
YOU SHOULD but we both know you won't or can't write C++

## So, what's up with your code? Why should I look into it?

Yours truly for each topic he came across has written the code in 1-2 or more than 2 methods which perform the exact same task. So that you could choose whichever method works for you. Each method is tested under the `tests/` with pytest

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


## TODO:
- [ ] Add problems section just like in series
- [ ] Write missing tests