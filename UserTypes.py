from enum import Enum

class userType(Enum):
    PERSON = 1
    STUDENT = 2
    EMPLOYEE = 3

class fieldOfStudy(Enum):
    COMPUTER_SCIENCE = 1
    ELECTRONICS = 2
    ENGINEERING = 3
    MEDICAL = 4
    PSYCHOLOGY = 5
    BIOLOGY = 6
    PHYSICS = 7
    CHEMISTRY = 8
    MATHEMATICS = 9

class fieldOfWork(Enum):
    PROGRAMMING = 1
    ELECTRONICS = 2
    ENGINEERING = 3
    MEDICAL = 4
    PSYCHOLOGY = 5

class userChoice(Enum):
    SAVE_NEW_ENTRY = 1
    SEARCH_BY_ID = 2
    PRINT_AVG_AGES = 3
    PRINT_ALL_NAMES = 4
    PRINT_ALL_IDS = 5
    PRINT_ALL_ENTRIES = 6
    PRINT_ENTRY_BY_INDEX = 7
    EXPORT_TO_CSV = 8
    EXIT = 9



