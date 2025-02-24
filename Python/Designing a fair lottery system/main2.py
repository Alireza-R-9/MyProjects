import random

input_file = "student_dataset.txt"
output_file = "results.txt"

def load_students(filename):
    students = []
    with open(filename, "r", encoding="utf-8") as file:
        next(file)
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 3:
                student_id, first_name, last_name = parts
                students.append((student_id, first_name, last_name))
    return students


def draw_winners(students, selection_counts, num_winners):
    eligible_students = [s for s in students if selection_counts[s[0]] < 3]
    never_selected = [s for s in students if selection_counts[s[0]] == 0]

    guaranteed_winners = random.sample(never_selected, min(len(never_selected), num_winners))

    remaining_slots = num_winners - len(guaranteed_winners)

    if remaining_slots > 0:
        weighted_students = []
        for student in eligible_students:
            weight = max(1, 5 - selection_counts[student[0]])
            weighted_students.extend([student] * weight)

        additional_winners = random.sample(weighted_students, min(remaining_slots, len(weighted_students)))
    else:
        additional_winners = []

    winners = guaranteed_winners + additional_winners

    for winner in winners:
        selection_counts[winner[0]] += 1

    return winners


def save_results(winners, selection_counts, filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Winners List:\n")
        for student in winners:
            file.write(f"{student[0]}, {student[1]} {student[2]} (انتخاب‌شده {selection_counts[student[0]]} بار)\n")

        file.write("\nFull Student List with Selection Counts:\n")
        for student_id, count in selection_counts.items():
            file.write(f"{student_id}: {count} بار انتخاب‌شده\n")


def main():
    students = load_students(input_file)

    if not students:
        print("لیست دانش‌آموزان خالی است. لطفاً فایل داده را بررسی کنید.")
        return

    selection_counts = {student[0]: 0 for student in students}

    num_days = int(input("تعداد روزهای قرعه‌کشی را وارد کنید: "))
    num_winners = int(input("تعداد برندگان در هر روز را وارد کنید: "))

    for day in range(1, num_days + 1):
        print(f"\n🔹 قرعه‌کشی روز {day}:")
        winners = draw_winners(students, selection_counts, num_winners)
        save_results(winners, selection_counts, output_file)
        for winner in winners:
            print(f"{winner[1]} {winner[2]} انتخاب شد (انتخاب {selection_counts[winner[0]]} بار)")

    print(f"\n✅ قرعه‌کشی برای {num_days} روز انجام شد! نتایج در '{output_file}' ذخیره شد.")


if __name__ == "__main__":
    main()
