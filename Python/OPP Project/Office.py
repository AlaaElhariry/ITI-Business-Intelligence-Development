class Office:
    employeesNum = 0 
    
    def __init__(self, name):
        self.name = name
        self.employees = []
    
    def hire(self, employee):
        self.employees.append(employee)
        Office.employeesNum += 1
    
    def fire(self, empId):
        self.employees = [e for e in self.employees if e.id != empId]
        Office.employeesNum -= 1
    
    def get_all_employees(self):
        return self.employees
    
    def get_employee(self, empId):
        for emp in self.employees:
            if emp.id == empId:
                return emp
        return None
    
    def deduct(self, empId, deduction):
        emp = self.get_employee(empId)
        if emp:
            emp.salary -= deduction
    
    def reward(self, empId, reward):
        emp = self.get_employee(empId)
        if emp:
            emp.salary += reward
    
    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        travel_time = distance / velocity
        arrival_hour = moveHour + travel_time
        return arrival_hour > targetHour
    
    def check_lateness(self, empId, moveHour):
        emp = self.get_employee(empId)
        if emp and emp.car:
            is_late = self.calculate_lateness(
                9, moveHour, emp.distanceToWork, emp.car.velocity or 60
            )
            if is_late:
                self.deduct(empId, 10)
            else:
                self.reward(empId, 10)
    
    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum = num