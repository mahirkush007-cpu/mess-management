// User and Feedback structures
let userList = [];
let feedbackList = [];

// User constructor
function User(id, name) {
    this.id = id;
    this.name = name;
    this.balance = 0;
    this.mealCount = 0;
    this.feedback = '';
}

// Feedback constructor
function Feedback(message) {
    this.message = message;
}

// Function to validate User ID
function isValidUserId(id) {
    if (!id || id.length === 0) return false;
    if (!/^[a-zA-Z0-9]+$/.test(id)) return false; // Alphanumeric check
    if (id[0] === '0') return false; // No leading zero
    return true;
}

// Function to add a user
function addUser() {
    const userId = prompt("Enter User ID (alphanumeric, no leading zero):");
    if (!isValidUserId(userId)) {
        alert("Invalid User ID. Try again.");
        return;
    }

    const userName = prompt("Enter User Name:");
    if (userList.some(user => user.id === userId)) {
        alert("User ID already exists. Please choose a different ID.");
        return;
    }

    const newUser = new User(userId, userName);
    userList.push(newUser);
    alert("User added successfully.");
}

// Function to remove a user
function removeUser() {
    const userId = prompt("Enter User ID to remove:");
    const index = userList.findIndex(user => user.id === userId);
    
    if (index === -1) {
        alert("User not found.");
        return;
    }

    userList.splice(index, 1);
    alert("User removed successfully.");
}

// Function to record a meal
function recordMeal() {
    const userId = prompt("Enter User ID to record meal:");
    const user = userList.find(user => user.id === userId);
    
    if (!user) {
        alert("User not found.");
        return;
    }

    if (user.mealCount === 0) {
        user.mealCount++;
        alert(`First meal recorded for ${user.name}. No charges.`);
    } else {
        user.balance += 50; // Charge for additional meals
        user.mealCount++;
        alert(`Meal recorded for ${user.name}. Charge of 50 units added to balance.`);
    }
}

// Function to display users
function displayUsers() {
    if (userList.length === 0) {
        alert("No users to display.");
        return;
    }

    let userInfo = "--- User List ---\n";
    userList.forEach(user => {
        userInfo += `ID: ${user.id}, Name: ${user.name}, Balance: ${user.balance}, Meals: ${user.mealCount}\n`;
    });
    alert(userInfo);
}

// Function to display non-eaters
function displayNonEaters() {
    const nonEaters = userList.filter(user => user.mealCount === 0);
    
    if (nonEaters.length === 0) {
        alert("All users have recorded meals.");
        return;
    }

    let nonEaterInfo = "--- Non-Eaters ---\n";
    nonEaters.forEach(user => {
        nonEaterInfo += `ID: ${user.id}, Name: ${user.name}\n`;
    });
    alert(nonEaterInfo);
}

// Function to generate reports
function generateReports() {
    if (userList.length === 0) {
        alert("No data to generate reports.");
        return;
    }

    let reportInfo = "--- Report ---\n| ID | Name | Meals | Revenue | Plates |\n";
    let totalMeals = 0;
    let totalRevenue = 0;
    let totalPlates = 0;

    userList.forEach(user => {
        if (user.mealCount > 0) {
            totalMeals++;
            totalRevenue += user.balance;
            totalPlates += user.mealCount;
            reportInfo += `| ${user.id} | ${user.name} | ${user.mealCount} | ${user.balance} | ${user.mealCount} |\n`;
        }
    });

    reportInfo += `\nTotal Meals: ${totalMeals}\nTotal Revenue: ${totalRevenue}\nTotal Plates Consumed: ${totalPlates}`;
    alert(reportInfo);
}

// Function to add feedback
function addFeedback() {
    const message = prompt("Enter your feedback:");
    const newFeedback = new Feedback(message);
    feedbackList.push(newFeedback);
    alert("Feedback added successfully.");
}

// Function to view feedback
function viewFeedback() {
    if (feedbackList.length === 0) {
        alert("No feedback available.");
        return;
    }

    let feedbackInfo = "--- Feedback ---\n";
    feedbackList.forEach(feedback => {
        feedbackInfo += `${feedback.message}\n`;
    });
    alert(feedbackInfo);
}

// Main menu function to handle user choices
function showMenu() {
    let choice;
    do {
        choice = prompt(`--- Mess Management System ---\n
1. Add User
2. Remove User
3. Record Meal
4. Display Users
5. Display Non-Eaters
6. Generate Reports
7. Add Feedback
8. View Feedback
9. Exit\n
Enter choice:`);

        switch (choice) {
            case '1': addUser(); break;
            case '2': removeUser(); break;
            case '3': recordMeal(); break;
            case '4': displayUsers(); break;
            case '5': displayNonEaters(); break;
            case '6': generateReports(); break;
            case '7': addFeedback(); break;
            case '8': viewFeedback(); break;
            case '9': alert("Exiting..."); break;
            default: alert("Invalid choice. Try again.");
        }
    } while (choice !== '9');
}

// Start the application
showMenu();
