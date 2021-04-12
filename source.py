class Notebook:
    def __init__(self, num):
        self.num = num
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.num:
            self.counter = self.counter + 1
            return self.counter
        else:
            raise StopIteration

n = Notebook(10)
# for i in n:
#     print(i)


def range_generator(value):
    counter = 0
    while value > 0:
        value -= 1
        counter += 1
        yield counter

r_gen = range_generator(5)
print(type(r_gen))
print(next(r_gen))
print(next(r_gen))
print(next(r_gen))
print(next(r_gen))
print(next(r_gen))
print(next(r_gen))


