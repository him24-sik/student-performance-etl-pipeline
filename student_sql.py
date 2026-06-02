import pandas as pd
import sqlite3

df = pd.read_csv(
    "processed_student_data.csv"
)


conn = sqlite3.connect("students.db")

df.to_sql(
    "students",
    conn,
    if_exists="replace",
    index=False
)

query = """
SELECT Subject,
AVG(Marks) AS Avg_Marks
FROM students
GROUP BY Subject
"""

result = pd.read_sql_query(query, conn)

print(result)

conn.close()