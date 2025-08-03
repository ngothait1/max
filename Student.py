from Person import Person
from UserTypes import fieldOfStudy
from utils import get_valid_integer_input, get_valid_float_input, get_valid_string_input
import random

class Student(Person):
    def __init__(self, name:str, personID:str, age:int, field_of_study:str = None, year:int = None, score_avg:float = None):
        super().__init__(name, personID, age)
        if field_of_study is not None and year is not None and score_avg is not None:
            self.field_of_study = field_of_study
            self.year = year
            self.score_avg = score_avg
        else:
            self._gather_student_info()

    def _gather_student_info(self):
        print("\n--- Student Information ---")

        choice = input("Do you want to enter student details manually? (y/n): ")
        if choice.lower() == "y":
            self.field_of_study = self._get_field_of_study()
            self.year = self._get_year()
            self.score_avg = self._get_score_avg()

    def _get_field_of_study(self):
        print("Available fields of study:")
        for field in fieldOfStudy:
            print(str(field.value) + ". " + field.name)

        while True:
            choice = get_valid_integer_input("Enter field of study number: ", "Field of study")
            if choice is None:
                return random.choice(list(fieldOfStudy)).name

            try:
                return fieldOfStudy(choice).name
            except ValueError:
                print("Invalid choice. Please enter a number between 1 and " + str(len(fieldOfStudy)))

    def _get_year(self):
        year = get_valid_integer_input("Enter year: ", "Year")
        if year is None or year < 1:
            print("Using random year....")
            return random.randint(1,5)
        return year


    def _get_score_avg(self):
        score = get_valid_float_input("Enter score average: ", "Score AVG")
        if score is None or score < 1 or score > 100:
            print("Using random score....")
            return random.randint(1,100)
        return score


    def getFieldOfStudy(self):
        return self.field_of_study

    def getYear(self):
        return self.year

    def getScoreAvg(self):
        return self.score_avg

    def printStudent(self):
        print(self.getPersonString() + "\n Field of study: " + self.getFieldOfStudy() + "\n Year: " + str(self.getYear()) + " \n Score AVG: " + str(self.getScoreAvg()))

    def myFunc(self):
        print("I am a student")

    def printMySelf(self):
        self.printStudent()




