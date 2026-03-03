#A decorator is a function that takes another function as an argument and extends its behavior without explicitly modifying it
import time

def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} seconds!")
        return result
    return wrapper
@timer
def some_fxn(n):
    time.sleep(n)
some_fxn(2)
