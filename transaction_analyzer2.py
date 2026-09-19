data = [
  (749.17, "Investment Return"),
  (-11.54, "Utilities"),
  (-247.58, "Online Shopping"),
  (981.17, "Investment Return"),
  (-410.65, "Rent"),
  (310.60, "Rent"),
  (563.70, "Gift"),
  (220.79, "Salary"),
  (-49.85, "Car Maintenance"),
  (308.49, "Salary"),
  (-205.55, "Car Maintenance"),
  (870.64, "Salary"),
  (-881.51, "Utilities"),
  (518.14, "Salary"),
  (-264.66, "Groceries")
]

def analyze_transactions(transactions):
  transactions.sort()
  largest_withdrawal = transactions[0]
  largest_deposit = transactions[-1]
  print(largest_withdrawal)
  print(largest_deposit)
  deposits = [transaction[0] for transaction in transactions if transaction[0] >= 0]
  total_deposited = sum(deposits)
  print(total_deposited)
  if len(deposits) <= 0:
    average = 0
  else:
    average = total_deposited / len(deposits)
  print(average)
  withdrawals = [transaction[0] for transaction in transactions if transaction[0] <= 0]
  total_withdrawals = sum(withdrawals)
  print(total_withdrawals)
  if len(withdrawals) <= 0:
    average_with = 0
  else:
    average_with = total_withdrawals / len(withdrawals)
  print(average_with)

def print_transactions(transactions):
  for transaction in transactions:
    amount = transaction[0]
    statement = transaction[1]
    print(f"${amount} - {statement}")

print_transactions(data)

def print_summary(transactions):
  deposits = [transaction[0] for transaction in transactions if transaction[0] >= 0]
  total_deposited = sum(deposits)
  print(total_deposited)
  withdrawals = [transaction[0] for transaction in transactions if transaction[0] <= 0]
  total_withdrawals = sum(withdrawals)
  print(total_withdrawals)
  balance = total_deposited + total_withdrawals
  print(balance)

while True:
  print("would you like to: ")
  print("print")
  print("analyze")
  print("or stop ? ")
  choice = input()
  if choice == "print":
    print_summary(data)
  elif choice == "analyze":
    analyze_transactions(data)
  elif choice == "stop":
    break
  else:
    print("Invalid choice")
    
 

