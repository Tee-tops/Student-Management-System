from datetime import datetime
from results import calculate_result, grade_description

def student_report(student):
    result = calculate_result(student)
    lines = [
        "=" * 50,
        "                 STUDENT REPORT CARD",
        "=" * 50,
        f"Student ID : {student.student_id}",
        f"Name       : {student.full_name}",
        f"Class/Form : {student.class_form}",
        f"Gender     : {student.gender}",
        f"Date of birth: {student.date_of_birth}",
        "-" * 50,
        "SUBJECT SCORES",
    ]
    if student.scores:
        for subject, score in student.scores.items():
            lines.append(f"{subject:<20} {score:>7.2f}")
    else:
        lines.append("No scores recorded.")
    lines += [
        "-" * 50,
        f"Total      : {result['total']:.2f}",
        f"Average    : {result['average']:.2f}",
        f"Grade      : {result['grade']} ({grade_description(result['grade'])})",
        f"Result date: {student.result_date}",
        "=" * 50,
    ]
    return "\n".join(lines)

def all_results_report(students):
    if not students:
        return "No students registered."
    ranked = sorted(students, key=lambda s: calculate_result(s)["average"], reverse=True)
    lines = ["STUDENT RESULTS (highest average first)", "-" * 75,
             f"{'ID':<12}{'NAME':<25}{'TOTAL':>10}{'AVERAGE':>12}{'GRADE':>10}", "-" * 75]
    for s in ranked:
        r = calculate_result(s)
        lines.append(f"{s.student_id:<12}{s.full_name[:24]:<25}{r['total']:>10.2f}{r['average']:>12.2f}{r['grade']:>10}")
    return "\n".join(lines)

def class_statistics(students):
    with_results = [s for s in students if s.scores]
    if not with_results:
        return "No scores available for class statistics."
    averages = [calculate_result(s)["average"] for s in with_results]
    return (
        "CLASS STATISTICS\n"
        f"Students registered: {len(students)}\n"
        f"Students with results: {len(with_results)}\n"
        f"Highest average: {max(averages):.2f}\n"
        f"Lowest average: {min(averages):.2f}\n"
        f"Class average: {sum(averages)/len(averages):.2f}"
    )

def save_text_report(students):
    filename = f"class_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    content = all_results_report(students) + "\n\n" + class_statistics(students)
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"Report saved as {filename}")
