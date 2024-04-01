from typing import Callable

def caching_fibonacci() -> Callable[[int], int]:
    cache = {}
    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache.keys():
            return cache[n]
        else:
            f = fibonacci(n - 1) + fibonacci(n - 2)
            cache[n] = f
            print(cache)
            return f
    return fibonacci

f = caching_fibonacci()
print(f(11))
print(f(9))
print(f(14))