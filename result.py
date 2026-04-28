def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 75:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "Fail"

def main():
    print("🎓 Student Result System")

    name = input("Enter Student Name: ")
    subjects = int(input("Enter number of subjects: "))

    total_marks = 0

    for i in range(subjects):
        marks = float(input(f"Enter marks for subject {i+1}: "))
        total_marks += marks

    percentage = total_marks / subjects
    grade = calculate_grade(percentage)

    print("\n--- Result ---")
    print("Name:", name)
    print("Total Marks:", total_marks)
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", grade)

if __name__ == "__main__":
    main()