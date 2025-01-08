#Table with title of rows

#row with names of expenses(string), row for interger(number), total for all expenses (number add together)

  #expense tracker

# An app that tracks and categorizes expenses, storing data in a CSV or SQLite database.
# Skills: File handling or databases, data analysis

list_expense = []


def add_expense():
  users = input("Enter your expense here. ").lower()
  list_expense.append(users)
  
  
  
def Delete_expense():
  users = input("Which expense do you want to delete? ").lower()
  if users in list_expense:
    list_expense.pop(users)
  else:
    print("Expense not found")
    
    
while True:  
  print("Expense Tracker")
  users = int(input("1.Add expense \n2. Delete expense \n3. Show List of expenses "))
  if users == 1:
    add_expense()
  elif users == 2:
    Delete_expense()
  elif users == 3:
    print(list_expense)
  
  