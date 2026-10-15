"""Student Performance Analytics System.

Run from the project root:
    python main.py
"""

from pathlib import Path

import pandas as pd

from functions import (
    SUBJECTS,
    calculate_student_results,
    get_class_summary,
    get_subject_summary,
)


PROJECT_DIR = Path(__file__).resolve().parent
DATA_FILE = PROJECT_DIR / "data" / "students.csv"


def load_dataset(file_path):
    """Load the CSV and validate its required columns and values."""
    df = pd.read_csv(file_path)

    required_columns = [
        "Student_ID", "Name", "Department", *SUBJECTS, "Attendance_Percentage"
    ]
    missing = [column for column in required_columns if column not in df.columns]
    if missing:
        raise ValueError(f"Dataset is missing required columns: {missing}")

    if df.empty:
        raise ValueError("The student dataset is empty.")

    if df["Student_ID"].duplicated().any():
        raise ValueError("Student_ID values must be unique.")

    if df[SUBJECTS].isna().any().any():
        raise ValueError("Subject marks cannot be blank.")

    for subject in SUBJECTS:
        if not df[subject].between(0, 100).all():
            raise ValueError(f"{subject} marks must be between 0 and 100.")

    if not df["Attendance_Percentage"].between(0, 100).all():
        raise ValueError("Attendance_Percentage must be between 0 and 100.")

    return df


def main():
    """Run the complete student performance analysis."""
    try:
        students = load_dataset(DATA_FILE)
    except (FileNotFoundError, ValueError, pd.errors.ParserError) as error:
        print(f"Could not load the dataset: {error}")
        return

    results = calculate_student_results(students)
    class_summary = get_class_summary(results)
    subject_summary = get_subject_summary(students)

    print("\n" + "=" * 68)
    print("          STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 68)

    print("\n1. DATASET OVERVIEW")
    print(f"Number of students : {len(students)}")
    print(f"Departments        : {students['Department'].nunique()}")
    print(f"Columns            : {len(students.columns)}")
    print("\nStudent records (first 10):")
    print(students.head(10).to_string(index=False))

    print("\n2. STUDENT RESULTS")
    display_columns = [
        "Student_ID", "Name", "Total_Marks", "Average_Marks", "Grade", "Result"
    ]
    print(results[display_columns].sort_values(
        "Average_Marks", ascending=False
    ).to_string(index=False))

    print("\n3. CLASS SUMMARY")
    print(f"Overall class average : {class_summary['class_average']}")
    print(f"Highest student avg   : {class_summary['highest_average']}")
    print(f"Lowest student avg    : {class_summary['lowest_average']}")
    print(f"Students passed       : {class_summary['passed']}")
    print(f"Students failed       : {class_summary['failed']}")

    print("\n4. SUBJECT-WISE PERFORMANCE (best average first)")
    print(subject_summary.to_string(index=False))

    print("\n5. TOP 5 PERFORMERS")
    top_five = results.nlargest(5, "Average_Marks")
    print(top_five[display_columns].to_string(index=False))

    print("\n6. PASS/FAIL COUNTS BY DEPARTMENT")
    department_results = results.groupby(
        ["Department", "Result"]
    ).size().unstack(fill_value=0)
    print(department_results.to_string())

    # Save a results file so the analysis can be reused without recalculating manually.
    output_file = PROJECT_DIR / "student_results.csv"
    results.to_csv(output_file, index=False)
    print(f"\nDetailed results saved to: {output_file.name}")
    print("\nAnalysis completed successfully.")


if __name__ == "__main__":
    main()
