import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('select * from user')
print cursor.description
print cursor.fetchall()
cursor.close()
conn.commit()
conn.close()