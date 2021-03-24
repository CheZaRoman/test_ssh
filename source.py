class UnAcceptedValueError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)

class Person:
    def __init__(self, name: str, age: str):
        if name.isdigit():
            raise UnAcceptedValueError('Name has nums')
        else:
            self.name = name

        if not age.isdigit():
            raise UnAcceptedValueError('age is not integer')
        else:
            self.age = int(age)

def input_func():
    name1 = input('Input name for first person: ')
    name2 = input('Input name for second person: ')
    age1 = input('Input age for first person: ')
    age2 = input('Input age for second person: ')
    return name1, name2, age1, age2

def create_two_persons(name1, name2, age1, age2):
    person = Person(name1, age1)
    person2 = Person(name2, age2)
    return person, person2

#name1,name2, age1, age2 = input_func()

def rec_func(name1,name2, age1, age2, ):
    while True:
        try:
            p1, p2 = create_two_persons(name1, name2, age1, age2)
            return p1, p2
        except UnAcceptedValueError:
            print('Incorrect')
            name1, name2, age1, age2 = input_func()
            rec_func(name1, name2, age1, age2)


#print(rec_func(name1, name2, age1, age2))

class UserContextManager:
    def __init__(self, name):
        self.name = name

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exit from context manager')


    def __enter__(self):
        print('Enter into context manager')
        return self

# user = UserContextManager()
# with UserContextManager(name="222") as user:
#     print('suite')
#     print('....')
#     print(100/0)
#     print(user.name)
#     print('....')
#     print('end suite')
#
# print('-----------------')
# with open('newfile.txt', 'x', encoding='utf-8') as g:
#     d = int(input())
#     print('1 / {} = {}'.format(d, 1 / d), file=g)

f = open('newfile.txt')
print(f.readlines())