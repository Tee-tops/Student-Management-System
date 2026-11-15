# Student Result Management System (Python)

A menu-driven console application for registering students, recording five subject scores, calculating totals/averages/grades, viewing report cards, ranking students, showing class statistics, and saving reports.

## Requirements
- Python 3.10+ (uses dataclasses; tested conceptually with Python 3.14)
- No third-party packages required.

## Run
Open this folder in VS Code and run:
```bash
python main.py
```
If `python` is not recognised on Windows, use the selected interpreter's **Run Python File** button in VS Code, or try:
```powershell
py main.py
```

## Files
- `main.py`: menu and user operations
- `student.py`: Student class and JSON conversion
- `results.py`: score entry, result calculations and grading
- `storage.py`: JSON file loading/saving
- `reports.py`: report cards, class report and statistics
- `data/students.json`: persistent student records (created/updated automatically)

## Grade scale
- A: 70–100
- B: 60–69.99
- C: 50–59.99
- D: 45–49.99
- F: below 45

## Notes
Scores are validated to be between 0 and 100. The five default subjects are English, Mathematics, Biology, Chemistry and Physics. You may edit these in `results.py`.
