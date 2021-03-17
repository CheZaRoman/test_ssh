class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def update(self, **kwargs):
        if kwargs.get('name'):
            self.__name = kwargs['name']
        if kwargs.get('age'):
            self.__age = kwargs['age']

    def get_info(self):
        return "{}, age: {}".format(self.__name, self.__age)

class Note:

    def __init__(self):
        self.__note_list = list()

    def add(self, person):
        self.__note_list.append(person)

    def remove(self, index):
        if 0 <= index <= len(self.__note_list)-1:
            self.__note_list.remove(self.__note_list[index])

    def update(self, index, **kwargs):
        if 0 <= index <= len(self.__note_list)-1:
            person = self.__note_list[index]
            person.update(**kwargs)

    def get_info_note(self):
        result = list()
        for i in self.__note_list:
            result.append(i.get_info())
        return result


class EmployeeNote(Note):

    def nothing(self):
        return 0
n = Note()
e = EmployeeNote()
p1 = Person('Ivan', 24)
p2 = Person('Ivan1', 23)
p3 = Person('Ivan2', 25)
p4 = Person('Ivan3', 26)
print('Note')
n.add(p1)
n.add(p2)
n.add(p3)
n.add(p4)
print(n.get_info_note())

n.remove(2)
print(n.get_info_note())

n.update(1, name='Jon', age=15, surname='RRR')
print(n.get_info_note())
print('EmployeeNote')
e.add(p1)
e.add(p2)
e.add(p3)
e.add(p4)
print(e.get_info_note())

e.remove(2)
print(e.get_info_note())

e.update(1, name='Jon', age=15, surname='RRR')
print(e.get_info_note())


class Computer:
    def __init__(self, processor, motherboard, graphic_card):
        pass
