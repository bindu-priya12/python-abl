
# Food Waste Monitoring System

prepared = [100, 120, 110, 130, 100, 150, 120]
served = [95, 100, 105, 110, 92, 130, 100]

limit = 10

total_prepared = 0
total_served = 0
total_waste = 0

print("FOOD WASTE MONITORING SYSTEM")
print("-" * 65)

for i in range(len(prepared)):
    leftover = prepared[i] - served[i]
    waste_percentage = (leftover / prepared[i]) * 100

    print(f"\nDay {i + 1}")
    print("Meals Prepared:", prepared[i])
    print("Meals Served:", served[i])
    print("Meals Left Over:", leftover)
    print(f"Waste Percentage: {waste_percentage:.2f}%")

    if waste_percentage > limit:
        print("Status: Waste limit exceeded!")
    else:
        print("Status: Waste within limit.")

    total_prepared += prepared[i]
    total_served += served[i]
    total_waste += leftover

print("\n" + "-" * 65)
print("WEEKLY SUMMARY")
print("Total Meals Prepared:", total_prepared)
print("Total Meals Served:", total_served)
print("Total Meals Wasted:", total_waste)

weekly_percentage = (total_waste / total_prepared) * 100
print(f"Overall Waste Percentage: {weekly_percentage:.2f}%")
