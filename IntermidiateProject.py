def saveNewEntry(data_dict, name, id, age):

    if not id.isdigit():
        print("Error: ID must be a number." + id + " is not a number.")
        pause()
        return

    if id in data_dict:
        print("Error, ID already exists: " + str(data_dict[id]) )
        pause()
        return


    data_dict[id] = {"name": name,"age": age}
    print("ID [" + str(id) + "]" + " saved successfully" + "")
    pause()

def searchById(data_dict, id):
    if not id.isdigit():
        print("Error: ID must be a number." + id + " is not a number.")
        pause()
        return

    if id not in data_dict:
        print("Error, ID " + str(id) + " does not exist")
        pause()
        return

    print("ID: " + id + "\nName: " + data_dict[id]["name"] + "\nAge: " + str(data_dict[id]["age"]))
    pause()


def printAgesAverage(data_dict):
    if len(data_dict) == 0:
        print("0")
        pause()
        return

    total = 0
    for key in data_dict:
        total += data_dict[key]["age"]
    print("Average: " + str(total / len(data_dict)))
    pause()

def printAllNames(data_dict):
    for index,key in enumerate (data_dict):
        print(str(index) + ". " + str(data_dict[key]["name"]))
    pause()

def printAllIds(data_dict):
    for index,key in enumerate (data_dict.keys()):
        print(str(index) + ". " + str(key))
    pause()


def printAllEntries(data_dict):
    for index,key in enumerate (data_dict.keys()):
        print(str(index) + ". " + key + "\n Name: " + data_dict[key]["name"] + "\n Age: " + str(data_dict[key]["age"]))
    pause()

def printEntryByIndex(data_dict, ind):

    if not ind.isdigit():
        print("Error: Index must be a number. " + ind + " is not a number.")
        pause()
        return

    ind = int(ind)

    if ind < 0 or ind >= len(data_dict):
        print("Error: Index out of range. The maximum index allowed is " + str(len(data_dict) - 1))
        pause()
        return

    key = list(data_dict.keys())[ind]

    print("ID: " + key + "\n Name: " + data_dict[key]["name"] + "\n Age: " + str(data_dict[key]["age"]))
    pause()

def pause():
    input(message)

info_dict = {}
flag = True
message = "Press Enter to continue...\n"

while flag:
    user_input = input("Enter your choice:\n"
          "1. Save a new entry\n"
          "2. Search by ID\n"
          "3. Print ages average\n"
          "4. Print all names\n"
          "5. Print all IDs\n"
          "6. Print all entries\n"
          "7. Print entry by index\n"
          "8. Exit\n")

    if user_input == "1":
        print("You chose to save a new entry")

        name = input("Enter a name: ")
        person_id = input("Enter a id: ")
        age = input("Enter age: ")

        if not age.isdigit():
            print("Error: Age must be a number." + age + " is not a number.")
            pause()
            continue
        age = int(age)
        saveNewEntry(info_dict, name, person_id, age)

    elif user_input == "2":
        print("You chose to search by ID")
        person_id = input("Please enter the ID you want to look for: ")
        searchById(info_dict, person_id)


    elif user_input == "3":
        print("You chose to print age average")
        printAgesAverage(info_dict)

    elif user_input == "4":
        print("You chose to Print all names")
        printAllNames(info_dict)

    elif user_input == "5":
        print("You chose to print all IDs")
        printAllIds(info_dict)

    elif user_input == "6":
        print("You chose to print all entries")
        printAllEntries(info_dict)

    elif user_input == "7":
        print("You chose to print entry by index")
        ind = input("Please enter the index of the entry you want to print: ")
        printEntryByIndex(info_dict, ind)


    elif user_input == "8":
        while True:
            confirm = input("Are you sure you want to exit? (Y/N): ")
            if confirm == "y" or confirm == "Y":
                flag = False
                print("Exiting... Goodbye!")
                break

            if confirm == "n" or confirm == "N":
                print("Exit canceled.\n")
                break

    else:
        print("Option " + str(user_input) + " does not exist. Please try again.\n")




