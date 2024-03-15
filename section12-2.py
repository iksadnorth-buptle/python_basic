# Section12-1

import sqlite3

# DB 조회
url = r'C:\python_basic\resource\database.db'
conn = sqlite3.connect(url, isolation_level=None)

c = conn.cursor()

c.execute("SELECT * FROM users")

# print('One -> \n', c.fetchone())
# print('Three -> \n', c.fetchmany(size=3))

# print('All -> \n', c.fetchall())
# print()

# 순회 1
rows = c.fetchall()
for row in rows:
    print('retrieve1 > ', row)

# 순회 2
for row in c.fetchall():
    print('retrieve2 > ', row)

# 순회 3
for row in c.execute("SELECT * FROM users ORDER BY id desc"):
    print('retrieve3 > ', row)

# WHERE Retrieve1
param1 = (3,)
c.execute("SELECT * FROM users WHERE id=?", param1)
print('param1', c.fetchone())
print('param1', c.fetchall())

# WHERE Retrieve2
param2 = 4
c.execute("SELECT * FROM users WHERE id=%s" % param2)
print('param1', c.fetchone())
print('param1', c.fetchall())

# WHERE Retrieve3
c.execute("SELECT * FROM users WHERE id=:ID", {"ID": 5})
print('param1', c.fetchone())
print('param1', c.fetchall())

# WHERE Retrieve4
param4 = (3,5)
c.execute("SELECT * FROM users WHERE id IN (?,?)", param4)
print('param1', c.fetchone())
print('param1', c.fetchall())

# WHERE Retrieve5
param5 = (3,5)
c.execute("SELECT * FROM users WHERE id IN (%s,%s)" % param5)
print('param1', c.fetchone())
print('param1', c.fetchall())

# WHERE Retrieve6
c.execute("SELECT * FROM users WHERE id=:ID1 or id=:ID2", {"ID1": 2, "ID2": 5})
print('param1', c.fetchone())
print('param1', c.fetchall())

# Dump 출력
url1 = r'C:\python_basic\resource\dump.sql'
with conn:
    with open(url1, 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Dump Print Complete')
