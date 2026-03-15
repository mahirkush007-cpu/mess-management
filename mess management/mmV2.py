class User:
    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name
        self.balance = 0
        self.meal_count = 0
        self.feedback = ""
        self.meals = [[0] * 3 for _ in range(7)]  # 7 days, 3 meals per day
        self.next = None


class Feedback:
    def __init__(self, message):
        self.message = message
        self.next = None


def menu():
    user_list = None
    feedback_list = None

    while True:
        print("\n--- Mess Management System ---")
        print("1. Add User")
        print("2. Remove User")
        print("3. Record Meal")
        print("4. Display Users")
        print("5. Display Non-Eaters")
        print("6. Generate Reports")
        print("7. Add Feedback")
        print("8. View Feedback")
        print("9. View Menu for a Specific Day and Meal Type")
        print("10. Exit")

        choice = input("Enter choice: ")
        if not choice.isdigit() or not (1 <= int(choice) <= 10):
            print("Invalid input. Please enter a valid number.")
            continue

        choice = int(choice)

        if choice == 1:
            user_list = add_user(user_list)  # Capture the updated user list
            display_users(user_list)
        elif choice == 2:
            user_list = remove_user(user_list)
        elif choice == 3:
            record_meal(user_list)
        elif choice == 4:
            display_users(user_list)
        elif choice == 5:
            display_non_eaters(user_list)
        elif choice == 6:
            generate_reports(user_list)
        elif choice == 7:
            feedback_list = add_feedback(feedback_list)
        elif choice == 8:
            view_feedback(feedback_list)
        elif choice == 9:
            view_menu_for_day_and_meal()
        elif choice == 10:
            print("Exiting...")
            break


def is_valid_user_id(user_id):
    if not user_id or not user_id.isalnum() or user_id[0] == '0':
        return False
    return True


def is_unique_user_id(user_list, user_id):
    temp = user_list
    while temp:
        if temp.id == user_id:
            return False
        temp = temp.next
    return True


def add_user(user_list):
    user_id = input("Enter User ID (alphanumeric, no leading zero): ")
    while not is_valid_user_id(user_id) or not is_unique_user_id(user_list, user_id):
        print("Invalid or duplicate User ID. Try again.")
        user_id = input("Enter User ID (alphanumeric, no leading zero): ")

    name = input("Enter User Name: ")
    new_user = User(user_id, name)
    new_user.next = user_list
    print(f"User  {name} added successfully with ID {user_id}.")  # Debug print
    return new_user


def find_user_by_id(user_list, user_id):
    temp = user_list
    while temp:
        if temp.id == user_id:
            return temp
        temp = temp.next
    return None


def display_users(user_list):
    if user_list is None:
        print("No users to display.")
        return

    print("\n--- User List ---")
    temp = user_list
    while temp:
        print(f"User  ID: {temp.id}, Name: {temp.name}, Balance: {temp.balance}, Meal Count: {temp.meal_count}")
        temp = temp.next

def remove_user(user_list):
    user_id = input("Enter User ID to remove: ")
    temp = user_list
    prev = None

    while temp and temp.id != user_id:
        prev = temp
        temp = temp.next

    if not temp:
        print("User  not found.")
        return user_list

    if prev:
        prev.next = temp.next
    else:
        user_list = temp.next

    print("User  removed successfully.")
    return user_list


def record_meal(user_list):
    user_id = input("Enter User ID to record meal: ")
    user = find_user_by_id(user_list, user_id)
    if not user:
        print("User  not found.")
        return

    if user.meal_count == 0:
        user.meal_count += 1
        print(f"First meal recorded for {user.name}. No charges.")
    else:
        meal_charge = 50  # Assuming meal charge is 50 units
        user.balance += meal_charge
        user.meal_count += 1
        print(f"Meal recorded for {user.name}. Charge of 50 units added to balance.")


def display_users(user_list):
    if user_list is None:
        print("No users to display.")
        return

    print("\n--- User List ---")
    temp = user_list
    while temp:
        print(f"User  ID: {temp.id}, Name: {temp.name}, Balance: {temp.balance}, Meal Count: {temp.meal_count}")
        temp = temp.next


def display_non_eaters(user_list ):
    if not user_list:
        print("No users to display.")
        return

    print("\n--- Non-Eaters ---")
    temp = user_list
    found = False
    while temp:
        if temp.meal_count == 0:
            print(f"ID: {temp.id}, Name: {temp.name}")
            found = True
        temp = temp.next

    if not found:
        print("All users have recorded meals.")


def generate_reports(user_list):
    if not user_list:
        print("No data to generate reports.")
        return

    total_meals = 0
    total_revenue = 0
    total_plates = 0

    print("\n--- Report ---")
    print("| ID        | Name               | Meals | Revenue | Plates |")
    print("|-----------|--------------------|-------|---------|--------|")

    temp = user_list
    while temp:
        if temp.meal_count > 0:
            total_meals += 1
            total_revenue += temp.balance
            total_plates += temp.meal_count

            print(f"| {temp.id:<9} | {temp.name:<18} | {temp.meal_count:<5} | {temp.balance:<7} | {temp.meal_count:<6} |")
        temp = temp.next

    print(f"\nTotal Meals: {total_meals}")
    print(f"Total Revenue: {total_revenue}")
    print(f"Total Plates Consumed: {total_plates}")


def add_feedback(feedback_list):
    message = input("Enter your feedback: ")
    new_feedback = Feedback(message)
    new_feedback.next = feedback_list
    return new_feedback


def view_feedback(feedback_list):
    if not feedback_list:
        print("No feedback available.")
        return

    print("\n--- Feedback ---")
    temp = feedback_list
    while temp:
        print(temp.message)
        temp = temp.next


def view_menu_for_day_and_meal():
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    meal_types = ["Breakfast", "Lunch", "Dinner"]
    menu = [
        [  # Sunday
            ["Poha", "Upma", "Aloo Paratha", "Dosa"],
            ["Chole Bhature", "Paneer Butter Masala with Naan", "Aloo Gobi", "Vegetable Pulao"],
            ["Palak Paneer", "Baingan Bharta", "Aloo Methi", "Dum Aloo"]
        ],
        [  # Monday
            ["Aloo Paratha", "Chana Masala", "Idli Sambhar", "Paratha with Curd"],
            ["Chole Tikki", "Paneer Tikka", "Baingan Bharta with Roti", "Vegetable Biryani"],
            ["Methi Thepla", "Aloo Tikki", "Mushroom Masala", "Dal Tadka"]
        ],
        [  # Tuesday
            ["Dosa with Sambar", "Pav Bhaji", "Sabudana Khichdi", "Poha"],
            ["Aloo Gobi", "Palak Paneer", "Methi Thepla with Yogurt", "Rajma with Rice"],
            ["Dal Makhani", "Kadhi Pakora", "Methi Paratha", "Aloo Baingan"]
        ],
        [  # Wednesday
            ["Dhokla", "Aloo Paratha", "Poha", "Sambar Idli"],
            ["Chana Masala with Rice", "Chole Bhature", "Aloo Gobi with Chapati", "Paneer Bhurji"],
            ["Gobi Masala", "Baingan Masala", "Kadhi Pakora", "Pulao"]
        ],
        [  # Thursday
            ["Aloo Tikki", "Samosa", "Pongal", "Upma"],
            ["Aloo Paratha", "Baingan Bharta", "Vegetable Kofta Curry", "Chole Rice"],
            ["Dal Fry", "Aloo Gobi", "Mutter Paneer", "Pulao with Raita"]
        ],
        [  # Friday
            ["Vada Pav", "Poha", "Sabudana Khichdi", "Chana Chaat"],
            ["Dal Tadka", "Gobi Manchurian", "Pav Bhaji", "Aloo Methi Paratha"],
            ["Kadhi Pakora", "Pulao with Paneer", "Methi Thepla", "Chana Masala"]
        ],
        [  # Saturday
            ["Aloo Paratha", "Samosa with Chutney", "Dosa", "Idli with Sambar"],
            [" Vegetable Biryani", "Paneer Tikka with Naan", "Chole Rice", "Mixed Vegetable Curry"],
            ["Dal Makhani", "Gobi Aloo", "Methi Thepla with Yogurt", "Aloo Baingan"]
        ]
    ]

    print("\n--- Select a Day to View Meals ---")
    for i, day in enumerate(days):
        print(f"{i + 1}. {day}")
    day_choice = int(input("Enter day number (1-7): ")) - 1

    if day_choice < 0 or day_choice >= len(days):
        print("Invalid day choice. Please select a valid day.")
        return

    print("\n--- Select a Meal Type ---")
    for i, meal_type in enumerate(meal_types):
        print(f"{i + 1}. {meal_type}")
    meal_choice = int(input("Enter meal type (1-3): ")) - 1

    if meal_choice < 0 or meal_choice >= len(meal_types):
        print("Invalid meal choice. Please select a valid meal type.")
        return

    print(f"\n--- Menu for {days[day_choice]} - {meal_types[meal_choice]} ---")
    for i, item in enumerate(menu[day_choice][meal_choice]):
        print(f"{i + 1}. {item}")


if __name__ == "__main__":
    menu()
