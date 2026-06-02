import pandas as pd

df = pd.read_csv(
    "python_skills/student_data_100.csv",
    sep="\t"
)

print("Columns:")
print(df.columns)

print("\nFirst 5 Records:")
print(df.head())

print("\nAverage Marks:")
print(df["Marks"].mean())

print("\nTop 5 Students:")
print(df.sort_values("Marks", ascending=False).head())

print("\nCourse Wise Average Marks:")
print(df.groupby("Course")["Marks"].mean())
print("\nSubject Wise Average Marks:")
print(df.groupby("Subject")["Marks"].mean())

print("\nHighest Attendance Student:")
print(df.sort_values("Attendance", ascending=False).head(1))

print("\nStudents Scoring Above 80:")
print(df[df["Marks"] > 80])
def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "D"

df["Grade"] = df["Marks"].apply(grade)
print("\nGrade Distribution:")
print(df["Grade"].value_counts())
df.to_csv(
    "python_skills/processed_student_data.csv",
    index=False
)

print("\nProcessed file saved successfully!")