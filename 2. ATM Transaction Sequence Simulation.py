
transactions = []

balance = float(input("Enter initial balance: ₹"))

while balance < 0:
    print("Balance cannot be negative.")
    balance = float(input("Enter initial balance: ₹"))

n = int(input("Enter number of transactions: "))

successful = 0
rejected = 0

for i in range(n):
    print("\nTransaction", i + 1)

    t_type = input("Enter type (deposit/withdrawal): ").lower()
    amount = float(input("Enter amount: ₹"))

    if amount <= 0:
        status = "Rejected"
        print("Invalid amount!")

    elif t_type == "deposit":
        balance += amount
        status = "Successful"
        print("Deposit successful.")

    elif t_type == "withdrawal":
        if amount <= balance:
            balance -= amount
            status = "Successful"
            print("Withdrawal successful.")
        else:
            status = "Rejected"
            print("Insufficient balance!")

    else:
        status = "Rejected"
        print("Invalid transaction type!")

    if status == "Successful":
        successful += 1
    else:
        rejected += 1

    transactions.append(
        [t_type, amount, status, balance]
    )

print("\n----- TRANSACTION SUMMARY -----")

for i, transaction in enumerate(transactions, start=1):
    print(
        f"{i}. Type: {transaction[0]}, "
        f"Amount: ₹{transaction[1]:.2f}, "
        f"Status: {transaction[2]}, "
        f"Balance: ₹{transaction[3]:.2f}"
    )

print("\nSuccessful transactions:", successful)
print("Rejected transactions:", rejected)
print(f"Final balance: ₹{balance:.2f}")

