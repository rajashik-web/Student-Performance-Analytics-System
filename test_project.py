
import unittest
import pandas as pd

from functions import (
    SUBJECTS,
    calculate_student_results,
    get_class_summary,
    get_subject_summary,
)


def make_student(marks):
    """Create one test student with the given subject marks."""
    row = {
        "Student_ID": "TEST001",
        "Name": "Test Student",
        "Department": "AI & ML",
        "Attendance_Percentage": 90,
    }
    row.update(dict(zip(SUBJECTS, marks)))
    return pd.DataFrame([row])


class TestStudentPerformance(unittest.TestCase):

    def test_total_and_average(self):
        df = make_student([80, 70, 90, 60])
        result = calculate_student_results(df)

        self.assertEqual(result.loc[0, "Total_Marks"], 300)
        self.assertEqual(result.loc[0, "Average_Marks"], 75.0)

    def test_grade_boundaries(self):
        for average, expected_grade in [
            (95, "A"),
            (80, "B"),
            (65, "C"),
            (40, "D"),
            (20, "F"),
        ]:
            with self.subTest(average=average):
                df = make_student([average] * 4)
                result = calculate_student_results(df)
                self.assertEqual(result.loc[0, "Grade"], expected_grade)

    def test_all_subjects_must_pass(self):
        passing = calculate_student_results(make_student([35, 35, 35, 35]))
        failing = calculate_student_results(make_student([34, 90, 90, 90]))

        self.assertEqual(passing.loc[0, "Result"], "Pass")
        self.assertEqual(failing.loc[0, "Result"], "Fail")

    def test_class_summary(self):
        df = pd.concat([
            make_student([80, 80, 80, 80]),
            make_student([40, 40, 40, 40]),
        ], ignore_index=True)

        results = calculate_student_results(df)
        summary = get_class_summary(results)

        self.assertEqual(summary["student_count"], 2)
        self.assertEqual(summary["class_average"], 60.0)
        self.assertEqual(summary["passed"], 2)
        self.assertEqual(summary["failed"], 0)

    def test_subject_summary(self):
        df = make_student([80, 70, 90, 60])
        summary = get_subject_summary(df)

        self.assertEqual(len(summary), 4)
        self.assertEqual(summary.iloc[0]["Average_Marks"], 90.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
