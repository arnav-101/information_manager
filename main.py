from modules.add_info import confirmation, add_name, add_age, add_gender, add_dob, add_information
import data_store
import modules.modify

menu = {
    1: 'Add information',
    2: 'Modify information',
    3: 'Get information',
    4: 'Explore information',
    5: 'Exit'
}

def display_menu():
    print("\nWelcome to the Information Manager")
    print("Here's a menu of things you can do:\n")

    for key, value in menu.items():
        print(f"\t{key}. {value}")


def run_menu():
    while True:
        display_menu()
        user_choice = input("\nEnter your choice (1-5): ").strip()

        # Input validation
        if not user_choice.isdigit():
            print("Enter digits only.")
            continue

        user_choice = int(user_choice)

        if user_choice not in menu:
            print("Enter a valid number from the menu.")
            continue

        confirm = confirmation()
        if confirm != 'y':
            print("Okay, returning to menu.\n")
            continue

        # Perform action based on choice
        match user_choice:
            case 1:
                if not data_store.user_info:
                    info = add_information()
                    data_store.user_info = info
                    print("\n✅ Information added successfully!")
                    print("Here's what you entered:")
                    for key, value in data_store.user_info.items():
                        print(f"  - {key.capitalize()}: {value}")
                
                else:
                    print("Data has already been added and can now only be viewed or modified.")

            case 2:
                modules.modify.modify_information()

            case 3:
                print("Here's your currently stored information.")
                for key, value in data_store.user_info.items():
                        print(f"  - {key.capitalize()}: {value}")

            case 4:
                print("🔍 Explore functionality not implemented yet.")

            case 5:
                print("👋 Exiting... Goodbye!")
                quit()

        input("\nPress Enter to return to the main menu...")

# Run the menu
run_menu()
