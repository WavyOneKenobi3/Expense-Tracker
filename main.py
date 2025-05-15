 
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
  
