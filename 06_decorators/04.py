import time
def cache_saver(func):
    cache_memory = {}
    def wrapper(*args):
        print(cache_memory)
        if args in cache_memory:
            return cache_memory[args]
        result = func(*args)
        cache_memory[args]=result
        return result
    return wrapper

@cache_saver
def big_func(num1,num2):
    time.sleep(2)
    return num1+num2

print(big_func(2,3))
print(big_func(2,3))