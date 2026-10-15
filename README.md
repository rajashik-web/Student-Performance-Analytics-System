# Student Performance Analytics System

A Python-based Student Performance Analytics System that analyzes student marks and attendance using Python, NumPy, and Pandas. It calculates total and average marks, assigns grades, identifies pass/fail status, analyzes subject-wise performance, and ranks top-performing students.

## Features

- Loads student records from a CSV file using Pandas.
- Validates student IDs, marks, and attendance values.
- Calculates total and average marks for each student.
- Assigns grades according to a defined grading scale.
- Determines pass/fail status for each student.
- Calculates class-level performance statistics.
- Performs subject-wise performance analysis.
- Identifies the top five performers.
- Displays department-wise pass/fail statistics.
- Exports detailed results to `student_results.csv`.

## Technologies Used

- Python
- NumPy
- Pandas
- CSV

## Grading Rules

| Average Marks | Grade |
|---|---|
| 90 and above | A |
| 75 to below 90 | B |
| 60 to below 75 | C |
| 35 to below 60 | D |
| Below 35 | F |

**Pass condition:** A student must score at least 35 marks in every subject. Otherwise, the student fails.

These rules were selected for this implementation because the assignment does not prescribe an exact grading scale.

## Dataset

The project includes 20 illustrative student records with the following information:

- Student ID
- Name
- Department
- Python marks
- Mathematics marks
- Artificial Intelligence marks
- Database Management marks
- Attendance percentage

The dataset is synthetic and does not contain real student records.

## Project Structure

```text
Student-Performance-Analytics-System/
├── data/
│   └── students.csv
├── main.py
├── functions.py
├── test_project.py
├── requirements.txt
├── student_results.csv
├── README.md
└── Project_Documentation.md
```

## Installation and Execution

### 1. Create a virtual environment

```bash
python -m venv .venv
```

### 2. Activate the environment on Windows

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the project

```bash
python main.py
```

The analysis is displayed in the terminal, and the calculated student results are saved to `student_results.csv`.

## Run Tests

```bash
python -m unittest -v test_project.py
```

The current test suite contains five tests covering calculations, grade boundaries, pass/fail rules, class summaries, and subject summaries.

## Expected Outcome

The program generates student-level results, class performance statistics, subject-wise summaries, and a ranking of the top five students.

## Author

Ashik Raj
