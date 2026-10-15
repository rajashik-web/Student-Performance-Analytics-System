"""Reusable calculations for the Student Performance Analytics System."""

import numpy as np
import pandas as pd

SUBJECTS = [
    "Python",
    "Mathematics",
    "Artificial_Intelligence",
    "Database_Management",
]


def calculate_student_results(df):
    """Return a copy of the dataset with totals, averages, grades and status."""
    results = df.copy()

    # NumPy is used for numerical calculations across the subject-mark columns.
    marks = results[SUBJECTS].to_numpy(dtype=float)
    results["Total_Marks"] = np.sum(marks, axis=1)
    results["Average_Marks"] = np.mean(marks, axis=1).round(2)

    grades = []
    statuses = []

    # Loops and conditions make the grading and pass rules explicit.
    for _, student in results.iterrows():
        average = student["Average_Marks"]
        if average >= 90:
            grade = "A"
        elif average >= 75:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 35:
            grade = "D"
        else:
            grade = "F"
        grades.append(grade)

        # A student passes only if every subject mark is at least 35.
        if all(student[subject] >= 35 for subject in SUBJECTS):
            statuses.append("Pass")
        else:
            statuses.append("Fail")

    results["Grade"] = grades
    results["Result"] = statuses
    return results


def get_subject_summary(df):
    """Summarize each subject's average, highest and lowest marks."""
    summary = pd.DataFrame({
        "Subject": SUBJECTS,
        "Average_Marks": [df[s].mean().round(2) for s in SUBJECTS],
        "Highest_Marks": [df[s].max() for s in SUBJECTS],
        "Lowest_Marks": [df[s].min() for s in SUBJECTS],
    })
    return summary.sort_values("Average_Marks", ascending=False)


def get_class_summary(results):
    """Return key class-level statistics."""
    return {
        "student_count": len(results),
        "class_average": round(float(results["Average_Marks"].mean()), 2),
        "highest_average": round(float(results["Average_Marks"].max()), 2),
        "lowest_average": round(float(results["Average_Marks"].min()), 2),
        "passed": int((results["Result"] == "Pass").sum()),
        "failed": int((results["Result"] == "Fail").sum()),
    }
