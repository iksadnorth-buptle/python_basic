# Section12-3

import sqlite3

# DB생성
url = r'C:\python_basic\resource\database.db'
conn = sqlite3.connect(url, isolation_level=None)
c = conn.cursor()

c.execute("UPDATE users SET username = ? WHERE id = ?", ('niceman', 1))
c.execute("UPDATE users SET username = :name WHERE id = :id", {"name" : "goodman", "id" : 5})
c.execute("UPDATE users SET username = '%s' WHERE id = %s" % ('lee', 3))

for user in c.execute("SELECT * FROM users"):
    print(user)

# Row Delete1
c.execute("DELETE FROM users WHERE id = ?", (2,))

# Row Delete2
c.execute("DELETE FROM users WHERE id = :id", {"id": 5})

# Row Delete3
c.execute("DELETE FROM users WHERE id = '%s'" % 4)

for user in c.execute("SELECT * FROM users"):
    print(user)

conn.commit()

conn.close()
