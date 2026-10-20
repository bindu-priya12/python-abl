
# Problem No. 28: Repeated Transaction Detection

transaction_ids = []
amounts = []

n = int(input("Enter the number of transactions: "))

# Input transaction details
for i in range(n):
    print("\nTransaction", i + 1)

    tid = input("Enter transaction ID: ")
    amount = float(input("Enter transaction amount: "))

    transaction_ids.append(tid)
    amounts.append(amount)

# Input the amount limit
limit = float(input("\nEnter the amount limit: "))

# Find duplicate transaction IDs
duplicate_ids = []

for tid in transaction_ids:
    if transaction_ids.count(tid) > 1:
        if tid not in duplicate_ids:
            duplicate_ids.append(tid)

print("\n--- Duplicate Transaction IDs ---")

if len(duplicate_ids) == 0:
    print("No duplicate transaction IDs found.")
else:
    for tid in duplicate_ids:
        print(tid)

# Find high-value transactions
print("\n--- High-Value Transactions ---")

found_high = False

for i in range(n):
    if amounts[i] > limit:
        print("ID:", transaction_ids[i],
              "| Amount: Rs.", amounts[i])
        found_high = True

if not found_high:
    print("No high-value transactions found.")

# Find suspicious transactions
print("\n--- Suspicious Transactions ---")

found_suspicious = False

for i in range(n):
    if (transaction_ids[i] in duplicate_ids
            or amounts[i] > limit):
        print("ID:", transaction_ids[i],
              "| Amount: Rs.", amounts[i])
        found_suspicious = True

if not found_suspicious:
    print("No suspicious transactions found.")
