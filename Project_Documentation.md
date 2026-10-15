# Project Documentation: Student Performance Analytics System

## 1. Project Title and Student Details
**Project:** Student Performance Analytics System  
**Student Name:** [Enter your name]  
**Course:** Python with AI — EWB Courses

## 2. Objective
To build a Python program that processes student marks and attendance, calculates student results, and summarizes class and subject performance.

## 3. Technologies Used
- Python
- NumPy
- Pandas
- CSV for storing the dataset

## 4. Dataset Description
The sample CSV contains 20 illustrative student records. Columns include Student_ID, Name, Department, marks in Python, Mathematics, Artificial Intelligence and Database Management, and Attendance_Percentage. The records are synthetic.

## 5. Implementation
1. Read `data/students.csv` with Pandas.
2. Check required columns, duplicate IDs, mark ranges and attendance ranges.
3. Use NumPy to calculate each student's total and average marks.
4. Use a loop and conditional statements to assign grades and pass/fail status.
5. Use Pandas to summarize subject performance and identify top performers.
6. Print the results and save the detailed output to `student_results.csv`.

## 6. Key Features
- Dataset loading and basic validation
- Total and average marks
- Grade assignment
- Pass/fail classification
- Class-level statistics
- Subject-wise averages, highest and lowest marks
- Top-five student ranking
- Department-level pass/fail counts
- Export of detailed results

## 7. Grading and Pass Rules
The assignment does not specify exact rules, so this implementation uses:
- A: average >= 90
- B: average >= 75 and < 90
- C: average >= 60 and < 75
- D: average >= 35 and < 60
- F: average < 35
- Pass: at least 35 marks in every subject; otherwise Fail.

## 8. Output / Screenshots
After running `python main.py`, capture screenshots of:
- Dataset overview
- Student results with grades and pass/fail
- Class summary
- Subject-wise performance
- Top five performers

## 9. Final Outcome
The program produces readable student-level results and class/subject summaries and exports the calculated results to a CSV file. Replace this paragraph with verified results from your final run if any implementation changes are made.

## 10. Challenges and Learning
Complete this section after testing. Describe any errors encountered, how you fixed them, and what you learned about functions, loops, conditions, NumPy and Pandas.

## 11. GitHub Repository
**Repository URL:** [Add your public GitHub repository URL after pushing the project]
