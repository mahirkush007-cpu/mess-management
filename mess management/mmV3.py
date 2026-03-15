

class User:
    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name
        self.balance = 0
        self.meal_count = 0
        self.feedback = ""
        self.meals = [[0] * 3 for _ in range(7)]  # 7 days, 3 meals per day

class Feedback:
    def __init__(self, message):
        self.message = message


class MessManagementSystem:
    def __init__(self):
        self.user_list = []
        self.feedback_list = []

    # User Management
     # Validates user_id
    def is_valid_user_id(self, user_id):
        return user_id and user_id.isalnum() and user_id[0] != '0'

    # Checks if user_id is unique
    def is_unique_user_id(self, user_id):
        return all(user.id != user_id for user in self.user_list)

    # Adds a new user
    def add_user(self, user_id, name):
        if not self.is_valid_user_id(user_id):
            return {"error": "Invalid User ID"}, False
        if not self.is_unique_user_id(user_id):
            return {"error": "User ID already exists"}, False

        new_user = User(user_id, name)
        self.user_list.append(new_user)
        return {"message": f"User {name} added successfully with ID {user_id}"}, True


    def remove_user(self, user_id):
        for user in self.user_list:
            if user.id == user_id:
                self.user_list.remove(user)
                return {"message": f"User with ID {user_id} removed successfully"}, True
        return {"error": "User ID not found"}, False

    def get_users(self):
        if not self.user_list:
            return {"message": "No users to display."}
        users = [{"id": user.id, "name": user.name, "balance": user.balance, "meal_count": user.meal_count} for user in self.user_list]
        return {"users": users}

    # Meal Management
    def record_meal(self, user_id):
        for user in self.user_list:
            if user.id == user_id:
                if user.meal_count == 0:
                    user.meal_count += 1
                    return {"message": f"First meal recorded for {user.name}. No charges."}, True
                else:
                    meal_charge = 50  # Assuming a fixed charge
                    user.balance += meal_charge
                    user.meal_count += 1
                    return {"message": f"Meal recorded for {user.name}. Charge of 50 units added."}, True
        return {"error": "User ID not found"}, False

    def display_non_eaters(self):
        non_eaters = [{"id": user.id, "name": user.name} for user in self.user_list if user.meal_count == 0]
        if not non_eaters:
            return {"message": "All users have recorded meals."}
        return {"non_eaters": non_eaters}

    # Feedback Management
    def add_feedback(self, message):
        new_feedback = Feedback(message)
        self.feedback_list.append(new_feedback)
        return {"message": "Feedback added successfully"}, True

    def view_feedback(self):
        if not self.feedback_list:
            return {"message": "No feedback available."}
        feedbacks = [{"message": feedback.message} for feedback in self.feedback_list]
        return {"feedbacks": feedbacks}

    # Report Generation
    def generate_reports(self):
        if not self.user_list:
            return {"message": "No data to generate reports."}

        total_meals = sum(user.meal_count for user in self.user_list)
        total_revenue = sum(user.balance for user in self.user_list)
        total_plates = total_meals

        report = {
            "total_meals": total_meals,
            "total_revenue": total_revenue,
            "total_plates": total_plates,
            "user_reports": [
                {"id": user.id, "name": user.name, "meals": user.meal_count, "revenue": user.balance}
                for user in self.user_list
            ],
        }
        return report

    # Menu Viewing
    def view_menu_for_day_and_meal(self, day_index, meal_index):
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        meal_types = ["Breakfast", "Lunch", "Dinner"]
        
        # Menu for each day and meal type
        menu = [
            [  # Sunday
                ["Cereal with Milk", "Toast with Butter", "Aloo Paratha"],  # Breakfast
                ["Chole Bhature", "Paneer Masala with Rice", "Aloo Gobi"],  # Lunch
                ["Dal Tadka", "Aloo Methi", "Rice with Raita"]  # Dinner
            ],
            [  # Monday
                ["Bread Butter", "Poha", "Vegetable Sandwich"],  # Breakfast
                ["Chana Masala", "Aloo Paratha", "Mixed Veg Curry"],  # Lunch
                ["Dal Fry", "Aloo Baingan", "Chapati"]  # Dinner
            ],
            [  # Tuesday
                ["Idli with Sambar", "Upma", "Cereal with Milk"],  # Breakfast
                ["Pav Bhaji", "Veg Pulao", "Aloo Tikki"],  # Lunch
                ["Dal Makhani", "Baingan Bharta", "Rice with Yogurt"]  # Dinner
            ],
            [  # Wednesday
                ["Cornflakes with Milk", "Dosa with Sambar", "Poha"],  # Breakfast
                ["Aloo Gobi", "Methi Paratha", "Chole Rice"],  # Lunch
                ["Kadhi Pakora", "Aloo Tikki", "Chapati"]  # Dinner
            ],
            [  # Thursday
                ["Aloo Tikki", "Vada Pav", "Toast with Butter"],  # Breakfast
                ["Paneer Tikka", "Chana Masala", "Roti with Sabzi"],  # Lunch
                ["Dal Fry", "Veg Biryani", "Aloo Baingan"]  # Dinner
            ],
            [  # Friday
                ["Sabudana Khichdi", "Poha", "Bread Pakora"],  # Breakfast
                ["Chole Bhature", "Pav Bhaji", "Mixed Veg Curry with Roti"],  # Lunch
                ["Dal Tadka", "Aloo Gobi", "Rice with Yogurt"]  # Dinner
            ],
            [  # Saturday
                ["Aloo Paratha", "Samosa", "Veg Cutlet"],  # Breakfast
                ["Veg Biryani", "Paneer Butter Masala", "Chole Rice"],  # Lunch
                ["Dal Makhani", "Aloo Methi", "Chapati"]  # Dinner
            ]
        ]


        # Validate day_index and meal_index
        if not (0 <= day_index < len(days)) or not (0 <= meal_index < len(meal_types)):
            return {"error": "Invalid day or meal type index."}, False

        # Return the selected menu
        return {"day": days[day_index], "meal_type": meal_types[meal_index], "menu": menu[day_index][meal_index]}, True