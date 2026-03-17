

from person_class import Person,Employee

def test_Person_greet():
    person1=Person('ali',22)
    assert person1.greet()=="Hello, my name is ali, and I am 22 years old."
    
def test_Emp_greet():
    emp1=Employee('omar',32,'Tester',3000)
    assert emp1.greet()=="Hello, I'm omar, Tester, and I am 32 years old."    
    
def test_emp_display_info():
      emp1=Employee('omar',32,'Tester',3000)  
      assert emp1.display_info()=="omar works as a Tester and earns a salary of $3000."
      