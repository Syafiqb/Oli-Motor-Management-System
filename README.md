# **Motor Oil Management System**

This motorcycle oil shop management system is designed to manage motor oil data, including viewing the oil list, adding, deleting, updating, and sorting by stock or price. The program has features that make it easier for admins to manage oil data.

## **Features**

### **READ Submenu**
- **Display All Oil List**: Displays all available oil data in table format.
- **Search Oil by Unique ID**: Searches for oil based on the unique code entered by the user.
- **Sort Oil Stock**: Sorts the oil list by stock (from lowest to highest or vice versa).
- **Sort Oil Price**: Sorts the oil list by price (from lowest to highest or vice versa).

### **CREATE Submenu**
- **Add Oil Data**: Adds new oil data to the list. Users are required to enter the oil name, stock, price, and oil category (Sport/Regular).

### **DELETE Submenu**
- **Delete Oil Data**: Deletes oil data based on the unique code entered by the user.

### **UPDATE Submenu**
- **Update Oil Stock**: Updates oil stock based on the unique code entered by the user.
- **Update Oil Price**: Updates oil price based on the unique code entered by the user.

## **Program Flow**

### **Main Menu**
1. **Display Oil List**: Displays all available oil data.
2. **Add Oil Data**: Adds new oil data to the list.
3. **Delete Oil Data**: Deletes oil data based on a unique code.
4. **Update Oil Data**: Updates oil stock or price.
5. **Exit Program**: Exits the program.

### **Submenu**
- Each submenu has an option to return to the main menu or continue with other operations.
- Every change (add, delete, update) requires user confirmation.

## **Technology & Library**

- **Python**: Programming language used.
- **PrettyTable**: Library for displaying data in table format.

## **How to Run**

1. Ensure Python is installed on your system.
2. Install the `PrettyTable` library if not already installed using the command:
   ```bash
   pip install prettytable
   ```

