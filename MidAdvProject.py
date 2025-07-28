import pandas as pd
import os
import json

def saveNewEntry(data_dict):
    print("You chose to save a new entry")

    name = input("Enter a name: ")
    id = input("Enter a id: ")
    age = input("Enter age: ")

    if not age.isdigit():
        print("Error: Age must be a number." + age + " is not a number.")
        return
    age = int(age)

    if not id.isdigit():
        print("Error: ID must be a number." + id + " is not a number.")
        return

    if id in data_dict:
        print("Error, ID already exists: " + str(data_dict[id]) )
        return


    data_dict[id] = {"name": name,"age": age}
    data_dict["stats"]["total_age"] += age
    data_dict["stats"]["count"] += 1
    entry_keys.append(id)

    print("ID [" + str(id) + "]" + " saved successfully" + "")

def searchById(data_dict):
    print("You chose to search by ID")
    id = input("Please enter the ID you want to look for: ")
    if not id.isdigit():
        print("Error: ID must be a number." + id + " is not a number.")
        return

    if id not in data_dict:
        print("Error, ID " + str(id) + " does not exist")
        return

    # print("ID: " + id + "\nName: " + data_dict[id]["name"] + "\nAge: " + str(data_dict[id]["age"]))
    printEntry(id, data_dict)

def printAgesAverage(data_dict):
    print("You chose to print age average")
    count = data_dict.get("stats")["count"]
    if count == 0:
        print("0\n")
    else:
        print("Average: " + str(data_dict["stats"]["total_age"] / count) + "\n")

def printAllNames(data_dict):
    print("You chose to Print all names")
    for index,key in enumerate (k for k in data_dict.keys() if k != "stats"):
        print(str(index) + ". " + str(data_dict[key]["name"]))

def printAllIds(data_dict):
    print("You chose to print all IDs")
    entry_keys = [k for k in data_dict.keys() if k != "stats"]
    for index,key in enumerate (entry_keys):
        print(str(index) + ". " + str(key))


def printAllEntries(data_dict):
    print("You chose to print all entries")
    entry_keys = [k for k in data_dict.keys() if k != "stats"]
    for index, key in enumerate(entry_keys):
        print(str(index) + ". ")
        printEntry(key, data_dict)

def printEntryByIndex(data_dict, entry_keys):
    print("You chose to print entry by index")
    ind = input("Please enter the index of the entry you want to print: ")

    if not ind.isdigit():
        print("Error: Index must be a number. " + ind + " is not a number.")
        return

    ind = int(ind)

    if ind < 0 or ind >= len(entry_keys):
        print("Error: Index out of range. The maximum index allowed is " + str(len(entry_keys) - 1))
        return

    idKey = entry_keys[ind]
    printEntry(idKey, data_dict)

def exit(flag):
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

def printEntry(key, entry):
    print(" ID: " + key + "\n Name: " + entry[key]["name"] + "\n Age: " + str(entry[key]["age"]))

def exportToCSV(data_dict):
    print("You chose to export CSV")

    id_keys = [k for k in data_dict if k != "stats"]

    if not id_keys:
        print("Error: No entries to export.")
        return

    file_name = input("What is your output file name? ")
    if not file_name.endswith(".csv"):
        print("Error: File name must end in .csv")
        return

    if not os.path.exists("conf.json"):
        print("Error: Config file conf.json is missing in path: " + os.getcwd())
        return

    with open("conf.json", "r") as json_file:
        conf = json.load(json_file)

    # Created a list to hold a dictionary for each row that will go to CSV file.
    data_for_df = []

    # id_keys - a list of users IDs
    for key in id_keys:
        entry = data_dict[key] #for each ID key, i get the data from the dictionary.
        row = {} #Starts an empty row.

        # conf.items() comes from the json files that looks like this - {"id": "id", "name": "name", "age": "age"}
        for csv_column, data_key in conf.items():
            #If the data key is "id", the value is not inside the user’s entry
            #(since the dictionary structure is: data_dict[id]), so i used the key itself for the "id" column.

           if data_key == "id":
               row[csv_column] = key

           #Otherwise, get the value from the user's entry with entry.get(data_key, "").
           #If it's missing, put an empty string ("").
           else:
               row[csv_column] = entry.get(data_key,"")

        #After the loop, row = {"id": "12421", "name": "Max", "age": 30}, so we add it to the list.
        data_for_df.append(row)

    #This builds a table from our list of dictionaries.
    df = pd.DataFrame(data_for_df, columns=conf.keys())
    df.to_csv(file_name,index=False)
    print(f"CSV exported successfully to {file_name}!")









info_dict = {"stats":{"total_age": 0, "count": 0}}
entry_keys = []
flag = True

while flag:
    user_input = input("Enter your choice:\n"
          "1. Save a new entry\n"
          "2. Search by ID\n"
          "3. Print ages average\n"
          "4. Print all names\n"
          "5. Print all IDs\n"
          "6. Print all entries\n"
          "7. Print entry by index\n"
          "8. Save all data\n"           
          "9. Exit\n")

    if user_input == "1":
        saveNewEntry(info_dict)


    elif user_input == "2":
        searchById(info_dict)

    elif user_input == "3":
        printAgesAverage(info_dict)


    elif user_input == "4":
        printAllNames(info_dict)


    elif user_input == "5":
        printAllIds(info_dict)


    elif user_input == "6":
        printAllEntries(info_dict)


    elif user_input == "7":
        printEntryByIndex(info_dict,entry_keys)


    elif user_input == "8":
        exportToCSV(info_dict)


    elif user_input == "9":
        flag = exit(flag)

    else:
        print("Option " + str(user_input) + " does not exist. Please try again.\n")

    pause()




