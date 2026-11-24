students = []

def get_grade(mark):
    if mark >= 90 and mark <= 100:
        return "A"
    elif mark >= 80 and mark < 90:
        return "B"
    elif mark >= 70 and mark < 79:
        return "C"
    elif mark >= 60 and mark < 69:
        return "D"
    elif mark < 60:
        return "F"
    else:
        return "Invalid mark"


def add_student():
    name = input("Enter the name of the student to add: ")
    mark = float(input(f"Enter the mark for {name} between 0 and 100: "))

    while True:
        if 0 <= mark <= 100:
            # students.append(name)
            students.append({"Name": name, "Mark": mark})
            print(f"{name} has been added to the student list.")
            break
        else:
            print("Invalid mark. Please enter a mark between 0 and 100.")
            mark = float(input(f"Enter the mark for {name} between 0 and 100: "))
            continue
    
    print(f"{name} has been added to the student list with a mark of {mark}.")

def show_results():
    if not students:
        print("No students in the list.")
        return

    total=0
    print("\nStudent Results:")
    print(f"Name\tMark\tGrade")
    for student in students:
        name = student["Name"]
        mark = student["Mark"]
        grade = get_grade(mark)
        print(f"{name}\t{mark}\t{grade}")
        total += mark
    average = total / len(students)
    print(f"\nAverage Mark: {average:.2f}")
    Highest_mark = max(student["Mark"] for student in students)
    print(f"Highest Mark: {Highest_mark}")
    Lowest_mark = min(student["Mark"] for student in students)
    print(f"Lowest Mark: {Lowest_mark}")


while True:
    print("\nGrade Manager Menu:")
    print("1. Add Student")
    print("2. Show Results")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_results()
    elif choice == "3":
        print("Exiting the Grade Manager.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")
