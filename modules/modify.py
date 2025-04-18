from modules.add_info import confirmation, add_name, add_age, add_gender, add_dob

import sys
import os

# Add parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import data_store



def modify_name():

    user_name = data_store.user_info['name']
    print(f"Your current name is: {user_name}")
    print("Confirm that you would like to modify")

    confirm = confirmation()

    if confirm == 'y':
        modified_name = add_name()
    else:
        return


    return modified_name




def modify_age():

    user_age = data_store.user_info['age']
    print(f"Your current name is: {user_age}")
    print("Confirm that you would like to modify")

    confirm = confirmation()

    if confirm == 'y':
        modified_age = add_age()
    else:
        return


    return modified_age




def modify_gender():

    user_gender = data_store.user_info['age']
    print(f"Your current name is: {user_gender}")
    print("Confirm that you would like to modify")

    confirm = confirmation()

    if confirm == 'y':
        modified_gender = add_gender()
    else:
        return


    return modified_gender




def modify_dob():

    user_dob = data_store.user_info['age']
    print(f"Your current name is: {user_dob}")
    print("Confirm that you would like to modify")

    confirm = confirmation()

    if confirm == 'y':
        modified_dob = add_dob()
    else:
        return


    return modified_dob



def modify_information():
    print("What would you like to modify:")
    for keys, value in data_store.user_info.items():
        print(f'{keys.title()}: {value}')

    choices = list(data_store.user_info.keys())

    while True:
        user_choice = input("Enter what you would like to modify:  ").lower().strip()

        if any(ch.isspace() for ch in user_choice):
            print("No spaces are allowed in between the input.")
            continue

        else:
            if user_choice in choices:
                confirm = confirmation()
                if confirm == 'y':
                    break
                else:
                    continue
            else:
                print("Enter a valid input (name/age/gender/dob)")
                continue

    
    match user_choice:

        case 'name':
            modified_name = modify_name()
            data_store.user_info['name'] = modified_name

        case 'age':
            modified_age = modify_age()
            data_store.user_info['age'] = modified_age

        case 'gender':
            modified_gender = modify_gender()
            data_store.user_info['gender'] = modified_gender
        
        case 'dob':
            modified_dob = modify_dob()
            data_store.user_info['dob'] = modified_dob
        


    # print(user_choice)

    

