
# Weekly Electricity Consumption Matrix

days = [
    "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday", "Sunday"
]

appliances = ["Fan", "Refrigerator", "Air Conditioner"]

# Electricity consumption in kWh
# Each row represents one day
# Each column represents one appliance

consumption = [
    [2, 3, 6],
    [2, 4, 5],
    [1, 3, 7],
    [2, 4, 6],
    [2, 3, 5],
    [3, 4, 7],
    [2, 3, 6]
]

daily_limit = 10
weekly_limit = 35

print("DAILY ELECTRICITY CONSUMPTION")

# Calculate daily totals
for i in range(len(days)):
    daily_total = 0

    for j in range(len(appliances)):
        daily_total += consumption[i][j]

    print(days[i], ":", daily_total, "kWh")

    if daily_total > daily_limit:
        print("Warning: Daily limit exceeded!")
    else:
        print("Daily consumption is within the limit.")

print("\nAPPLIANCE-WISE WEEKLY CONSUMPTION")

# Calculate appliance-wise totals
for j in range(len(appliances)):
    appliance_total = 0

    for i in range(len(days)):
        appliance_total += consumption[i][j]

    print(appliances[j], ":", appliance_total, "kWh")

    if appliance_total > weekly_limit:
        print("Warning: Weekly appliance limit exceeded!")
    else:
        print("Appliance consumption is within the limit.")
