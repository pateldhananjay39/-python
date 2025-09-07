

import sqlite3

conn = sqlite3.connect('multiple_student_subjects.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS multiple_student_subjects')

cursor.execute('''
    CREATE TABLE multiple_student_subjects (
        Enrollment INTEGER,
        name TEXT NOT NULL,
        Subject TEXT NOT NULL,
        Mark INTEGER NOT NULL,
        PRIMARY KEY (Enrollment, Subject)
    )
''')
conn.commit()

multiple_student_subjects = [
    (92400133074, 'Dhananjay', 'PWP', 95),
    (92400133074, 'Dhananjay', 'ICE', 95),
    (92400133074, 'Dhananjay', 'DMGT', 90),
    (92400133074, 'Dhananjay', 'DSC', 95),
    (92400133074, 'Dhananjay', 'SS', 90),
    (92400133074, 'Dhananjay', 'COA', 95)
]
cursor.executemany('''
    INSERT INTO multiple_student_subjects (Enrollment, name, Subject, Mark) 
    VALUES (?, ?, ?, ?)
''', multiple_student_subjects)
conn.commit()

cursor.execute('SELECT * FROM multiple_student_subjects')
rows = cursor.fetchall()
print("All Student Subjects Records:")
for row in rows:
    print(row)

cursor.execute('SELECT name, Subject, Mark FROM multiple_student_subjects WHERE Mark > 90')
high_marks = cursor.fetchall()
print("\nSubjects with Marks greater than 90:")
for subject in high_marks:
    print(subject)

cursor.execute('''
    UPDATE multiple_student_subjects 
    SET Mark = 98 
    WHERE Enrollment = 92400133074 AND Subject = 'ICE'
''')
conn.commit()

cursor.execute('''
    SELECT Subject, Mark FROM multiple_student_subjects 
    WHERE Enrollment = 92400133074 AND Subject = 'ICE'
''')
updated = cursor.fetchone()
print(f"\nUpdated Mark for ICE: {updated[1]}")

cursor.execute('''
    DELETE FROM multiple_student_subjects 
    WHERE Enrollment = 92400133074 AND Subject = 'DMGT'
''')
conn.commit()

cursor.execute('''
    SELECT * FROM multiple_student_subjects 
    WHERE Enrollment = 92400133074 AND Subject = 'DMGT'
''')
deleted = cursor.fetchone()
if deleted is None:
    print("\n'DMGT' subject record has been successfully deleted")

cursor.execute('''SELECT AVG(Mark) FROM multiple_student_subjects''')
avg_mark = cursor.fetchone()[0]
print(f"\nThe average mark of students is: {avg_mark:.2f}")