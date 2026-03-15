from flask import Flask, render_template, request, jsonify
from mmV3 import MessManagementSystem

mms = MessManagementSystem()


app = Flask(__name__)

@app.route('/add_user', methods=['POST'])  # Ensure there's no typo here
def add_user():
    data = request.get_json()
    user_id = data.get('user_id')
    name = data.get('name')
    print("Checking mms object:", dir(mms))  # This will print the available methods of mms
    if not user_id or not name:
        return jsonify({"error": "Missing data"}), 400

    response, success = mms.add_user(user_id, name)
    return jsonify(response), 201 if success else 400


@app.route('/remove_user', methods=['POST'])
def remove_user():
    data = request.get_json()
    user_id = data.get('user_id')

    response, success = mms.remove_user(user_id)
    return jsonify(response), 200 if success else 404

@app.route('/get_meals', methods=['POST'])
def get_meals():
    try:
        # Parse request data
        data = request.json
        day = data.get('day')  # Get the day from the request
        meal_type = data.get('meal_type')  # Get the meal type (Breakfast, Lunch, Dinner)

        # Validate input: Make sure both 'day' and 'meal_type' are provided
        if not day or not meal_type:
            return jsonify({"error": "Missing day or meal type"}), 400

        # Define valid days and meal types
        days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
        meal_types = ["breakfast", "lunch", "dinner"]

        # Check if the provided day and meal type are valid
        if day.lower() not in days or meal_type.lower() not in meal_types:
            return jsonify({"error": "Invalid day or meal type"}), 400

        # Get the indices for day and meal type
        day_index = days.index(day.lower())
        meal_index = meal_types.index(meal_type.lower())

        # Fetch menu from the Mess Management System
        result, success = mms.view_menu_for_day_and_meal(day_index, meal_index)

        # If fetching menu is successful, return the menu list
        if success:
            return jsonify({"menu": result["menu"]}), 200  # Return the menu
        else:
            return jsonify({"error": "Could not retrieve menu"}), 400

    except Exception as e:
        # If an error occurs, send an error response
        return jsonify({"error": str(e)}), 500
    
@app.route('/add_feedback', methods=['POST'])
def add_feedback():
    try:
        data = request.get_json()  # Get the feedback message from the request body
        feedback_message = data.get('message')

        if not feedback_message:
            return jsonify({"error": "Missing feedback message"}), 400

        # Here, you would store the feedback in your system (or add it to a list)
        # Assuming you have a feedback list like in the MessManagementSystem
        mms.add_feedback(feedback_message)

        return jsonify({"message": "Feedback added successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/view_feedback', methods=['GET'])
def view_feedback():
    response = mms.view_feedback()
    if "feedbacks" in response:
        return jsonify({"feedbacks": response["feedbacks"]}), 200
    else:
        return jsonify({"error": "No feedback available."}), 404



# Sample data structures (you can modify these as needed)
user_list = []  # This will hold user data
feedback_list = []  # This will hold feedback data

@app.route('/')
def home():
    return render_template('home.html') 

@app.route('/dash.html')
def dash():
    return render_template('dash.html')  # Render the dashboard page

@app.route('/report.html')
def report():
    return render_template('report.html')

@app.route('/meals.html')
def meal():
    return render_template('meals.html')

@app.route('/lunch.html')
def lunch():
    return render_template('lunch.html')

@app.route('/dinner.html')
def dinner():
    return render_template('dinner.html')

@app.route('/user.html')
def user():
    return render_template('user.html')

@app.route('/feedback.html')
def feedback():
    return render_template('feedback.html')

if __name__ == '__main__':
   app.run(debug=True, port=5001)  # Change to port 5001 or any other available port  
for rule in app.url_map.iter_rules():
    print(rule)
