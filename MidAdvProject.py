import pandas as pd
from Person import Person
from Employee import Employee
from Student import Student
from UserTypes import userType,userChoice


def saveNewEntry(data_dict:dict,keys:list[str]):
    print("You chose to save a new entry")

    try:
        from utils import get_valid_string_input, get_valid_integer_input, validate_id_format
        name = get_valid_string_input("Enter a name: ", "Name")
        if name is None:
            return

        id = get_valid_string_input("Enter an ID: ", "ID")
        if id is None:
            return

        if not validate_id_format(id):
            print("Error: ID must be a number - " + id + " is not a number.\n")
            return

        if id in data_dict:
            person = data_dict[id]
            print("Error, ID already exists: ID: " + id + " ," + "Name: " + person.getName(), " Age: " + person.getAge() + ".\n")
            return

        age = get_valid_integer_input("Enter age: ", "Age")
        if age is None:
            return

        # user_type = choose_user_type()

        # if user_type == userType.PERSON:
        #     person = Person(name, id, age)
        #     data_dict[id] = person
        #
        # elif user_type == userType.STUDENT:
        #     student = Student(name, id,age)
        #     data_dict[id] = student
        #
        # elif user_type == userType.EMPLOYEE:
        #     employee = Employee(name, id, age)
        #     data_dict[id] = employee

        user_type = choose_user_type_2()
        person = user_type(name, id, age)
        data_dict[id] = person

        print("\nYou chose to save a new entry as - " + user_type.__name__)

        data_dict["stats"]["total_age"] += age
        data_dict["stats"]["count"] += 1
        keys.append(id)

        print("ID [" + str(id) + "]" + " saved successfully" + "")

    except Exception as e:
        print("Unexpected error during saveNewEntry: " + str(e))
        return


def searchById(data_dict:dict):
    print("You chose to search by ID")
    id = input("Please enter the ID you want to look for: ")

    if not id.isdigit():
        print("Error: ID must be a number - " + id + " is not a number.")
        return

    if id not in data_dict:
        print("Error, ID " + str(id) + " does not exist")
        return

    data_dict[id].printMySelf()

def printAgesAverage(data_dict:dict):
    print("You chose to print age average")
    count = data_dict.get("stats")["count"]
    if count == 0:
        print("0\n")
    else:
        print("Average: " + str(data_dict["stats"]["total_age"] / count) + "\n")

def printAllNames(data_dict:dict,keys:list[str]):
    print("You chose to Print all names")
    for index,key in enumerate(keys):
        person = data_dict[key]
        print(str(index) + ". " + str(person.getName()))

def printAllIds(keys:list[str]):
    print("You chose to print all IDs")
    for index,key in enumerate (keys):
        print(str(index) + ". " + str(key))


def printAllEntries(data_dict:dict,keys:list[str]):
    print("You chose to print all entries")
    for index, key in enumerate(keys):
        print(str(index) + ". ")
        # printEntry(key, data_dict)
        data_dict[key].printMySelf()


def printEntryByIndex(data_dict:dict, entry_keys:list[str]):
    print("You chose to print entry by index")

    ind = input("Please enter the index of the entry you want to print: ")

    try:
        ind = int(ind)
        data_dict[entry_keys[ind]].printMySelf()
    except ValueError:
        print("Error: index must be a number. " + ind + " is not a number.\n")
        return
    except IndexError:
        print("Error: Invalid or out-of-range index. The maximum index allowed is " + str(len(entry_keys) - 1) + ".\n")
        return



def exit(flag:bool):
    while True:
        confirm = input("Are you sure you want to exit? (Y/N): ")
        if confirm == "y" or confirm == "Y":
            flag = False
            print("Exiting... Goodbye!")
            return flag

        if confirm == "n" or confirm == "N":
            print("Exit canceled.\n")
            return flag


def pause():
    message = "Press Enter to continue...\n"
    input(message)


def exportToCSV(data_dict:dict, keys:list[str]):
    print("You chose to export CSV")

    if not keys:
        print("Error: No entries to export.")
        return

    try:
        file_name = input("What is your output file name? ")
        if not file_name.endswith(".csv"):
            print("Error: File name must end in .csv\n")
            return

        # Define all possible columns for the CSV
        columns = ["id", "name", "age", "type", "field_of_study", "year", "score_avg", "field_of_work", "salary"]
        
        # Created a list to hold a dictionary for each row that will go to CSV file
        data_for_df = []

        for key in keys:
            try:
                entry = data_dict[key]
                
                # Start with basic Person data
                row = {
                    "id": key,
                    "name": entry.getName(), 
                    "age": entry.getAge(),
                    "type": type(entry).__name__,  # This will be "Person", "Student", or "Employee"
                    "field_of_study": "",
                    "year": "",
                    "score_avg": "",
                    "field_of_work": "",
                    "salary": ""
                }

                # Use isinstance to check the type and add specific fields
                if isinstance(entry, Student):
                    try:
                        row["field_of_study"] = entry.getFieldOfStudy()
                        row["year"] = entry.getYear()
                        row["score_avg"] = entry.getScoreAvg()
                    except AttributeError as e:
                        print("Warning: Could not access Student attributes for ID" + key + " " +  str(e))
                        
                elif isinstance(entry, Employee):
                    try:
                        row["field_of_work"] = entry.getFieldOfWork()
                        row["salary"] = entry.getSalary()
                    except AttributeError as e:
                        print("Warning: Could not access Employee attributes for ID " + key + " " +  str(e))

                data_for_df.append(row)
                
            except Exception as e:
                print("Error processing entry with ID " + key + " " +  str(e))
                continue

        if not data_for_df:
            print("Error: No valid data to export.")
            return

        try:
            # Create DataFrame with all columns
            df = pd.DataFrame(data_for_df, columns=columns)
            df.to_csv(file_name, index=False)
            print("CSV exported successfully to " + file_name)
            print("Exported " + str(len(data_for_df)) + " entries.")
            
        except Exception as e:
            print("Error creating or saving CSV file: " + str(e))
            return
            
    except KeyboardInterrupt:
        print("\nExport cancelled by user.")
        return
    except Exception as e:
        print("Unexpected error during export: " + str(e))
        return

def choose_user_type():
    print("Select the type of user you want to create:")

    for user_type in userType:
        print(str(user_type.value) + ". " + user_type.name)

    choice = input("Enter the number for the user type: ")

    try:
        choice_num = int(choice)
        return userType(choice_num)
    except ValueError:
        print("Error: Invalid choice. Please enter a number.\n")
        return choose_user_type()

def choose_user_type_2():
    print("Select the type of user you want to create:")
    user_list = [Person, Student, Employee ]
    for index, user_type in enumerate(user_list):
        print(str(index) + ". " + user_type.__name__)

    choice = input("Enter the number for the user type: ")

    try:
        choice_num = int(choice)
        return user_list[choice_num]
    except ValueError:
        print("Error: Invalid choice. Please enter a number.\n")
        return choose_user_type_2()
    except IndexError:
        print("Error: Invalid choice. Please enter a number between 0 and " + str(len(user_list) - 1) + ".\n")
        return choose_user_type_2()


info_dict = {"stats":{"total_age": 0, "count": 0}}
entry_keys = []
flag = True

while flag:
    try:
        user_input = input("Enter your choice:\n"
              "1. Save a new entry\n"
              "2. Search by ID\n"
              "3. Print ages average\n"
              "4. Print all names\n"
              "5. Print all IDs\n"
              "6. Print all entries\n"
              "7. Print entry by index\n"
              "8. Export to CSV\n"           
              "9. Exit\n")

        try:
            choice = userChoice(int(user_input))
        except (ValueError, KeyError):
            print("Error: Invalid choice. Please enter a valid number.\n")
            continue

        if choice == userChoice.SAVE_NEW_ENTRY:
            saveNewEntry(info_dict, entry_keys)

        elif choice == userChoice.SEARCH_BY_ID:
            searchById(info_dict)

        elif choice == userChoice.PRINT_AVG_AGES:
            printAgesAverage(info_dict)

        elif choice == userChoice.PRINT_ALL_NAMES:
            printAllNames(info_dict, entry_keys)

        elif choice == userChoice.PRINT_ALL_IDS:
            printAllIds(entry_keys)

        elif choice == userChoice.PRINT_ALL_ENTRIES:
            printAllEntries(info_dict, entry_keys)

        elif choice == userChoice.PRINT_ENTRY_BY_INDEX:
            printEntryByIndex(info_dict, entry_keys)

        elif choice == userChoice.EXPORT_TO_CSV:
            exportToCSV(info_dict, entry_keys)

        elif choice == userChoice.EXIT:
            flag = exit(flag)

    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
        flag = False
        break

    pause()




