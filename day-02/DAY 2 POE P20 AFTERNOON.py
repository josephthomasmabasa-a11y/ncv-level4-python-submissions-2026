# IPO
# Input: Customer name, machine type (A / B / C)
# Process: Generate random minutes (30-180), convert to hours,
#          Amount before VAT = Initial cost + (Hourly rate x Hours),
#          VAT = Amount x 14%, Total = Amount + VAT,
#          Store each total in a list
# Output: Display each customer's minutes, amount, VAT, total
#         and final summary: total, average, highest, lowest, count

import random

def generate_minutes():
    minutes = random.randint(30, 180)
    return minutes

def calc_amount(machine_type, minutes):
    machine_type = machine_type.upper().strip()

    if machine_type == "A":
        initial_cost = 50.00
        hourly_rate = 30.00
    elif machine_type == "B":
        initial_cost = 62.50
        hourly_rate = 36.25
    elif machine_type == "C":
        initial_cost = 74.87
        hourly_rate = 40.50
    else:
        initial_cost = 0
        hourly_rate = 0

    hours = minutes / 60
    amount = initial_cost + (hourly_rate * hours)
    return amount

def calc_total_amount(amount):
    vat = amount * 0.14
    total = amount + vat
    return vat, total

def display_summary(payments):
    # payments is a list of totals
    total_payments = 0
    for amount in payments:
        total_payments = total_payments + amount

    number_of_customers = len(payments)

    if number_of_customers > 0:
        average = total_payments / number_of_customers
    else:
        average = 0

    highest = max(payments) if payments else 0
    lowest = min(payments) if payments else 0

    print("\n========== DAILY SUMMARY ==========")
    print("Number of customers:", number_of_customers)
    print("Total payments for the day: R", format(total_payments, ".2f"))
    print("Average payment: R", format(average, ".2f"))
    print("Highest payment: R", format(highest, ".2f"))
    print("Lowest payment: R", format(lowest, ".2f"))
    print("====================================")

def process_customers():
    payments = []  # list to store each total

    # Ask how many customers - this is the loop
    num_customers = int(input("How many customers today? "))

    for i in range(num_customers):
        print(f"\n--- Customer {i+1} ---")
        name = input("Enter customer name: ")
        machine_type = input("Enter machine type (A / B / C): ")

        minutes = generate_minutes()
        amount = calc_amount(machine_type, minutes)
        vat, total = calc_total_amount(amount)

        payments.append(total)

        print("Minutes used:", minutes)
        print("Amount before VAT: R", format(amount, ".2f"))
        print("VAT (14%): R", format(vat, ".2f"))
        print(name, "-> Total payable: R", format(total, ".2f"))

    display_summary(payments)

# Start the program
process_customers()