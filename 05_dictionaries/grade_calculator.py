scores = {}
subjects = ("Math", "Science", "English", "Computer")
student_name = input("Enter your name: ")
total_marks = 0

for subject in subjects:
    scores[subject] = float(input(f"Enter the marks of a {subject}: "))
    while scores[subject] < 0 or scores[subject] > 100:
        scores[subject] = float(input("Please Enter correct marks (0-100): "))

print("=" * 30)
print(f"{'REPORT CARD':^30}") # To align the text f"{text:<10}" # Left, f"{text:^10}"  # Center (f"{text:>10}"  # Right
print("=" * 30)
print("\n")
print(f"Name: {student_name}")
print("\n")
for key, value in scores.items():
    print(key, "=", f"{value:.2f}")

for value in scores.values():
    total_marks += value
print("\n")
print(f"Total marks: {total_marks:.2f} out of 400.00")
percentage_score = total_marks / 400 * 100
print(f"Percentage: {percentage_score:.2f}%")
if percentage_score >= 85:
    print("Grade: A")
elif percentage_score >= 70:
    print("Grade: B")
elif percentage_score >= 50:
    print("Grade: C")
else:
    print("Grade: F")
print("\n")
print("=" * 30)