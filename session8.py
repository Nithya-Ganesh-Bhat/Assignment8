#Q1

def some_function():
    """Summary or Description of the Function
    Parameters:
    argument1 (int): Description of arg1
    Returns:
    int:Returning value
    """

def doc_string_outer():
    char_len = 50
    def doc_string_inner(func):
        length = len(func.__doc__) > char_len
        return length
    return doc_string_inner

fn = doc_string_outer()
fn(some_function)

#Q2

def fibo_outer(num):
    def fibo_inner():
        nonlocal num
        number1 = 0
        number2 = 1
        nextFibo = number1 + number2
        while nextFibo <= num:
            number1 = number2
            number2 = nextFibo
            nextFibo = number1+number2
        num = nextFibo
        return num
    return fibo_inner

fn = fibo_outer(3)
fn()

#Q3

counters = dict()
counters['add'] = 0
counters['mul'] = 0
counters['div'] = 0

def counter(fn):
    cnt = 0
    global counters
    def inner(*args,**kwargs):
        nonlocal cnt
        cnt += 1
        print('{0} has been called {1} times'.format(fn.__name__,cnt))
        counters[fn.__name__] = cnt
        return fn(*args, **kwargs)
    return inner

def add(a,b):
    return a+b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

counter_mult = counter(mul)
counter_mult(3,4)
counter_mult(5,6)
counter_mult(7,8)
counter_mult(8,9)
counter_mult(1,2)

counter_add = counter(add)
counter_add(5,10)
counter_add(2,3)

counter_div = counter(div)
counter_div(10,2)
counter_div(6,3)
counter_div(6,3)

counters

#Q4

def counter_dict(times_dict):
    """ This function can keep a track of how many times add/mul/div functions were called,
    and update a dictionary , specific to a user, with the counts"""
    def inner(fn,*args, **kwargs):
        nonlocal times_dict
        times_dict[fn.__name__] += 1
        print('{0} has been called {1} times'.format(fn.__name__, times_dict[fn.__name__]))
        print(times_dict)
        return fn(*args, **kwargs)
    return inner
