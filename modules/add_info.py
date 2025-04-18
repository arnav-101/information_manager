from datetime import datetime

# module to add info

def confirmation():             # function to confirm all the infos later on

    while True:
        confirmation = input("Would you like to confirm (y/n):  ").lower().strip()

        if any(ch.isspace() for ch in confirmation):
            print("Please enter input without any spaces.")
            continue

        else:
            if confirmation in ['y', 'n']:
                break
            else:
                print("Kindly enter only 'y' or 'n' for yes and no respectively!")
                continue

    return confirmation




def add_name():     # function to add the name

    while True:
        user_name = input("Enter your name: ").strip()

        if not all(part.isalpha() for part in user_name.split()):
            print("Name can only contain alphabets and spaces.")
            continue

        confirm = confirmation()
        if confirm == 'y':
            print(f"You have confirmed your name as {user_name}")
            break
        else:
            continue
    
    return user_name


        

def add_age():      # function to add the age

    while True:
        user_age = input("Enter your age: ").strip()

        if user_age.isdigit() and ' ' not in user_age:
            user_age = int(user_age)
        else:
            print("Only numbers are accepted. No spaces are allowed either.")
            continue

        confirm = confirmation()
        if confirm == 'y':
            print(f"You have confirmed your age as {user_age}")
            break
        else:
            continue
    
    return user_age




def add_gender():       # function to add gender

    genders = ['male', 'female', 'other']

    while True:
        user_gender = input("Enter your gender (male/female/other): ").lower().strip()
        
        if not(user_gender.isalpha()):
            print("Kindly enter alphabets only, no spaces, special characters, numbers are allowed.")
            continue

        if user_gender in genders:
            pass
        else:
            print("Enter only one of these male/female/other")
            continue
            

        confirm = confirmation()
        if confirm == 'y':
            print(f"You have confirmed your gender as {user_gender}")
            break
        else:
            continue
    
    return user_gender




def add_dob():      # function to add dob
    while True:
        dob_input = input("Enter your date of birth (YYYY-MM-DD): ").strip()

        try:
            dob = datetime.strptime(dob_input, "%Y-%m-%d")
            confirm = confirmation()
            if confirm == 'y':
                print(f"You have confirmed your date of birth as {dob.strftime('%Y-%m-%d')}")
                return dob.strftime('%Y-%m-%d')  # Or return `dob` object if you prefer
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD (e.g., 1990-05-14).")





def add_information():      # function to collect all information and create dict of the user_info
    name = add_name()
    age = add_age()
    gender = add_gender()
    dob = add_dob()

    user_information = {
        'name': name,
        'age': age,
        'gender': gender,
        'dob': dob
    }

    return user_information
