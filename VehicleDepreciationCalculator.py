def takeInputs():
    while True:
        try:
            cost = float(input("Enter Initial vehicle cost: $"))
            if cost == 0:
                print("\nThank you for using the depreciation schedule!")
                exit()
            break
        except ValueError:
            print("Invalid cost")

    while True:
        try:
            years = int(input("Enter number of years for the schedule: "))
            break
        except ValueError:
            print("Invalid number of years")

    while True:
        try:
            vehicle_type = input("Enter vehicle type (sedan or SUV): ").lower()
            if vehicle_type not in ["sedan", "suv"]:
                raise ValueError()
            break
        except ValueError:
            print("Invalid vehicle type")

    return cost, years, vehicle_type


def depSchedule(cost, years, vehicle_type):
    if vehicle_type == "sedan":
        rate = 0.10
    else:
        rate = 0.11

    depreciation_amounts = []
    current_values = []
    total_depreciation = 0

    for year in range(1, years + 1):
        depreciation = round(cost * rate, 2)
        current_value = cost - depreciation

        depreciation_amounts.append(depreciation)
        current_values.append(current_value)
        total_depreciation += depreciation

        cost = current_value

    return depreciation_amounts, current_values, total_depreciation


def main():
    while True:
        cost, years, vehicle_type = takeInputs()
        depreciation_amounts, current_values, total_depreciation = depSchedule(cost, years, vehicle_type)

        print("\nYear\tDepreciation Amount\tCurrent value of vehicle")
        for year, depreciation, current_value in zip(range(1, years + 1), depreciation_amounts, current_values):
            print("{0:2d}\t\t{1:17.2f}\t{2:22.2f}".format(year, depreciation, current_value))
        if vehicle_type == "sedan":
            rate = 0.10
        else:
            rate = 0.11

        print("Vehicle depreciation rate: {0:.2%}".format(rate))
        print("Total Depreciation at the end of the schedule: ${0:,.2f}\n".format(total_depreciation))


main()