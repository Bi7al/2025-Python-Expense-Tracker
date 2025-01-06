import datetime;


expenses = [];

def add_new_expense():
    Expense = {
    "title":input("Enter expense title: "),
    "cost":input("Enter Cost : "),
    "date": datetime.datetime.now(),
    "desc":input("Enter Description : ")
    }
    expenses.append(Expense);
    Expense={};
    print("Expense Added Successfully!!\n")
# End of Add new Expense Function    
    
    

def print_expenses():
    for i in range(len(expenses)):
        print(f"""
Expense Title : {expenses[i]["title"]}   Dated : {str(expenses[i]["date"].date())}
Cost : {expenses[i]["cost"]}
Expense Description : {expenses[i]["desc"]}\n""")
        
# End of Print Function        
        

continue_loop = True;
print("""Hello to Expense Tracker""");
print("-------------------------------");
while(continue_loop):
    print("""1. Add a New Expense
2. View Expenses
3. Exit""");
    choice = int(input("Enter your choice: "));
    if(choice==1):
        add_new_expense();
    elif(choice==2):
        print_expenses();
    elif(choice==3):
        exit();
    else:
        print("Invalid Input");


