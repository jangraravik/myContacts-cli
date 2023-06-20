import database.connect as db

print('Delete ID:')
id = input()

vals = (id,)

db.cursor.execute("DELETE FROM contacts WHERE id=%s ", vals)
db.connect.commit()
print(db.cursor.rowcount, "record deleted.")