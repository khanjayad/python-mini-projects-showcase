print("Welcome to the Rent Calculator!")
print("-" * 30)

try:
    rent = int(input("Enter your hostel/flat rent = "))
    food = int(input("Enter the amount of food ordered = "))
    electricity_spend = int(input("Enter the total of electricity spend (in units) = "))
    charge_per_unit = int(input("Enter the charge per unit = "))
    persons = int(input("Enter the number of persons living in room/flat = "))

    if persons <= 0:
        print("Number of persons must be greater than 0.")
        exit()

    total_bill = electricity_spend * charge_per_unit
    rent_per_person = rent // persons
    food_per_person = food // persons
    electricity_per_person = total_bill // persons
    total_per_person = rent_per_person + food_per_person + electricity_per_person

    print("\nBreakdown per person:")
    print(f"Rent: {rent_per_person}")
    print(f"Food: {food_per_person}")
    print(f"Electricity: {electricity_per_person}")
    print(f"Total Payable: {total_per_person}")
except ValueError:
    print("Please enter valid numbers.")
