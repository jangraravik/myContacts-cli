import database.connect as db

print('Read ID:')
id = input()

vals = (id,)

db.cursor.execute("SELECT * FROM contacts WHERE id=%s ", vals)
rows = db.cursor.fetchall()
for row in rows:
    print(row)

