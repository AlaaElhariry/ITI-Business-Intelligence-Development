from Person import Person
from Employee import Employee
from Car import Car
from Office import Office


def main():
    # Create cars
    car1 = Car(name="BMW", fuelRate=80, velocity=60)
    car2 = Car(name="Toyota", fuelRate=50, velocity=70)

    # Create employees
    emp1 = Employee(
        name="Alaa",
        money=2000,
        id=1,
        email="alaa@gmail.com",
        salary=5000,
        distanceToWork=30,
        car=car1
    )

    emp2 = Employee(
        name="Ahmed",
        money=1500,
        id=2,
        email="ahmed@gmail.com",
        salary=4500,
        distanceToWork=20,
        car=car2
    )

    # Create office
    iti_office = Office("ITI Smart Village")

    # Hire employees
    iti_office.hire(emp1)
    iti_office.hire(emp2)

    print("Employees hired:", Office.employeesNum)
    print("-" * 40)

    # Employees go to work
    print("Alaa going to work:")
    emp1.drive(emp1.distanceToWork)

    print("\nAhmed going to work:")
    emp2.drive(emp2.distanceToWork)

    print("-" * 40)

    # Check lateness
    iti_office.check_lateness(empId=1, moveHour=8.5)
    iti_office.check_lateness(empId=2, moveHour=9.2)

    # Show final salaries
    print("\nFinal Salaries:")
    for emp in iti_office.get_all_employees():
        print(f"{emp.name}: {emp.salary} EGP")

    print("-" * 40)

    # Fire an employee
    iti_office.fire(1)
    print("Employees after firing:", Office.employeesNum)


if __name__ == "__main__":
    main()
