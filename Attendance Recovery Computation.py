total_classes = int(input("Enter total classes conducted: "))
attended_classes = int(input("Enter classes attended: "))
target = float(input("Enter target attendance percentage: "))

if (total_classes <= 0 or attended_classes < 0
        or attended_classes > total_classes
        or target < 0 or target > 100):

    print("Invalid input. Please enter valid values.")

else:
    current = attended_classes / total_classes * 100

    print(f"\nCurrent attendance: {current:.2f}%")

    if current >= target:
        print("Target already achieved.")
        print("Additional classes required: 0")

    else:
        # Scenario 1: Attend every future class
        future = 0
        a1 = attended_classes
        t1 = total_classes

        if target == 100:
            scenario1 = -1
        else:
            while a1 / t1 * 100 < target and future < 100000:
                a1 += 1
                t1 += 1
                future += 1

            scenario1 = future if a1 / t1 * 100 >= target else -1

        # Scenario 2: Attend 4 out of every 5 classes
        future = 0
        a2 = attended_classes
        t2 = total_classes

        if target > 80:
            scenario2 = -1
        else:
            while a2 / t2 * 100 < target and future < 100000:
                future += 1
                t2 += 1

                if future % 5 != 0:
                    a2 += 1

            scenario2 = future if a2 / t2 * 100 >= target else -1

        print("\nScenario 1: Attend every class")
        if scenario1 == -1:
            print("Target cannot be reached in this scenario.")
        else:
            print("Additional classes required:", scenario1)

        print("\nScenario 2: Attend 4 out of 5 classes")
        if scenario2 == -1:
            print("Target cannot be reached in this scenario.")
        else:
            print("Additional classes required:", scenario2)