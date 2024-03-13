def show_menu():
    print("\nWelcome to the Digital Learning Hub!")
    print("1. Learn New Skills")
    print("2. Track Learning")
    print("3. Find Resources")
    print("4. Exit")

def learn_new_skills():
    skills = ['Programming', 'Data Analysis', 'Cybersecurity', 'Digital Marketing']
    print("\nSelect a skill to learn:")
    for i, skill in enumerate(skills, 1):
        print(f"{i}. {skill}")
    choice = input("Enter your choice: ")
    print(f"You have chosen to learn {skills[int(choice) - 1]}.")

def track_learning():
    print("\nEnter the number of hours you have spent learning today: ")
    hours = input()
    print(f"Great! You have logged {hours} hours of learning today.")

def find_resources():
    resources = {
        'Programming': 'https://www.codecademy.com',
        'Data Analysis': 'https://www.datacamp.com',
        'Cybersecurity': 'https://www.cybrary.it',
        'Digital Marketing': 'https://www.hubspot.com/resources'
    }
    print("\nSelect a skill to find resources:")
    skills = list(resources.keys())
    for i, skill in enumerate(skills, 1):
        print(f"{i}. {skill}")
    choice = input("Enter your choice: ")
    chosen_skill = skills[int(choice) - 1]
    print(f"Here are some resources to learn {chosen_skill}: {resources[chosen_skill]}")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            learn_new_skills()
        elif choice == '2':
            track_learning()
        elif choice == '3':
            find_resources()
        elif choice == '4':
            print("Thank you for using the Digital Learning Hub. Keep learning!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

