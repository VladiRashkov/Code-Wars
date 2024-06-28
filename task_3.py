class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @staticmethod
    def compare(p1, p2):
        return p1.age<p2.age



p1 = Person('Peter',15)
p2 = Person('Ivan', 23)
result = Person.compare(p1, p2)

print(result)
