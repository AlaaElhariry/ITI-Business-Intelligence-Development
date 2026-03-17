class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name}, and I am {self.age} years old."

class Employee(Person):
    def __init__(self, name, age, job_title, salary):
        super().__init__(name, age)
        self.job_title = job_title
        self.salary = salary

    def display_info(self):
        return f"{self.name} works as a {self.job_title} and earns a salary of ${self.salary}."

    def greet(self):
        return f"Hello, I'm {self.name}, {self.job_title}, and I am {self.age} years old."
