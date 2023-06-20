import database.connect as db

print('Update ID:')
id = input()

print('Enter Name:')
name = input()
print('Enter Mobile:')
mobile = input()

vals = (name, mobile, id)
db.cursor.execute("UPDATE contacts SET name=%s, mobile=%s WHERE id=%s ", vals)
db.connect.commit()
print(db.cursor.rowcount, "record updated.")