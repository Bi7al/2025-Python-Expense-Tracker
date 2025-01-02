import datetime;

print("""Hello to Expense Tracker""")
print("-------------------------------")
expenses = [];
Expense = {
    "title":"",
    "cost":0.0,
    "date": datetime,
    "desc":""
}
def add_new_expense():
    Expense["title"] = input("Enter expense title: ");
    Expense["cost"]= input("Enter Cost : ");
    Expense["desc"]=input("Enter Description : ");
    Expense["date"]= datetime.datetime.now();
    expenses.append(Expense.copy());
add_new_expense();


def print_expenses():
    for i in range(len(expenses)):
        print(f"""Expense Title : {expenses[i]["title"]}   Dated : {str(expenses[i]["date"].date())}\n
Cost : {expenses[i]["cost"]}\nExpense Description : {expenses[i]["desc"]}""")
print_expenses();