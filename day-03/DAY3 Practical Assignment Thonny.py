# Name: Mabasa Joseph
# Student Number: Westcol lecturer and TUT student
# Date: 17 November 2026
# Program: Learner Marks Management System
# This program stores learners and their marks,
# and can add, search, update, delete and rank them.

# Question1 - Collections
# Dictionary: unique student number,Names and Marks.
learners = {
    "2024001": {"name": "Thandi", "marks": [65, 72, 58]},
    "2024002": {"name": "Sipho", "marks": [48, 90, 55]},
    "2024003": {"name": "Lerato", "marks": [81, 39, 77]},
    "2024004": {"name": "Dumisani", "marks": [72, 72, 48]},
    "2024005": {"name": "Naledi", "marks": [90, 55, 72]}
}

# List
print(learners["2024001"]["marks"])
print(learners["2024001"]["marks"][0])
print(learners["2024001"]["marks"][-1])
print(learners["2024001"]["marks"][0:2])

# Tuple - a seat must not change, so tuple is right
point = (3, 4)
x, y = point
print(x, y)

# Set - duplicates are removed
codes = {"CS1", "CS2", "CS1", "CS3"}
print(len(codes))
print("CS3" in codes)

# Question2 - First principles
def total_of(values):
    total = 0
    for v in values:
        total = total + v
    return total

def mean_of(values):
    return total_of(values) / len(values)

def average_of(values):
    total = 0
    for v in values:
        total = total + v
    return total / len(values)

def max_of(values):
    best = values[0]
    for v in values:
        if v > best:
            best = v
    return best

def min_of(values):
    smallest = values[0]
    for v in values:
        if v < smallest:
            smallest = v
    return smallest

def range_of(values):
    return max_of(values) - min_of(values)

def above_mean(values):
    result = []
    avg = mean_of(values)
    for v in values:
        if v > avg:
            result.append(v)
    return result

def learner_average(learners, number):
    marks = learners[number]["marks"]
    if len(marks) == 0:
        return None
    return average_of(marks)

# Question3 - Search and mode
def find_first(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1

def find_all(values, target):
    positions = []
    for i in range(len(values)):
        if values[i] == target:
            positions.append(i)
    return positions

def count_of(values, target):
    count = 0
    for v in values:
        if v == target:
            count = count + 1
    return count

def mode_of(values):
    counts = {}
    for v in values:
        if v in counts:
            counts[v] = counts[v] + 1
        else:
            counts[v] = 1
    best = 0
    for v in counts:
        if counts[v] > best:
            best = counts[v]
    modes = []
    for v in counts:
        if counts[v] == best:
            modes.append(v)
    return modes

# Question4 - Sorting
def bubble_sort(values):
    items = values[:]
    n = len(items)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            break
    return items

def selection_sort(values):
    items = values[:]
    for i in range(len(items) - 1):
        smallest = i
        for j in range(i + 1, len(items)):
            if items[j] < items[smallest]:
                smallest = j
        items[i], items[smallest] = items[smallest], items[i]
    return items

# Question6 - Tests
data = []
for x in "65 72 48 90 55 72 48 72".split():
    data.append(int(x))

print("Total  :", total_of(data))
print("Mean   :", mean_of(data))
print("Highest:", max_of(data))
print("Lowest :", min_of(data))
print("First 72 at:", find_first(data, 72))
print("All 72 at  :", find_all(data, 72))
print("Count of 72:", count_of(data, 72))
print("Mode   :", mode_of(data))
print("Mode (tie):", mode_of([1, 2, 2, 3, 3]))
print(bubble_sort(data))
print(selection_sort(data))
print(data)

# Question5 - Register
def is_valid_number(text):
    return text.isdigit() and len(text) == 7

def is_valid_mark(text):
    return text.isdigit() and int(text) <= 100

def show_menu():
    print()
    print("1. Add learner")
    print("2. Add mark")
    print("3. Rename learner")
    print("4. Delete learner")
    print("5. Find by name")
    print("6. Show ranking")
    print("7. Exit")

def ask_number():
    return input("Student number (7 digits): ")

def add_learner(learners, number, name):
    if number in learners:
        return False
    learners[number] = {"name": name, "marks": []}
    return True

def add_mark(learners, number, mark):
    if number not in learners:
        return False
    learners[number]["marks"].append(mark)
    return True

def rename_learner(learners, number, new_name):
    if number not in learners:
        return False
    learners[number]["name"] = new_name
    return True

def delete_learner(learners, number):
    if number not in learners:
        return False
    del learners[number]
    return True

def find_by_name(learners, text):
    matches = []
    for number in learners:
        if text.lower() in learners[number]["name"].lower():
            matches.append(number)
    return matches

def ranking(learners):
    rows = []
    for number in learners:
        avg = learner_average(learners, number)
        if avg is not None:
            rows.append((avg, number))
    n = len(rows)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if rows[j][0] < rows[j + 1][0]:
                rows[j], rows[j + 1] = rows[j + 1], rows[j]
    return rows

def print_ranking(learners):
    rows = ranking(learners)
    if len(rows) == 0:
        print("No marks captured yet.")
        return
    print("Rank  Number    Name          Average")
    for position in range(len(rows)):
        avg = rows[position][0]
        number = rows[position][1]
        name = learners[number]["name"]
        print(f"{position + 1:<6}{number:<10}{name:<14}{avg:>6.1f}")

def main():
    choice = ""
    while choice != "7":
        show_menu()
        choice = input("Choice: ")
        if choice == "1":
            number = ask_number()
            name = input("Name: ")
            if not is_valid_number(number) or name == "":
                print("Invalid number or name.")
            elif add_learner(learners, number, name):
                print("Added.")
            else:
                print("That student number already exists.")
        elif choice == "2":
            number = ask_number()
            text = input("Mark (0-100): ")
            if not is_valid_mark(text):
                print("Invalid mark.")
            elif add_mark(learners, number, int(text)):
                print("Mark added.")
            else:
                print("No such learner.")
        elif choice == "3":
            number = ask_number()
            if rename_learner(learners, number, input("New name: ")):
                print("Renamed.")
            else:
                print("No such learner.")
        elif choice == "4":
            if delete_learner(learners, ask_number()):
                print("Deleted.")
            else:
                print("No such learner.")
        elif choice == "5":
            found = find_by_name(learners, input("Name contains: "))
            if len(found) == 0:
                print("No match.")
            for number in found:
                print(number, learners[number]["name"], learners[number]["marks"])
        elif choice == "6":
            print_ranking(learners)
        elif choice == "7":
            print("Goodbye.")
        else:
            print("Invalid choice. Enter 1 to 7.")

main()