# Example of Classes
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def method(self):
        print("Hi, My Name is:" + self.name)


h1 = Human("Pratiksha", 23)
h1.method()

h1.name = "Shree"
h1.age = 26

h1.method()
