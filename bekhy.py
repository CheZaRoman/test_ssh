
class Human:
    list_person = []

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


    def convert_to_dict(self):
        return {"name": self.name, "surname": self.surname, "age": self.age}


    def check_and_add_to_list(self):
        duplicated = 0
        person_dict = self.convert_to_dict()
        for i in self.list_person:
            if i['name'] == person_dict.get('name') and i['surname'] == person_dict.get('surname') and i['age'] == person_dict.get('age'):
                duplicated += 1
        if not duplicated:
            Human.list_person.append(person_dict)


human1 = Human("Ivan", "Ivan", 32)
human2 = Human("Ivan", "Ivan", 32)
human3 = Human("Petr", "Petr", 24)
human4 = Human("Petr", "Petr", 24)
human5 = Human("Petr", "Petr", 24)

#
#

human1.check_and_add_to_list()
human2.check_and_add_to_list()
human3.check_and_add_to_list()
human4.check_and_add_to_list()
human5.check_and_add_to_list()
# human21.check_and_add_to_list()
# human3.check_and_add_to_list()
# human4.check_and_add_to_list()
# human5.check_and_add_to_list()
print(Human.list_person)



