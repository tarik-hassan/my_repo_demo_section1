class Student:
    def __init__(self, fname, lname, id, energy_level = 10):
        self.fname = fname
        self.lname = lname
        self.id = id
        self.energy_level = energy_level
    
    def __str__(self):
        return f"{self.lname}: {self.id}"
    
    def greeting(self, fname, lname):
        print("Hello, my name is", fname, lname)
    
    def take_exam(self, energy_level):
        self.energy_level = energy_level - 1
    
    def get_energy_level(self):
        return self.energy_level

from student import Student

student1 = Student("Jon", "Urda", "123")
print(student1)