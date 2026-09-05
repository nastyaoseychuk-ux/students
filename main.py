import sqlite3

connection = sqlite3.connect("student.db")
cursor = connection.cursor()

query = """
SELECT age.subject, AVG(age.grade) AS average_grade
FROM students
JOIN age
    ON students.student_id = age.student_id
WHERE students.age <= 20
GROUP BY age.subject;
"""

cursor.execute(query)

results = cursor.fetchall()

print(results)

connection.close()