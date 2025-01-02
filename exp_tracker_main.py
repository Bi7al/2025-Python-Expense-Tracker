import datetime;

print("""Hello to Expense Tracker""")
print("-------------------------------")
expenses = [];
Expense = {
    "title":"",
    "cost":0.0,
    "date":"",
    "desc":""
}
def add_new_expense():
    Expense["title"] = input("Enter expense title: ");
    Expense["cost"]= input("Enter Cost : ");
    Expense["desc"]=input("Enter Description : ");
    Expense["date"]= datetime.datetime.now();
    expenses.append(Expense.copy());
add_new_expense();
print(expenses);
