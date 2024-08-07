class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_name(self, name):
        self.name = name
        return self

    def get_name(self):
        print(self.name)

    def __str__(self):
        return f"Name - {self.name}, age - {self.age}"


class Cat(Animal):
    def mau(self):
        print('Mau-mau')


class Dog(Animal):
    def __init__(self, last_name, *args, **kwargs):
        # super(Dog, self).__init__(name, age)
        super().__init__(*args, **kwargs)
        self.last_name = last_name

    def gav(self):
        print('Gav-gav')


cat = Cat("Bob", 2)
print(cat)
cat.age = 1000000
print(cat)

# cat2 = Cat("Murka", 3).set_name('Bax')
# print(cat2)
# cat2.get_name()
# cat.mau()
# print(cat.name)
# cat.set_name("Bax")
# print(cat.name)

# dog = Dog("Johnson", "Bobik", 3)
# dog.gav()
# print(dog.name)
# print(dog.last_name)
