
print ('Hello World')
import time 
def cache(func):
    cache_value={}
    print(f"this is cache_value from cache {cache_value}")
    def wrapper(*args):
        if args in cache_value:
            return f"this is cache_value from wrapper {cache_value[args]}"
        result=func(*args)
        cache_value[args]=result
        print(f"this is cache_value from wrapper {cache_value[args]} after gettng result")
        return result
    return wrapper
    
@cache
def long_tim(a,b):
    time.sleep(5)
    return a+b

print(f"this is the actual call {long_tim(2,3)}")
print(f"this is the actual call 2 {long_tim(2,4)}")
print(f"this is the actual call 3 {long_tim(2,9)}")
