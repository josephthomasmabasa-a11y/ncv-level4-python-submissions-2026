"""PRACTICAL 3: STUDENT ATTENDANCE - JSON file (Thonny)."""
import json

# ============================================================
# STEP 0: CREATE attendance.json FROM YOUR LIST - SO YOU ONLY NEED 1 FILE
# ============================================================
# Your same list M001-M219
learners_data = """M001,Lerato Molefe,3173,3178,Soshanguve
M002,Nomsa Mabena,3614,3680,Atteridgeville
M003,Peter Mthembu,894,959,Ga-Rankuwa
M004,Ayanda Dlamini,1217,1267,Hammanskraal
M005,Sipho Mahlangu,1822,1889,Mamelodi
M006,Naledi Masemola,1585,1659,Soshanguve
M007,Kabelo Nkosi,1007,1083,Atteridgeville
M008,Palesa Maseko,1469,1482,Ga-Rankuwa
M009,Tshepo Ndlovu,1466,1518,Hammanskraal
M010,Thabo Mokoena,1740,1774,Mamelodi
M011,Lerato Molefe,3818,3831,Soshanguve
M012,Nomsa Mabena,3567,3608,Atteridgeville
M013,Peter Mthembu,1674,1676,Ga-Rankuwa
M014,Ayanda Dlamini,2731,2810,Hammanskraal
M015,Sipho Mahlangu,1225,1234,Mamelodi
M016,Naledi Masemola,1229,1243,Soshanguve
M017,Kabelo Nkosi,2621,2679,Atteridgeville
M018,Palesa Maseko,1991,2084,Ga-Rankuwa
M019,Tshepo Ndlovu,701,713,Hammanskraal
M020,Thabo Mokoena,2097,2099,Mamelodi
M021,Lerato Molefe,806,880,Soshanguve
M022,Nomsa Mabena,3381,3435,Atteridgeville
M023,Peter Mthembu,3495,3545,Ga-Rankuwa
M024,Ayanda Dlamini,2203,2287,Hammanskraal
M025,Sipho Mahlangu,1624,1697,Mamelodi
M026,Naledi Masemola,2457,2477,Soshanguve
M027,Kabelo Nkosi,3643,3724,Atteridgeville
M028,Palesa Maseko,2064,2093,Ga-Rankuwa
M029,Tshepo Ndlovu,3573,3642,Hammanskraal
M030,Thabo Mokoena,2761,2854,Mamelodi
M031,Lerato Molefe,841,867,Soshanguve
M032,Nomsa Mabena,1998,2022,Atteridgeville
M033,Peter Mthembu,967,984,Ga-Rankuwa
M034,Ayanda Dlamini,2965,3028,Hammanskraal
M035,Sipho Mahlangu,828,898,Mamelodi
M036,Naledi Masemola,3289,3347,Soshanguve
M037,Kabelo Nkosi,428,486,Atteridgeville
M038,Palesa Maseko,2365,2441,Ga-Rankuwa
M039,Tshepo Ndlovu,890,956,Hammanskraal
M040,Thabo Mokoena,2366,2430,Mamelodi
M041,Lerato Molefe,2423,2470,Soshanguve
M042,Nomsa Mabena,2154,2223,Atteridgeville
M043,Peter Mthembu,3947,3970,Ga-Rankuwa
M044,Ayanda Dlamini,411,442,Hammanskraal
M045,Sipho Mahlangu,774,777,Mamelodi
M046,Naledi Masemola,2308,2356,Soshanguve
M047,Kabelo Nkosi,2250,2264,Atteridgeville
M048,Palesa Maseko,3168,3258,Ga-Rankuwa
M049,Tshepo Ndlovu,3072,3105,Hammanskraal
M050,Thabo Mokoena,925,985,Mamelodi
M051,Lerato Molefe,1562,1619,Soshanguve
M052,Nomsa Mabena,2052,2089,Atteridgeville
M053,Peter Mthembu,3412,3433,Ga-Rankuwa
M054,Ayanda Dlamini,2288,2344,Hammanskraal
M055,Sipho Mahlangu,1633,1672,Mamelodi
M056,Naledi Masemola,3174,3179,Soshanguve
M057,Kabelo Nkosi,716,742,Atteridgeville
M058,Palesa Maseko,1674,1761,Ga-Rankuwa
M059,Tshepo Ndlovu,3480,3533,Hammanskraal
M060,Thabo Mokoena,814,873,Mamelodi
M061,Lerato Molefe,672,731,Soshanguve
M062,Nomsa Mabena,2471,2528,Atteridgeville
M063,Peter Mthembu,3088,3090,Ga-Rankuwa
M064,Ayanda Dlamini,1117,1172,Hammanskraal
M065,Sipho Mahlangu,3058,3093,Mamelodi
M066,Naledi Masemola,708,718,Soshanguve
M067,Kabelo Nkosi,917,938,Atteridgeville
M068,Palesa Maseko,2161,2197,Ga-Rankuwa
M069,Tshepo Ndlovu,2312,2326,Hammanskraal
M070,Thabo Mokoena,1230,1309,Mamelodi
M071,Lerato Molefe,2323,2410,Soshanguve
M072,Nomsa Mabena,3721,3729,Atteridgeville
M073,Peter Mthembu,2156,2239,Ga-Rankuwa
M074,Ayanda Dlamini,2996,3015,Hammanskraal
M075,Sipho Mahlangu,435,484,Mamelodi
M076,Naledi Masemola,2942,3025,Soshanguve
M077,Kabelo Nkosi,1586,1667,Atteridgeville
M078,Palesa Maseko,561,633,Ga-Rankuwa
M079,Tshepo Ndlovu,2635,2710,Hammanskraal
M080,Thabo Mokoena,1860,1892,Mamelodi
M081,Lerato Molefe,1262,1295,Soshanguve
M082,Nomsa Mabena,2485,2525,Atteridgeville
M083,Peter Mthembu,652,655,Ga-Rankuwa
M084,Ayanda Dlamini,3572,3607,Hammanskraal
M085,Sipho Mahlangu,3077,3103,Mamelodi
M086,Naledi Masemola,662,687,Soshanguve
M087,Kabelo Nkosi,1603,1670,Atteridgeville
M088,Palesa Maseko,2308,2372,Ga-Rankuwa
M089,Tshepo Ndlovu,956,997,Hammanskraal
M090,Thabo Mokoena,3693,3758,Mamelodi
M091,Lerato Molefe,3691,3724,Soshanguve
M092,Nomsa Mabena,2702,2793,Atteridgeville
M093,Peter Mthembu,3369,3463,Ga-Rankuwa
M094,Ayanda Dlamini,1653,1735,Hammanskraal
M095,Sipho Mahlangu,3455,3542,Mamelodi
M096,Naledi Masemola,2565,2601,Soshanguve
M097,Kabelo Nkosi,3045,3109,Atteridgeville
M098,Palesa Maseko,2731,2785,Ga-Rankuwa
M099,Tshepo Ndlovu,3783,3844,Hammanskraal
M100,Thabo Mokoena,655,683,Mamelodi
M101,Lerato Molefe,1032,1037,Soshanguve
M102,Nomsa Mabena,2277,2291,Atteridgeville
M103,Peter Mthembu,2501,2576,Ga-Rankuwa
M104,Ayanda Dlamini,3957,3969,Hammanskraal
M105,Sipho Mahlangu,1467,1558,Mamelodi
M106,Naledi Masemola,2312,2401,Soshanguve
M107,Kabelo Nkosi,1953,2040,Atteridgeville
M108,Palesa Maseko,1728,1770,Ga-Rankuwa
M109,Tshepo Ndlovu,1913,1936,Hammanskraal
M110,Thabo Mokoena,2223,2265,Mamelodi
M111,Lerato Molefe,3349,3361,Soshanguve
M112,Nomsa Mabena,3004,3089,Atteridgeville
M113,Peter Mthembu,3100,3167,Ga-Rankuwa
M114,Ayanda Dlamini,2242,2294,Hammanskraal
M115,Sipho Mahlangu,2928,2933,Mamelodi
M116,Naledi Masemola,3970,4016,Soshanguve
M117,Kabelo Nkosi,783,823,Atteridgeville
M118,Palesa Maseko,2189,2235,Ga-Rankuwa
M119,Tshepo Ndlovu,2275,2350,Hammanskraal
M120,Thabo Mokoena,3394,3440,Mamelodi
M121,Lerato Molefe,584,621,Soshanguve
M122,Nomsa Mabena,1473,1508,Atteridgeville
M123,Peter Mthembu,761,789,Ga-Rankuwa
M124,Ayanda Dlamini,2005,2009,Hammanskraal
M125,Sipho Mahlangu,1097,1118,Mamelodi
M126,Naledi Masemola,2324,2408,Soshanguve
M127,Kabelo Nkosi,3328,3398,Atteridgeville
M128,Palesa Maseko,837,927,Ga-Rankuwa
M129,Tshepo Ndlovu,2843,2908,Hammanskraal
M130,Thabo Mokoena,772,776,Mamelodi
M131,Lerato Molefe,2806,2861,Soshanguve
M132,Nomsa Mabena,591,682,Atteridgeville
M133,Peter Mthembu,3195,3212,Ga-Rankuwa
M134,Ayanda Dlamini,2911,2952,Hammanskraal
M135,Sipho Mahlangu,1404,1473,Mamelodi
M136,Naledi Masemola,3392,3461,Soshanguve
M137,Kabelo Nkosi,3823,3827,Atteridgeville
M138,Palesa Maseko,1535,1559,Ga-Rankuwa
M139,Tshepo Ndlovu,1007,1038,Hammanskraal
M140,Thabo Mokoena,1584,1599,Mamelodi
M141,Lerato Molefe,2814,2870,Soshanguve
M142,Nomsa Mabena,925,934,Atteridgeville
M143,Peter Mthembu,3245,3302,Ga-Rankuwa
M144,Ayanda Dlamini,1672,1742,Hammanskraal
M145,Sipho Mahlangu,2061,2135,Mamelodi
M146,Naledi Masemola,1320,1365,Soshanguve
M147,Kabelo Nkosi,3426,3439,Atteridgeville
M148,Palesa Maseko,3172,3202,Ga-Rankuwa
M149,Tshepo Ndlovu,1458,1475,Hammanskraal
M150,Thabo Mokoena,1818,1876,Mamelodi
M151,Lerato Molefe,2689,2717,Soshanguve
M152,Nomsa Mabena,2673,2730,Atteridgeville
M153,Peter Mthembu,1645,1652,Ga-Rankuwa
M154,Ayanda Dlamini,2789,2845,Hammanskraal
M155,Sipho Mahlangu,905,929,Mamelodi
M156,Naledi Masemola,2917,2925,Soshanguve
M157,Kabelo Nkosi,2420,2436,Atteridgeville
M158,Palesa Maseko,1983,2049,Ga-Rankuwa
M159,Tshepo Ndlovu,1550,1612,Hammanskraal
M160,Thabo Mokoena,1834,1891,Mamelodi
M161,Lerato Molefe,603,670,Soshanguve
M162,Nomsa Mabena,2143,2146,Atteridgeville
M163,Peter Mthembu,2760,2788,Ga-Rankuwa
M164,Ayanda Dlamini,3108,3147,Hammanskraal
M165,Sipho Mahlangu,2680,2711,Mamelodi
M166,Naledi Masemola,821,872,Soshanguve
M167,Kabelo Nkosi,2108,2189,Atteridgeville
M168,Palesa Maseko,958,1046,Ga-Rankuwa
M169,Tshepo Ndlovu,2587,2616,Hammanskraal
M170,Thabo Mokoena,1039,1097,Mamelodi
M171,Lerato Molefe,1162,1253,Soshanguve
M172,Nomsa Mabena,2890,2951,Atteridgeville
M173,Peter Mthembu,752,787,Ga-Rankuwa
M174,Ayanda Dlamini,3499,3550,Hammanskraal
M175,Sipho Mahlangu,2197,2272,Mamelodi
M176,Naledi Masemola,663,736,Soshanguve
M177,Kabelo Nkosi,3160,3160,Atteridgeville
M178,Palesa Maseko,3424,3454,Ga-Rankuwa
M179,Tshepo Ndlovu,3846,3856,Hammanskraal
M180,Thabo Mokoena,1511,1542,Mamelodi
M181,Lerato Molefe,2391,2411,Soshanguve
M182,Nomsa Mabena,3436,3502,Atteridgeville
M183,Peter Mthembu,2025,2058,Ga-Rankuwa
M184,Ayanda Dlamini,2303,2357,Hammanskraal
M185,Sipho Mahlangu,3694,3696,Mamelodi
M186,Naledi Masemola,971,983,Soshanguve
M187,Kabelo Nkosi,1107,1161,Atteridgeville
M188,Palesa Maseko,3709,3711,Ga-Rankuwa
M189,Tshepo Ndlovu,1501,1579,Hammanskraal
M190,Thabo Mokoena,3612,3674,Mamelodi
M191,Lerato Molefe,2850,2892,Soshanguve
M192,Nomsa Mabena,1420,1459,Atteridgeville
M193,Peter Mthembu,1138,1147,Ga-Rankuwa
M194,Ayanda Dlamini,2629,2667,Hammanskraal
M195,Sipho Mahlangu,506,521,Mamelodi
M196,Naledi Masemola,696,702,Soshanguve
M197,Kabelo Nkosi,3133,3144,Atteridgeville
M198,Palesa Maseko,2587,2645,Ga-Rankuwa
M199,Tshepo Ndlovu,658,662,Hammanskraal
M200,Thabo Mokoena,783,831,Mamelodi
M201,Lerato Molefe,3219,3281,Soshanguve
M202,Nomsa Mabena,1671,1718,Atteridgeville
M203,Peter Mthembu,1778,1813,Ga-Rankuwa
M204,Ayanda Dlamini,1008,1023,Hammanskraal
M205,Sipho Mahlangu,2894,2901,Mamelodi
M206,Naledi Masemola,578,624,Soshanguve
M207,Kabelo Nkosi,1136,1150,Atteridgeville
M208,Palesa Maseko,3020,3063,Ga-Rankuwa
M209,Tshepo Ndlovu,2402,2447,Hammanskraal
M210,Thabo Mokoena,1432,1523,Mamelodi"""

# Convert your list to JSON attendance records
# sessions_total = 20 for everyone
# sessions_attended and late_submissions are made from your readings
# so every student gets a different, realistic attendance
attendance_list = []
for line in learners_data.split("\n"):
    line = line.strip()
    if line == "":
        continue
    parts = line.split(",")
    if len(parts) != 5:
        continue
    sid = parts[0].strip()
    name = parts[1].strip()
    prev = parts[2].strip()
    curr = parts[3].strip()
    if not prev.isdigit() or not curr.isdigit():
        continue
    usage = int(curr) - int(prev)
    if usage < 0:
        continue
    # Make attendance from usage - same for everyone, no random
    attended = 20 - (usage % 9)  # 12 to 20
    late = usage % 6  # 0 to 5
    attendance_list.append({
        "student_id": sid,
        "name": name,
        "sessions_total": 20,
        "sessions_attended": attended,
        "late_submissions": late
    })

# Add a few BAD records to test your validation - like in Practical 1
attendance_list.append({"student_id": "M001", "name": "Duplicate Meter", "sessions_total": 20, "sessions_attended": 18, "late_submissions": 1})
attendance_list.append({"student_id": "M211", "name": "Missing Field", "sessions_total": 20, "sessions_attended": 18})
attendance_list.append({"student_id": "M212", "name": "", "sessions_total": 20, "sessions_attended": 18, "late_submissions": 1})
attendance_list.append({"student_id": "M213", "name": "Too Many Attended", "sessions_total": 20, "sessions_attended": 25, "late_submissions": 1})
attendance_list.append({"student_id": "M214", "name": "Negative Late", "sessions_total": 20, "sessions_attended": 18, "late_submissions": -1})
attendance_list.append({"student_id": "M215", "name": "Text Attended", "sessions_total": 20, "sessions_attended": "eighteen", "late_submissions": 1})

with open("attendance.json", "w", encoding="utf-8") as f:
    json.dump(attendance_list, f, indent=2)

# ============================================================
# SECTION 1: VALIDATE A JSON STUDENT RECORD - YOUR CODE, UNCHANGED
# ============================================================
def check_student(student, seen_ids):
    if type(student) is not dict:
        return "Student record must be a JSON object"
    required_fields = ["student_id", "name", "sessions_total",
                       "sessions_attended", "late_submissions"]
    for field in required_fields:
        if field not in student:
            return "Missing field: " + field
    if type(student["student_id"]) is not str or student["student_id"].strip() == "":
        return "Invalid student ID"
    if type(student["name"]) is not str or student["name"].strip() == "":
        return "Invalid student name"
    if student["student_id"] in seen_ids:
        return "Duplicate student ID"
    total = student["sessions_total"]
    attended = student["sessions_attended"]
    late = student["late_submissions"]
    if type(total) is not int or type(attended) is not int or type(late) is not int:
        return "Attendance and late submissions must be whole numbers"
    if total <= 0 or attended < 0 or attended > total or late < 0:
        return "Attendance or late submission values are out of range"
    return ""

# ============================================================
# SECTION 2: CALCULATE RISK USING IF / ELIF / ELSE
# ============================================================
def calculate_risk(attendance_percent, late_submissions):
    if attendance_percent < 60 or late_submissions >= 5:
        return "HIGH"
    elif attendance_percent < 75 or late_submissions >= 3:
        return "MEDIUM"
    else:
        return "LOW"

# ============================================================
# SECTION 3: SORT BY ATTENDANCE (LOWEST FIRST)
# ============================================================
def sort_by_attendance(students):
    i = 0
    while i < len(students):
        smallest = i
        j = i + 1
        while j < len(students):
            first = students[j]
            second = students[smallest]
            if first["attendance_percent"] < second["attendance_percent"]:
                smallest = j
            elif first["attendance_percent"] == second["attendance_percent"]:
                if first["late_submissions"] > second["late_submissions"]:
                    smallest = j
            j += 1
        students[i], students[smallest] = students[smallest], students[i]
        i += 1

# ============================================================
# SECTION 4: READ THE JSON FILE
# ============================================================
def main():
    try:
        with open("attendance.json", "r", encoding="utf-8") as input_file:
            input_records = json.load(input_file)
    except FileNotFoundError:
        print("ERROR: Put attendance.json in the program's folder.")
        return
    except json.JSONDecodeError:
        print("ERROR: The JSON file contains invalid JSON syntax.")
        return
    if type(input_records) is not list:
        print("ERROR: The JSON file must contain a list of students.")
        return

    # ========================================================
    # SECTION 5: VALIDATE AND CLASSIFY STUDENTS
    # ========================================================
    clean_students = []
    errors = []
    seen_ids = {}
    record_number = 0
    high_count = 0
    medium_count = 0
    low_count = 0
    for student in input_records:
        record_number += 1
        reason = check_student(student, seen_ids)
        if reason != "":
            errors.append("Record " + str(record_number) + ": " + reason)
            continue
        seen_ids[student["student_id"]] = True
        percent = 100 * student["sessions_attended"] / student["sessions_total"]
        risk = calculate_risk(percent, student["late_submissions"])
        student["attendance_percent"] = percent
        student["risk"] = risk
        clean_students.append(student)
        if risk == "HIGH":
            high_count += 1
        elif risk == "MEDIUM":
            medium_count += 1
        else:
            low_count += 1
    sort_by_attendance(clean_students)

    # ========================================================
    # SECTION 6: SAVE CLEAN JSON AND ERROR LOG
    # ========================================================
    with open("attendance_clean.json", "w", encoding="utf-8") as clean_file:
        json.dump(clean_students, clean_file, indent=2)
    with open("attendance_errors.log", "w", encoding="utf-8") as error_file:
        for error in errors:
            error_file.write(error + "\n")

    # ========================================================
    # SECTION 7: WRITE THE SUMMARY REPORT
    # ========================================================
    accepted_count = 0
    for student in clean_students:
        accepted_count += 1
    rejected_count = 0
    for error in errors:
        rejected_count += 1
    with open("attendance_report.txt", "w", encoding="utf-8") as report:
        report.write("STUDENT ATTENDANCE EARLY WARNING\n")
        report.write(f"Accepted: {accepted_count} | Rejected: {rejected_count}\n")
        report.write(f"HIGH: {high_count}\nMEDIUM: {medium_count}\nLOW: {low_count}\n")
        report.write("\n10 LOWEST ATTENDANCE RECORDS\n")
        count = 0
        for student in clean_students:
            if count == 10:
                break
            count += 1
            report.write(f'{student["student_id"]} {student["name"]}: '
                         f'{student["attendance_percent"]:.1f}% ({student["risk"]})\n')

    # ========================================================
    # SECTION 8: DISPLAY THE SUMMARY
    # ========================================================
    print("STUDENT ATTENDANCE PROCESSOR")
    print("Accepted:", accepted_count, "Rejected:", rejected_count)
    print("HIGH:", high_count, "MEDIUM:", medium_count, "LOW:", low_count)
    print("Files created: attendance_clean.json, attendance_errors.log, attendance_report.txt")
    print("Fixed document is: attendance_clean.json")

    # ========================================================
    # SECTION 9: RETRIEVER - READ ONE LEARNER FROM ATTENDANCE
    # ========================================================
    print("\n--- RETRIEVER ---")
    print("Type EXIT to stop.")
    while True:
        search = input("Enter student ID to retrieve (e.g. M093): ").strip().upper()
        if search == "EXIT":
            print("Retriever closed.")
            break
        if search == "":
            continue
        found = None
        for s in clean_students:
            if s["student_id"] == search:
                found = s
                break
        if found is None:
            print("NOT FOUND:", search, "- rejected or does not exist. Check attendance_errors.log")
            continue
        print("--- RETRIEVED ---")
        print("ID:", found["student_id"])
        print("Name:", found["name"])
        print("Sessions:", found["sessions_attended"], "/", found["sessions_total"])
        print("Attendance:", f'{found["attendance_percent"]:.1f}%')
        print("Late submissions:", found["late_submissions"])
        print("Risk:", found["risk"])

# ============================================================
# SECTION 10: START THE PROGRAM
# ============================================================
if __name__ == "__main__":
    main()