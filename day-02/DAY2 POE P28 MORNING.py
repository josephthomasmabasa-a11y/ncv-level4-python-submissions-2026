# IPO
# Input: Customer's name, facility code (squa / swim / gym / wei), number of hours used
# Process: Determine hourly rate from facility code,
#          Calculate amount due before VAT = rate * hours,
#          Calculate final amount = amount due + 14% VAT
# Output: Display customer's name and final amount payable with R prefix and two decimal places

def amount_due(facility_code, hours):
    if facility_code == "squa":
        rate = 13
    elif facility_code == "swim":
        rate = 12
    elif facility_code == "gym":
        rate = 11
    elif facility_code == "wei":
        rate = 8

    amount = rate * hours
    return amount

def final_amount_due(amount):
    final = amount * 1.14
    return final

def display(name, final_amount):
    print(name, "-> R", format(final_amount, ".2f"))

def process_payment():
    name = input("Enter customer's name: ")
    facility_code = input("Enter facility code (squa/swim/gym/wei): ")
    hours = float(input("Enter number of hours: "))

    amount = amount_due(facility_code, hours)
    final = final_amount_due(amount)
    display(name, final)

process_payment()