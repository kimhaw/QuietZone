import sqlite3

conn = sqlite3.connect("quietzone.db")
cursor = conn.cursor()

#Create academic records table
cursor.execute("""
CREATE TABLE IF NOT EXISTS academic_records (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     subject_name TEXT,
     record_type TEXT,
     score REAL,
     grade TEXT,
     semester TEXT
)
""")

#Check existing columns
cursor.execute("PRAGMA table_info(academic_records)")
columns = [column[1] for column in cursor.fetchall()]

# Add record_type if it does not exist
if "record_type" not in columns:
    cursor.execute("""
    ALTER TABLE academic_records
    ADD COLUMN record_type TEXT
    """)

# Add grade if it does not exist
if "grade" not in columns:
    cursor.execute("""
    ALTER TABLE academic_records
    ADD COLUMN grade TEXT
    """)

conn.commit()

cursor.execute("""
INSERT INTO academic_records
(subject_name, score, semester, record_type, grade)
VALUES ('Mathematics I', 15, 'Semester 2610', 'Midterm', '')
""")
conn.commit()

# Display academic records
cursor.execute("SELECT * FROM academic_records")
records = cursor.fetchall()

for record in records:
    print(record)

print("Academic records updated successfully!")

conn.close()
