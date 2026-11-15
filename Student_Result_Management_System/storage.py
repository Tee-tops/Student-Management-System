import json
import os
from student import Student

def load_students(filename):
    if not os.path.exists(filename):
        os.makedirs(os.path.dirname(filename) or ".", exist_ok=True)
        return []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
        return [Student.from_dict(item) for item in data]
    except (json.JSONDecodeError, OSError) as error:
        print(f"Could not load saved data ({error}). Starting with an empty list.")
        return []

def save_students(students, filename):
    os.makedirs(os.path.dirname(filename) or ".", exist_ok=True)
    with open(filename, "w", encoding="utf-8") as file:
        json.dump([student.to_dict() for student in students], file, indent=4)
