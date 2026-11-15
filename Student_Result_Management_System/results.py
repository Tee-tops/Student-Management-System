SUBJECTS = ["English", "Mathematics", "Biology", "Chemistry", "Physics"]

def record_scores(student):
    print("Enter scores from 0 to 100. Five subjects are required.")
    for subject in SUBJECTS:
        while True:
            raw = input(f"{subject} score: ").strip()
            try:
                score = float(raw)
                if 0 <= score <= 100:
                    student.scores[subject] = score
                    break
                print("Score must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

def calculate_result(student):
    scores = student.scores
    if not scores:
        return {"total": 0, "average": 0, "grade": "N/A"}
    total = sum(scores.values())
    average = total / len(scores)
    if average >= 70: grade = "A"
    elif average >= 60: grade = "B"
    elif average >= 50: grade = "C"
    elif average >= 45: grade = "D"
    else: grade = "F"
    return {"total": total, "average": average, "grade": grade}

def grade_description(grade):
    return {"A": "Excellent", "B": "Very Good", "C": "Good", "D": "Pass", "F": "Fail"}.get(grade, "No result")
