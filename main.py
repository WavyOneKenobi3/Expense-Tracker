#Table with title of rows

#row with names of expenses(string), row for interger(number), total for all expenses (number add together)

  #expense tracker

# An app that tracks and categorizes expenses, storing data in a CSV or SQLite database.
# Skills: File handling or databases, data analysis

list_expense = {}


def add_expense():
  key = input("Enter your expense here. ").lower()
  value = input("Amount of the expense")
  list_expense.update({key: value})
  
  
  
  
def Delete_expense():
  delete_bill = input("which expense do you want to delete? ").lower()
  if delete_bill in list_expense:
    del list_expense[delete_bill]
  else:
    print("Expense not found")
    
    
while True:
  try:  
    print("Expense Tracker")
    users = int(input("1.Add expense \n2. Delete expense \n3. Show List of expenses \n "))
    if users == 1:
      add_expense()
    elif users == 2:
      Delete_expense()
    elif users == 3:
      print(list_expense)
    else:
      print("Your selection is not an option")
  except ValueError:
    print("Invalid entry")
  