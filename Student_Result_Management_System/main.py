from student import Student
from storage import load_students, save_students
from results import record_scores, calculate_result
from reports import student_report, all_results_report, class_statistics, save_text_report

DATA_FILE = "data/students.json"

def get_student(students, student_id):
    return next((s for s in students if s.student_id.lower() == student_id.lower()), None)

def add_student(students):
    print("\n--- Register Student ---")
    student_id = input("Student ID: ").strip()
    if not student_id:
        print("Student ID cannot be empty.")
        return
    if get_student(students, student_id):
        print("That Student ID already exists.")
        return
    name = input("Full name: ").strip()
    form = input("Class/Form: ").strip()
    gender = input("Gender: ").strip()
    dob = input("Date of birth (YYYY-MM-DD): ").strip()
    student = Student(student_id, name, form, gender, dob)
    students.append(student)
    save_students(students, DATA_FILE)
    print(f"{name} registered successfully.")

def view_students(students):
    print("\n--- Registered Students ---")
    if not students:
        print("No students registered yet.")
        return
    for s in students:
        print(f"{s.student_id} | {s.full_name} | {s.class_form}")

def search_student(students):
    term = input("Enter Student ID or name: ").strip().lower()
    matches = [s for s in students if term in s.student_id.lower() or term in s.full_name.lower()]
    if not matches:
        print("No matching student found.")
    else:
        for s in matches:
            print(f"{s.student_id} | {s.full_name} | {s.class_form}")

def update_student(students):
    sid = input("Student ID to update: ").strip()
    s = get_student(students, sid)
    if not s:
        print("Student not found."); return
    print("Press Enter to keep the current value.")
    s.full_name = input(f"Full name [{s.full_name}]: ").strip() or s.full_name
    s.class_form = input(f"Class/Form [{s.class_form}]: ").strip() or s.class_form
    s.gender = input(f"Gender [{s.gender}]: ").strip() or s.gender
    s.date_of_birth = input(f"Date of birth [{s.date_of_birth}]: ").strip() or s.date_of_birth
    save_students(students, DATA_FILE)
    print("Student information updated.")

def delete_student(students):
    sid = input("Student ID to delete: ").strip()
    s = get_student(students, sid)
    if not s:
        print("Student not found."); return
    confirm = input(f"Delete {s.full_name}? (y/n): ").strip().lower()
    if confirm == "y":
        students.remove(s)
        save_students(students, DATA_FILE)
        print("Student deleted.")

def enter_or_update_scores(students):
    sid = input("Student ID: ").strip()
    s = get_student(students, sid)
    if not s:
        print("Student not found. Register the student first."); return
    record_scores(s)
    save_students(students, DATA_FILE)
    print("Scores saved.")

def show_report(students):
    sid = input("Student ID: ").strip()
    s = get_student(students, sid)
    if not s:
        print("Student not found."); return
    print(student_report(s))

def menu():
    students = load_students(DATA_FILE)
    actions = {
        "1": lambda: add_student(students),
        "2": lambda: view_students(students),
        "3": lambda: search_student(students),
        "4": lambda: update_student(students),
        "5": lambda: delete_student(students),
        "6": lambda: enter_or_update_scores(students),
        "7": lambda: show_report(students),
        "8": lambda: print(all_results_report(students)),
        "9": lambda: print(class_statistics(students)),
        "10": lambda: save_text_report(students),
    }
    while True:
        print("\n" + "=" * 48)
        print("       STUDENT RESULT MANAGEMENT SYSTEM")
        print("=" * 48)
        print("1. Register student")
        print("2. View all students")
        print("3. Search student")
        print("4. Update student information")
        print("5. Delete student")
        print("6. Record/update scores")
        print("7. View individual report card")
        print("8. View all results (sorted by average)")
        print("9. Class statistics")
        print("10. Save class report to text file")
        print("0. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "0":
            save_students(students, DATA_FILE)
            print("Data saved. Goodbye!")
            break
        action = actions.get(choice)
        if action:
            try:
                action()
            except (ValueError, OSError) as error:
                print(f"Error: {error}")
        else:
            print("Invalid option. Please choose from the menu.")

if __name__ == "__main__":
    menu()
