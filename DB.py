import sqlite3
conn=sqlite3.connect('DB.db')
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS DB_1
          (
           [user_name] TEXT,
           [password] TEXT,
           [mobile] TEXT,
           [email_id] TEXT)''')

conn.commit()
conn.close()
