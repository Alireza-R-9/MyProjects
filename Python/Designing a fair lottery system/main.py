import random

# File names
input_file = "student_dataset.txt"
output_file = "lottery_results.txt"


# Load student data from file
def load_students(filename):
    students = []
    with open(filename, "r", encoding="utf-8") as file:
        next(file)  # Skip header line
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 3:
                student_id, first_name, last_name = parts
                students.append((student_id, first_name, last_name))
    return students


# Select winners with fairness constraints
def draw_winners(students, selection_counts, num_winners):
    eligible_students = [s for s in students if selection_counts[s[0]] < 3]  # Only those selected < 3 times
    never_selected = [s for s in students if selection_counts[s[0]] == 0]  # Those never selected

    # Ensure everyone is selected at least once
    guaranteed_winners = random.sample(never_selected, min(len(never_selected), num_winners))

    # Fill remaining slots with weighted random selection
    remaining_slots = num_winners - len(guaranteed_winners)

    if remaining_slots > 0:
        weighted_students = []
        for student in eligible_students:
            weight = max(1, 5 - selection_counts[student[0]])  # Higher weight for less selected students
            weighted_students.extend([student] * weight)

        additional_winners = random.sample(weighted_students, min(remaining_slots, len(weighted_students)))
    else:
        additional_winners = []

    winners = guaranteed_winners + additional_winners

    # Update selection counts
    for winner in winners:
        selection_counts[winner[0]] += 1

    return winners


# Save lottery results to file
def save_results(winners, selection_counts, filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Winners List:\n")
        for student in winners:
            file.write(f"{student[0]}, {student[1]} {student[2]} (Selected {selection_counts[student[0]]} times)\n")

        file.write("\nFull Student List with Selection Counts:\n")
        for student_id, count in selection_counts.items():
            file.write(f"{student_id}: Selected {count} times\n")


# Main function
def main():
    students = load_students(input_file)

    if not students:
        print("Student list is empty. Please check the data file.")
        return

    selection_counts = {student[0]: 0 for student in students}

    num_days = int(input("Enter the number of lottery days: "))
    num_winners = int(input("Enter the number of winners per day: "))

    for day in range(1, num_days + 1):
        print(f"\n🔹 Lottery Day {day}:")
        winners = draw_winners(students, selection_counts, num_winners)
        save_results(winners, selection_counts, output_file)
        for winner in winners:
            print(f"{winner[1]} {winner[2]} selected ({selection_counts[winner[0]]} times)")

    print(f"\n✅ Lottery completed for {num_days} days! Results saved in '{output_file}'.")


if __name__ == "__main__":
    main()
