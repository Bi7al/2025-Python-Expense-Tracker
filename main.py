from datetime import datetime

# """
# Personal Expense Tracker - CLI Based (Python Project)

# This is a simple command-line application that allows users to track their personal expenses.
# Users can add new expenses by entering the amount, category, and date (optional).
# All expenses are stored as Python dictionaries and maintained in a list during runtime.

# The data is saved and loaded using JSON (JavaScript Object Notation), which provides
# a clean, structured, and readable way to persist data between sessions.

# Main Features:
# - Add a new expense
# - View all expenses
# - Filter expenses by category or date
# - Calculate and display total expenses
# - Save/load expenses to/from a JSON file

# Core Python concepts used:
# File handling, list operations, list comprehensions, dictionaries, string formatting and the json module.

# """

#Custom Functions

def add_expense(expenses:list):
    """(expenses:List)->none
    Create a new expense dict and appends it to the expenses list"""
    
    amount=input("Enter Amount:")
    category=input('Enter Category( Food, Travel, Entertainment, Work and Misc):')
    date_str=input('Enter Date (YY-MM-DD):')
    date= datetime.strptime(date_str,'%Y-%m-%d')
    new_expense={
        'exp_amount' :amount,
        'exp_category':category,
        'exp_date':date
    }
    print(new_expense) #Test Print
    expenses.append(new_expense)
    print(expenses) #Test Print
#end



    


#start
menu="""Welcome----------------
1.Add a new Expense
2.View all expenses
3.Filter Expenses
4.Calculate and Display total expenses
5.Exit
choice:"""

expenses=[]



while True:
    user_input=input(menu)
    if user_input=='1':
        add_expense(expenses)
    elif user_input=='2':
        pass
    elif user_input=='3':
        pass
    elif user_input=='4':
        pass
    elif user_input=='5':
        exit()
    else:
        print("Invalid Input")
