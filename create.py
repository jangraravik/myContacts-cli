import database.connect as db

print('Enter Name:')
name = input()
print('Enter Mobile:')
mobile = input()

vals = (name, mobile)

db.cursor.execute("INSERT INTO contacts (name, mobile) VALUES (%s, %s)", vals)
db.connect.commit()
print(db.cursor.rowcount, "record inserted.")