
def get_valid_integer_input(prompt,field_name):
    while True:
        try:
            user_input = int(input(prompt))
            return int(user_input)
        except ValueError:
            print("Error: " + field_name +  " must be a number - " + str(user_input) + " is not a number.")
            retry = input("Retry? (y/n): ")
            if retry.lower() != "y":
                return None
        except KeyboardInterrupt:
            print("Keyboard interrupt detected. Exiting...")
            return None

def get_valid_float_input(prompt,field_name):
    while True:
        try:
            user_input = float(input(prompt))
            return float(user_input)
        except ValueError:
            print("Error: " + field_name + " must be a number - " + str(user_input) + " is not a number.")
            retry = input("Retry? (y/n): ")
            if retry.lower() != "y":
                return None
        except KeyboardInterrupt:
            print("Keyboard interrupt detected. Exiting...")
            return None

def validate_id_format(id_str):
    return id_str.isdigit()

def get_valid_string_input(prompt,field_name):
    try:
        user_input = input(prompt)
        if not user_input.strip():
            print("Error: " + field_name + " cannot be empty.")
            return None
        return user_input.strip()
    except KeyboardInterrupt:
        print("Keyboard interrupt detected. Exiting...")
        return None


