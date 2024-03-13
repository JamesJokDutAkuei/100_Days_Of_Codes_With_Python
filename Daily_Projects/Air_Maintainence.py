import random

def show_menu():
    print("\nWelcome to the Health and Environment Awareness Program!")
    print("1. Learn about air quality and health.")
    print("2. Get daily air quality reports.")
    print("3. Health tips based on current air quality.")
    print("4. Exit.")

def learn_about_air_quality():
    print("\nUnderstanding Air Quality:")
    print("Air quality is determined by the concentration of pollutants in the air, "
          "which can have significant impacts on human health and the environment. "
          "Poor air quality can cause or exacerbate respiratory diseases, heart disease, "
          "and even affect the brain.")

def daily_air_quality_report():
    # Simulating air quality index values: Good (0-50), Moderate (51-100), Unhealthy (101-150)
    aqi = random.randint(0, 150)
    print(f"\nToday's air quality index is: {aqi}")
    if aqi <= 50:
        print("Status: Good")
    elif 51 <= aqi <= 100:
        print("Status: Moderate")
    else:
        print("Status: Unhealthy")

def health_tips():
    # Providing health tips based on a simplistic version of the air quality report
    aqi = random.randint(0, 150)  # Assume this is the same value the user got in the report.
    print("\nHealth Tips for Today:")
    if aqi <= 50:
        print("Enjoy outdoor activities. It's a great day to be outside!")
    elif 51 <= aqi <= 100:
        print("Sensitive individuals should consider limiting prolonged outdoor exertion.")
    else:
        print("Everyone should avoid prolonged outdoor exertion; sensitive groups should stay indoors.")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            learn_about_air_quality()
        elif choice == '2':
            daily_air_quality_report()
        elif choice == '3':
            health_tips()
        elif choice == '4':
            print("Thank you for using the app. Stay healthy and environmentally conscious!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()

