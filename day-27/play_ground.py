def add(*args):
    return sum(args)


# print(add(1, 2, 3, 4, 5, 6))

def calculate(n, **kwargs):
    for m in kwargs.get('multiply', []): n *= m
    for d in kwargs.get('divide', []): n /= d
    for a in kwargs.get('add', []): n += a
    for s in kwargs.get('subtract', []): n -= s


    print(n)


calculate(2, add=[3], multiply=[5, 6, 7])

class Car:
    def __init__(self, **kw):
        self.make = kw['make']
        self.mode = kw['model']

myCar = Car(make='nissan', model='gtr')