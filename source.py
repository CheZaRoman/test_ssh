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

    def add_person(self, person):
        self.__note_list.append(person)

    def remove_person(self, index):
        if 0 <= index <= len(self.__note_list)-1:
            self.__note_list.remove(self.__note_list[index])

    def update_person(self, index, **kwargs):
        if 0 <= index <= len(self.__note_list)-1:
            person = self.__note_list[index]
            person.update(**kwargs)

    def get_info_note(self):
        result = list()
        for i in self.__note_list:
            result.append(i.get_info())
        return result

n = Note()
p1 = Person('Ivan', 24)
p2 = Person('Ivan1', 23)
p3 = Person('Ivan2', 25)
p4 = Person('Ivan3', 26)
n.add_person(p1)
n.add_person(p2)
n.add_person(p3)
n.add_person(p4)
print(n.get_info_note())

n.remove_person(2)
print(n.get_info_note())

n.update_person(1, name='Jon', age=15, surname='RRR')
print(n.get_info_note())