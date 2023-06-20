import mysql.connector

connect = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="myContacts-cli"
)

cursor = connect.cursor()