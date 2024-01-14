class Dog:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def bark(self):
        print("bark")


class Beagle(Dog):
    def __init__(self, name, age, gender, is_hunter):
        super().__init__(name, age, gender)
        self.is_hunter = is_hunter

    def hunt(self):
        if self.is_hunter:
            print(f"{self.name} is hunting so good")
        else:
            print(f"{self.name} can not hunt now")



b1 = Beagle("jessi", 7, "girl", True)
b1.bark()
b1.hunt()