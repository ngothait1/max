from Person import Person
from UserTypes import fieldOfWork
from utils import get_valid_integer_input, get_valid_string_input
import random


class Employee(Person):
    def __init__(self, name:str, personID:str, age:int, field_of_work:str = None, salary:int = None):
        super().__init__(name, personID, age)

        # If the fields are provided, use them
        if field_of_work is not None and salary is not None:
            self.field_of_work = field_of_work
            self.salary = salary
        else:
            # If the fields are not provided, gather the information from the user
            self._gather_employee_info()

    def _gather_employee_info(self):
        """Private method to gather employee-specific information from user input"""
        print("\n--- Employee Information ---")

        # Option 1: Let user choose or use random
        choice = input("Do you want to enter employee details manually? (y/n): ")

        if choice.lower() == "y":
            # Manual input
            self.field_of_work = self._get_field_of_work()
            self.salary = self._get_salary()
        else:
            # Random input
            self.field_of_work = random.choice(list(fieldOfWork)).name
            self.salary = random.randint(8000,50000)
            print("\nRandom employee data generated")
            print("Field of work: " + self.field_of_work + "\nSalary: " + str(self.salary))

    def _get_field_of_work(self):

        """Get field of work from user"""
        print("Available fields of work:")
        for field in fieldOfWork:
            print(str(field.value) + ". " + field.name)

        while True:
            choice = get_valid_integer_input("Enter field of work number: ", "Field of work")
            if choice is None:
                return random.choice(list(fieldOfWork)).name

            try:
                return fieldOfWork(choice).name
            except ValueError:
                print("Invalid choice. Please enter a number between 1 and " + str(len(fieldOfWork)))

    def _get_salary(self):
        
        """Get salary from user"""
        salary = get_valid_integer_input("Enter salary: ", "Salary")
        if salary is None or salary < 0:
            print("Using random salary....")
            return random.randint(8000,50000)
        return salary


    def getFieldOfWork(self):
        return self.field_of_work


    def getSalary(self):
        return self.salary

    def printEmployee(self):
        print(self.getPersonString() + "\n Field of work: " + self.getFieldOfWork() + "\n Salary: " + str(self.getSalary()))

    def myFunc(self):
        print("I am an Employee")

    def printMySelf(self):
        self.printEmployee()