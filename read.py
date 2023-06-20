import database.connect as db

print('Available Contacts:')

db.cursor.execute("SELECT * FROM contacts")
rows = db.cursor.fetchall()
for row in rows:
    print(row)

