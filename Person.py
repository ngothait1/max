class Person:

    def __init__(self,name:str,personID:str,age:int):
        self._name = name
        self._id = personID
        self._age = age

    #self - Like in java - this.name or this.age. gives permission to get into the members inside the class
    def getName(self):
        return self._name

    def setName(self,name):
        self._name = name

    def getPersonID(self):
        return self._id

    def getAge(self):
        return self._age

    def setAge(self,age):
        self._age = age

    def getPersonString(self):
        return " ID: " + self._id + "\n Name: " + self._name + "\n Age: " + str(self._age)

    def printMySelf(self):
        print(self.getPersonString())

if __name__ == "__main__":
    test_name = "test"
    test_id = "0"
    test_age = 99

    person = Person(test_name,test_id,test_age)
    if person.getAge() != test_age:
        print("Error: Age should be " + str(test_age) + " but i got " + str(person.getAge()))

    if person.getName() != test_name:
        print("Error: Name should be " + test_name + " but i got " + person.getName())

    if person.getPersonID() != test_id:
        print("Error: ID should be " + test_id + " but i got " + person.getPersonID())
