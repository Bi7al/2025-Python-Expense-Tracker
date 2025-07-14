from datetime import datetime
import json
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
def read_json():
    """()-> expenses:list
    Returns list of expenses after reading them from a json file"""
    with open('exp_data.json','r') as fp:
       expenses= json.load(fp)
       return expenses
#end  
    


def save_json(expenses):
    """(expenses)->none
    Recieves a list of expenses and saves them to a JSON file"""
    with open('exp_data.json','w') as fp:
       json.dump(expenses,fp,indent=3)
#end

def add_expense(expenses:list):
    """(expenses:List)->none
    Create a new expense dict and appends it to the expenses list"""
    
    amount=input("Enter Amount:")
    category=input('Enter Category( Food, Travel, Entertainment, Work and Misc):').lower()
    date_str=input('Enter Date (YY-MM-DD):')
    
    new_expense={
        'exp_amount' :int(amount),
        'exp_category':category,
        'exp_date':date_str
    }
    expenses.append(new_expense)
    save_json(expenses)
#end

def view_exp(expenses:list):
    """(expenses:list)->none
    Recieves a list of dictionaries with expenses as dictionary and prints Expense"""
    
    for expense in expenses:
        print("Expense----------------")
        print(f"""\tAmount: {expense['exp_amount']}""")
        print(f"""\tCategory: {expense['exp_category'].capitalize()}""")
        print(f"""\tDated: {expense['exp_date']}""")
#end   

def filter_exp(expenses):
    """(expenses)->none
    Prints expenses based on category filter"""
    category= input('Enter Category( Food, Travel, Entertainment, Work and Misc):').lower()
    
    #Assumption : User Enters a valid input
    filtered = [expense for expense in expenses if expense['exp_category']==category]
    #Hands over the Printing Responsibility to view_exp()
    view_exp(filtered)
#end

def calc_total(expenses):
    """(expenses:list)->none
    Calculates Total Expenses and diplays it. Also Displays Percentages"""  
    categories=['food','travel','entertainment','work','misc']
    dict_obj={key:sum([expense['exp_amount'] for expense in expenses if expense['exp_category']==key]) for key in categories}
    total_exp=sum(dict_obj.values())
    print(f"""Total Expenses: {total_exp}""")
    print("Category wise Percentages:")
    for key, val in dict_obj.items():
        percentage = (val / total_exp) * 100 if total_exp else 0
        print(f"{key.capitalize():<15}: {percentage:<6.2f}%")
#end
    
    
        
    
      
    
    

#start
menu="""Welcome----------------
1.Add a new Expense
2.View all expenses
3.Filter Expenses
4.Calculate and Display total expenses
5.Exit
choice:"""

expenses = read_json();




while True:
    
    user_input=input(menu)
    if user_input=='1':
        add_expense(expenses)
    elif user_input=='2':
        view_exp(expenses)
    elif user_input=='3':
        filter_exp(expenses)
    elif user_input=='4':
        calc_total(expenses)
    elif user_input=='5':
        exit()
    else:
        print("Invalid Input")
