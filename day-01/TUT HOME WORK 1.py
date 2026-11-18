# IPO
# Input: Athlete names and times 
#        Thandi 22:30, Sipho 27:15, Lerato 19:45, Pieter 31:05, Naledi 24:50
# Process: 1. Convert mm:ss to seconds
#          2. If seconds <= 1500 (25:00), count as qualified
#          3. Keep the lowest time as the winner
# Output: Each athlete QUALIFIED / NOT QUALIFIED, total qualified, winner

athletes  = [
    ("Thandi", "22:30"),
    ("Sipho", "27:15"),
    ("Lerato", "19:45"),
    ("Pieter", "31:05"),
    ("Naledi", "24:50")
]

total = 0
qualified = 0
winner_name = ""
winner_time = ""
winner_seconds = 0
first = True

for name, time_str in athletes:
    parts = time_str.split(":")
    minutes = int(parts[0])
    seconds = int(parts[1])
    total_seconds = minutes * 60 + seconds
    total = total + 1

    if total_seconds <= 1500:
        qualified = qualified + 1
        print(name, "-", time_str, "-> QUALIFIED")
    else:
        print(name, "-", time_str, "-> NOT QUALIFIED")

    if first or total_seconds < winner_seconds:
        first = False
        winner_seconds = total_seconds
        winner_name = name
        winner_time = time_str

print("----------------------")
print("Qualified:", qualified, "of", total)
print("Winner:", winner_name, "(", winner_time, ")")
  


