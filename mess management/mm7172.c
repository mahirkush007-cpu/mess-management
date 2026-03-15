/*Project Name: Mess Management System
  
  Group Members: 1. Mahir Bhat - 23001003071
                 2. Manik Zutshi - 23001003072*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// Define structures
typedef struct User {
    char id[20];             // User ID (alphanumeric allowed)
    char name[50];           // User name
    int balance;             // User balance (whole number)
    int mealCount;           // Meal count
    char feedback[100];      // Feedback
    int meals[7][3];         // Meals for each day of the week (7 days, 3 meals per day)
    struct User* next;       // Pointer to next user
} User;

typedef struct Feedback {
    char message[100];
    struct Feedback* next;
} Feedback;

// Function prototypes
void menu();
void addUser(User** userList);
void removeUser(User** userList);
void recordMeal(User* userList);
void displayUsers(User* userList);
void displayNonEaters(User* userList);
void generateReports(User* userList);
void addFeedback(Feedback** feedbackList);
void viewFeedback(Feedback* feedbackList);
void viewMenuForDayAndMeal();  // New function to view meals for a specific day and meal type

int isValidUserId(const char* id);
int isValidBalance(int balance);
User* findUserById(User* userList, const char* id);
int isUniqueUserId(User* userList, const char* id);
void clearInputBuffer();  // Function to clear the input buffer

int main() {
    menu();
    return 0;
}

// Main menu function
void menu() {
    User* userList = NULL;
    Feedback* feedbackList = NULL;
    int choice;

    do {
        printf("\n--- Mess Management System ---\n");
        printf("1. Add User\n");
        printf("2. Remove User\n");
        printf("3. Record Meal\n");
        printf("4. Display Users\n");
        printf("5. Display Non-Eaters\n");
        printf("6. Generate Reports\n");
        printf("7. Add Feedback\n");
        printf("8. View Feedback\n");
        printf("9. View Menu for a Specific Day and Meal Type\n");  // Meal menu option now second-last
        printf("10. Exit\n");  // Exit option last
        printf("Enter choice: ");
        if (scanf("%d", &choice) != 1) {
            clearInputBuffer();  // Clear the buffer if invalid input
            printf("Invalid input. Please enter a valid number.\n");
            continue;
        }

        switch (choice) {
            case 1: addUser(&userList); break;
            case 2: removeUser(&userList); break;
            case 3: recordMeal(userList); break;
            case 4: displayUsers(userList); break;
            case 5: displayNonEaters(userList); break;
            case 6: generateReports(userList); break;
            case 7: addFeedback(&feedbackList); break;
            case 8: viewFeedback(feedbackList); break;
            case 9: viewMenuForDayAndMeal(); break;  // New case
            case 10: printf("Exiting...\n"); break;  // Last case for exit
            default: printf("Invalid choice. Try again.\n");
        }
    } while (choice != 10);  // Loop ends when choice is 10 (exit)
}

// Function to clear the input buffer
void clearInputBuffer() {
    while (getchar() != '\n');  // Consume all characters until a newline
}

void viewMenuForDayAndMeal() {
    const char* days[] = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
    const char* mealTypes[] = {"Breakfast", "Lunch", "Dinner"};
    int dayChoice, mealChoice;

    // Define vegetarian Indian meal options for each day and meal type
    const char* menu[7][3][4] = {
        {   // Sunday
            {"Poha", "Upma", "Aloo Paratha", "Dosa"},                  // Breakfast
            {"Chole Bhature", "Paneer Butter Masala with Naan", "Aloo Gobi", "Vegetable Pulao"},  // Lunch
            {"Palak Paneer", "Baingan Bharta", "Aloo Methi", "Dum Aloo"}  // Dinner
        },
        {   // Monday
            {"Aloo Paratha", "Chana Masala", "Idli Sambhar", "Paratha with Curd"},  // Breakfast
            {"Chole Tikki", "Paneer Tikka", "Baingan Bharta with Roti", "Vegetable Biryani"}, // Lunch
            {"Methi Thepla", "Aloo Tikki", "Mushroom Masala", "Dal Tadka"}         // Dinner
        },
        {   // Tuesday
            {"Dosa with Sambar", "Pav Bhaji", "Sabudana Khichdi", "Poha"},        // Breakfast
            {"Aloo Gobi", "Palak Paneer", "Methi Thepla with Yogurt", "Rajma with Rice"}, // Lunch
            {"Dal Makhani", "Kadhi Pakora", "Methi Paratha", "Aloo Baingan"}      // Dinner
        },
        {   // Wednesday
            {"Dhokla", "Aloo Paratha", "Poha", "Sambar Idli"},                   // Breakfast
            {"Chana Masala with Rice", "Chole Bhature", "Aloo Gobi with Chapati", "Paneer Bhurji"},  // Lunch
            {"Gobi Masala", "Baingan Masala", "Kadhi Pakora", "Pulao"}           // Dinner
        },
        {   // Thursday
            {"Aloo Tikki", "Samosa", "Pongal", "Upma"},                        // Breakfast
            {"Aloo Paratha", "Baingan Bharta", "Vegetable Kofta Curry", "Chole Rice"},  // Lunch
            {"Dal Fry", "Aloo Gobi", "Mutter Paneer", "Pulao with Raita"}      // Dinner
        },
        {   // Friday
            {"Vada Pav", "Poha", "Sabudana Khichdi", "Chana Chaat"},            // Breakfast
            {"Dal Tadka", "Gobi Manchurian", "Pav Bhaji", "Aloo Methi Paratha"},  // Lunch
            {"Kadhi Pakora", "Pulao with Paneer", "Methi Thepla", "Chana Masala"} // Dinner
        },
        {   // Saturday
            {"Aloo Paratha", "Samosa with Chutney", "Dosa", "Idli with Sambar"},   // Breakfast
            {"Vegetable Biryani", "Paneer Tikka with Naan", "Chole Rice", "Mixed Vegetable Curry"}, // Lunch
            {"Dal Makhani", "Gobi Aloo", "Methi Thepla with Yogurt", "Aloo Baingan"}  // Dinner
        }
    };

    // Prompt user to choose a day of the week
    printf("\n--- Select a Day to View Meals ---\n");
    for (int i = 0; i < 7; i++) {
        printf("%d. %s\n", i + 1, days[i]);
    }
    printf("Enter day number (1-7): ");
    if (scanf("%d", &dayChoice) != 1 || dayChoice < 1 || dayChoice > 7) {
        clearInputBuffer();  // Clear the buffer if invalid input
        printf("Invalid day choice. Please select a valid day.\n");
        return;
    }

    // Adjust for 0-based index (user enters 1-7, we use 0-6)
    dayChoice--;

    // Prompt user to choose a meal type
    printf("\n--- Select a Meal Type ---\n");
    for (int i = 0; i < 3; i++) {
        printf("%d. %s\n", i + 1, mealTypes[i]);
    }
    printf("Enter meal type (1-3): ");
    if (scanf("%d", &mealChoice) != 1 || mealChoice < 1 || mealChoice > 3) {
        clearInputBuffer();  // Clear the buffer if invalid input
        printf("Invalid meal choice. Please select a valid meal type.\n");
        return;
    }

    // Adjust for 0-based index (user enters 1-3, we use 0-2)
    mealChoice--;

    // Display the menu based on the selected day and meal type
    printf("\n--- Menu for %s - %s ---\n", days[dayChoice], mealTypes[mealChoice]);
    for (int i = 0; i < 4; i++) {
        printf("%d. %s\n", i + 1, menu[dayChoice][mealChoice][i]);
    }
}

// Function to validate User ID
int isValidUserId(const char* id) {
    if (id == NULL || strlen(id) == 0) {
        return 0; // ID is empty
    }

    // Check if the ID contains only alphanumeric characters (no special characters)
    for (int i = 0; id[i] != '\0'; i++) {
        if (!isalnum(id[i])) {
            return 0; // Invalid character found
        }
    }
    
    // Allow IDs that are non-negative (no zero or negative values)
    if (id[0] == '0') {
        return 0; // IDs starting with zero are invalid
    }

    return 1;
}

// Function to check if balance is a valid whole number
int isValidBalance(int balance) {
    return balance >= 0;
}

// Function to check if User ID is unique
int isUniqueUserId(User* userList, const char* id) {
    User* temp = userList;
    while (temp) {
        if (strcmp(temp->id, id) == 0) {
            return 0; // ID already exists
        }
        temp = temp->next;
    }
    return 1; // ID is unique
}

// Function to add a user (without initial balance)
void addUser(User** userList) {
    User* newUser = (User*)malloc(sizeof(User));
    char userId[20];

    do {
        printf("Enter User ID (alphanumeric, no leading zero): ");
        scanf("%s", userId);

        if (!isValidUserId(userId)) {
            printf("Invalid User ID. Try again.\n");
        } else if (!isUniqueUserId(*userList, userId)) {
            printf("User ID already exists. Please choose a different ID.\n");
        } else {
            strcpy(newUser->id, userId);
            break;
        }
    } while (1);

    getchar(); // Consume newline
    printf("Enter User Name: ");
    fgets(newUser->name, sizeof(newUser->name), stdin);
    newUser->name[strcspn(newUser->name, "\n")] = '\0';

    newUser->balance = 0;  // Initialize balance to 0
    newUser->mealCount = 0;
    newUser->feedback[0] = '\0';
    newUser->next = *userList;
    *userList = newUser;

    printf("User added successfully.\n");
}

// Function to find a user by ID
User* findUserById(User* userList, const char* id) {
    User* temp = userList;
    while (temp) {
        if (strcmp(temp->id, id) == 0) {
            return temp;
        }
        temp = temp->next;
    }
    return NULL;
}

// Function to remove a user
void removeUser(User** userList) {
    char userId[20];
    printf("Enter User ID to remove: ");
    scanf("%s", userId);

    User* temp = *userList;
    User* prev = NULL;

    while (temp && strcmp(temp->id, userId) != 0) {
        prev = temp;
        temp = temp->next;
    }

    if (!temp) {
        printf("User not found.\n");
        return;
    }

    if (prev) {
        prev->next = temp->next;
    } else {
        *userList = temp->next;
    }

    free(temp);
    printf("User removed successfully.\n");
}

// Function to record a meal
void recordMeal(User* userList) {
    char userId[20];
    printf("Enter User ID to record meal: ");
    scanf("%s", userId);

    User* user = findUserById(userList, userId);
    if (!user) {
        printf("User not found.\n");
        return;
    }

    if (user->mealCount == 0) {
        user->mealCount++;
        printf("First meal recorded for %s. No charges.\n", user->name);
    } else {
        int mealCharge = 50;  // Assuming meal charge is 50 units
        user->balance += mealCharge; // Add balance if it's the second or more meal
        user->mealCount++;
        printf("Meal recorded for %s. Charge of 50 units added to balance.\n", user->name);
    }
}

// Function to display users
void displayUsers(User* userList) {
    if (!userList) {
        printf("No users to display.\n");
        return;
    }

    printf("\n--- User List ---\n");
    User* temp = userList;
    while (temp) {
        printf("ID: %s, Name: %s, Balance: %d, Meals: %d\n",
               temp->id, temp->name, temp->balance, temp->mealCount);
        temp = temp->next;
    }
}

// Function to display non-eaters
void displayNonEaters(User* userList) {
    if (!userList) {
        printf("No users to display.\n");
        return;
    }

    printf("\n--- Non-Eaters ---\n");
    User* temp = userList;
    int found = 0;
    while (temp) {
        if (temp->mealCount == 0) {
            printf("ID: %s, Name: %s\n", temp->id, temp->name);
            found = 1;
        }
        temp = temp->next;
    }

    if (!found) {
        printf("All users have recorded meals.\n");
    }
}

// Function to generate reports
void generateReports(User* userList) {
    if (!userList) {
        printf("No data to generate reports.\n");
        return;
    }

    int totalMeals = 0;
    int totalRevenue = 0;
    int totalPlates = 0;

    printf("\n--- Report ---\n");
    printf("| ID        | Name               | Meals | Revenue | Plates |\n");
    printf("|-----------|--------------------|-------|---------|--------|\n");

    User* temp = userList;
    while (temp) {
        if (temp->mealCount > 0) {
            totalMeals++;
            totalRevenue += temp->balance;
            totalPlates += temp->mealCount;

            printf("| %-9s | %-18s | %-5d | %-7d | %-6d |\n", 
                   temp->id, temp->name, temp->mealCount, temp->balance, temp->mealCount);
        }
        temp = temp->next;
    }

    printf("\nTotal Meals: %d\n", totalMeals);
    printf("Total Revenue: %d\n", totalRevenue);
    printf("Total Plates Consumed: %d\n", totalPlates);
}

// Function to add feedback
void addFeedback(Feedback** feedbackList) {
    Feedback* newFeedback = (Feedback*)malloc(sizeof(Feedback));
    printf("Enter your feedback: ");
    getchar(); // Consume newline left by previous input
    fgets(newFeedback->message, sizeof(newFeedback->message), stdin);
    newFeedback->message[strcspn(newFeedback->message, "\n")] = '\0';
    
    newFeedback->next = *feedbackList;
    *feedbackList = newFeedback;

    printf("Feedback added successfully.\n");
}

// Function to view feedback
void viewFeedback(Feedback* feedbackList) {
    if (!feedbackList) {
        printf("No feedback available.\n");
        return;
    }

    printf("\n--- Feedback ---\n");
    Feedback* temp = feedbackList;
    while (temp) {
        printf("%s\n", temp->message);
        temp = temp->next;
    }
}

/*Output:

--- Mess Management System ---
1. Add User
2. Remove User
3. Record Meal
4. Display Users
5. Display Non-Eaters
6. Generate Reports
7. Add Feedback
8. View Feedback
9. Exit
Enter choice: 1
Enter User ID (alphanumeric, no leading zero): A1
Enter User Name: Rohan
User added successfully.

--- Mess Management System ---
1. Add User
2. Remove User
3. Record Meal
4. Display Users
5. Display Non-Eaters
6. Generate Reports
7. Add Feedback
8. View Feedback
9. Exit
Enter choice: 1
Enter User ID (alphanumeric, no leading zero): 0
Invalid User ID. Try again.
Enter User ID (alphanumeric, no leading zero): -1
Invalid User ID. Try again.
Enter User ID (alphanumeric, no leading zero): B2
Enter User Name: Riya
User added successfully.

--- Mess Management System ---
1. Add User
2. Remove User
3. Record Meal
4. Display Users
5. Display Non-Eaters
6. Generate Reports
7. Add Feedback
8. View Feedback
9. Exit
Enter choice: 1
Enter User ID (alphanumeric, no leading zero): A1
User ID already exists. Please choose a different ID.
Enter User ID (alphanumeric, no leading zero): C3
Enter User Name: Siddhesh
User added successfully.

--- Mess Management System ---
1. Add User
2. Remove User
3. Record Meal
4. Display Users
5. Display Non-Eaters
6. Generate Reports
7. Add Feedback
8. View Feedback
9. Exit
Enter choice: 1
Enter User ID (alphanumeric, no leading zero): D4
Enter User Name: Ruhi
User added successfully.

--- Mess Management System ---
1. Add User
2. Remove User
3. Record Meal
4. Display Users
5. Display Non-Eaters
6. Generate Reports
7. Add Feedback
8. View Feedback
9. Exit
Enter choice: 2
Enter User ID to remove: A1
User removed successfully.

--- Mess Management System ---
1. Add User
2. Remove User
3. Record Meal
4. Display Users
5. Display Non-Eaters
6. Generate Reports
7. Add Feedback
8. View Feedback
9. Exit
Enter choice: 4

--- User List ---
ID: D4, Name: Ruhi, Balance: 0, Meals: 0
ID: C3, Name: Siddhesh, Balance: 0, Meals: 0
ID: B2, Name: Riya, Balance: 0, Meals: 0

--- Mess Management System ---
1. Add User
2. Remove User
3. Record Meal
4. Display Users
5. Display Non-Eaters
6. Generate Reports
7. Add Feedback
8. View Feedback
9. Exit
Enter choice: 3
Enter User ID to record meal: B2
First meal recorded for Riya. No charges.

--- Mess Management System ---
1. Add User
2. Remove User
3. Record Meal
4. Display Users
5. Display Non-Eaters
6. Generate Reports
7. Add Feedback
8. View Feedback
9. Exit
Enter choice: 3
Enter User ID to record meal: A1
User not found.

--- Mess Management System ---
1. Add User
2. Remove User
3. Record Meal
4. Display Users
5. Display Non-Eaters
6. Generate Reports
7. Add Feedback
8. View Feedback
9. Exit
Enter choice: 3
Enter User ID to record meal: C3
Meal recorded for Siddhesh. Charge of 50 units added to balance.

--- Mess Management System ---
1. Add User
2. Remove User
3. Record Meal
4. Display Users
5. Display Non-Eaters
6. Generate Reports
7. Add Feedback
8. View Feedback
9. Exit
Enter choice: 5

--- Non-Eaters ---
ID: D4, Name: Ruhi

--- Mess Management System ---
1. Add User
2. Remove User
3. Record Meal
4. Display Users
5. Display Non-Eaters
6. Generate Reports
7. Add Feedback
8. View Feedback
9. Exit
Enter choice: 6

--- Report ---
| ID        | Name               | Meals | Revenue | Plates |
|-----------|--------------------|-------|---------|--------|
| C3        | Siddhesh           | 2     | 50      | 2      |
| B2        | Riya               | 1     | 0       | 1      |

Total Meals: 2
Total Revenue: 50
Total Plates Consumed: 3

--- Mess Management System ---
1. Add User
2. Remove User
3. Record Meal
4. Display Users
5. Display Non-Eaters
6. Generate Reports
7. Add Feedback
8. View Feedback
9. Exit
Enter choice: 7
Enter your feedback: Nice Meal  
Feedback added successfully.

--- Mess Management System ---
1. Add User
2. Remove User
3. Record Meal
4. Display Users
5. Display Non-Eaters
6. Generate Reports
7. Add Feedback
8. View Feedback
9. Exit
Enter choice: 8

--- Feedback ---
Nice Meal 

--- Mess Management System ---
1. Add User
2. Remove User
3. Record Meal
4. Display Users
5. Display Non-Eaters
6. Generate Reports
7. Add Feedback
8. View Feedback
9. Exit
Enter choice: 9
Exiting...
*/
