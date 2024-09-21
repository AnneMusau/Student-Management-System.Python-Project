import sqlite3

# Connect to database 
CONN = sqlite3.connect('your_database.db')
CURSOR = CONN.cursor()
