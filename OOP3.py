class Person:
    def __init__(self, name, surname, age, *args, **kwargs):
        self.name = name
        self.surname = surname
        self.age = age

    def display_info(self):
        print("Name: {}\n Surname: {}\n Age: {}".format(self.name,
                                                        self.surname,
                                                        self.age))

    @property
    def name1(self):
        return self.name

    def __str__(self):
        return "Имя: {} \t Возраст: {}".format(self.name, self.age)

class Employee(Person):

    def __init__(self, name, surname, age, company):
        Person.__init__(self, name, surname, age)
        self.company = company
        self.position = 'director'

    def display_info(self):
        Person.display_info(self)
        print("Company: {}".format(self.company))


# p = Person("Nick", "Test", 22)
# e = Employee("Nick2", "Test2", 55, "Work1")
# print(p)
# print(e)
#
# p.display_info()
# e.display_info()

# #
# print(isinstance(p, Person))
# print(isinstance(p, Employee))
# print(isinstance(e, Person))
# print(isinstance(e, Employee))

# print(p)
# print(e)

# class EmailError(Exception):
#     def __init__(self, data):
#         self.data = data
#
#     def __str__(self):
#         return self.data
#
#
# class User:
#     def __init__(self, username, email):
#         self.username = username
#         self.email = self.validate(email)
#
#     def validate(self, email):
#         if "@" and "." not in email:
#             raise EmailError("Invalid email")
#         return email
#
#
# u1 = User('username1', 'username1@mail.com')
# u2 = User('invalid', 'invalidmail')


def func(geojson):
    new_data = []
    if geojson.get('features'):
        for f in geojson['features']:
            geometry = f.get('geometry')
            new_feature = {
                geometry.get('type'): geometry.get('coordinates')
            }
            new_data.append(new_feature)
    return new_data

geojson = {
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              60.46875,
              56.75272287205736
            ],
            [
              38.3203125,
              42.5530802889558
            ],
            [
              71.015625,
              39.90973623453719
            ],
            [
              84.72656249999999,
              49.38237278700955
            ],
            [
              73.828125,
              54.97761367069628
            ],
            [
              60.46875,
              56.75272287205736
            ]
          ]
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              83.3203125,
              36.03133177633187
            ],
            [
              88.24218749999999,
              36.03133177633187
            ],
            [
              88.24218749999999,
              45.583289756006316
            ],
            [
              83.3203125,
              45.583289756006316
            ],
            [
              83.3203125,
              36.03133177633187
            ]
          ]
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              74.53125,
              55.97379820507658
            ],
            [
              82.6171875,
              55.97379820507658
            ],
            [
              82.6171875,
              60.06484046010452
            ],
            [
              74.53125,
              60.06484046010452
            ],
            [
              74.53125,
              55.97379820507658
            ]
          ]
        ]
      }
    }
  ]
}

print(func(geojson))