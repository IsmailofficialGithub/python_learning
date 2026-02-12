print('create a timer decorator that print start and end time of function')
import time
def timer(function):
    def wrapper(*args,**kargs):
        start= time.time()
        result = function(*args,**kargs)
        end= time.time()
        print(f'Function {function.__name__} run is {start-end} time ')
        return result
    return wrapper

@timer
def example_fun(n):
    time.sleep(n)

example_fun(2)


           

    