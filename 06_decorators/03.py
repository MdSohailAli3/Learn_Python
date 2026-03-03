# Problem: Implement a decorator that caches the return values of a 
# function, so that when it's called with the same arguments,
#  the cached value is returned instead of re-executing the function.
import time
def cache(func):
    cache_value={}
    print(cache_value)
    def wrapper(*args):
        print(args)
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper
@cache
def some_big_func(num1,num2):
    time.sleep(5)
    return num1+num2
print(some_big_func(2,3))
print(some_big_func(2,3))
print(some_big_func(4,3))
print(some_big_func(4,3))
