import sqlite3

dbfile = 'data.db'

connection = sqlite3.connect(dbfile)
cursor = connection.cursor()

query = """
SELECT * FROM albums
WHERE TITLE LIKE '%Live%' AND LENGTH(Title) > 10
"""

cursor.execute(query)
rows = cursor.fetchall()


for row in rows:
    print(f'{rows[0]}: {row[1]}')

connection.close()
