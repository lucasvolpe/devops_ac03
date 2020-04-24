  
import sqlite3

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute('''CREATE TABLE Lucas (id integer, nome text not null, email text null)''')
c.execute("INSERT INTO victor VALUES (1, 'Lucas','Lucas@123.com')")
c.execute("INSERT INTO victor VALUES (2, 'Renat', renato@123.com)")

c.execute('''SELECT * FROM Lucas''')

for row in c.fetchall():
    print(row)

conn.commit()
conn.close()
