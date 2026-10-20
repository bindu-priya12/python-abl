
# Library Borrowing and Fine Reconciliation

# Each tuple contains:
# (Book ID, Book Title, Days Borrowed, Returned)

records = [
    (101, "Python Basics", 10, "Yes"),
    (102, "Data Science", 5, "Yes"),
    (103, "Artificial Intelligence", 12, "No"),
    (104, "Web Development", 8, "Yes"),
    (105, "Machine Learning", 6, "No")
]

allowed_days = 7
fine_per_day = 5
total_fine = 0

print("LIBRARY BORROWING AND FINE REPORT")
print("-" * 65)

for record in records:
    book_id, title, days, returned = record

    overdue_days = max(0, days - allowed_days)
    fine = overdue_days * fine_per_day
    total_fine += fine

    if returned == "Yes":
        availability = "Available"
    else:
        availability = "Not Available"

    print("Book ID:", book_id)
    print("Book Title:", title)
    print("Days Borrowed:", days)
    print("Overdue Days:", overdue_days)
    print("Fine: Rs.", fine)
    print("Availability:", availability)
    print("-" * 65)

print("Total Fine: Rs.", total_fine)
