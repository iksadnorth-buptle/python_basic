# Section12-1

import sqlite3

print('version : ', sqlite3.version)
print('version : ', sqlite3.sqlite_version)

from datetime import datetime

now = datetime.now()
print('now : ', now)

nowDateTime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDatetime : ', nowDateTime)

# DB 생성 & Auto Commit(Rollback)
url = r'C:\python_basic\resource\database.db'
conn = sqlite3.connect(url, isolation_level=None)

# Cursor
c = conn.cursor()
print('Cursor Type : ', type(c))

# 테이블 생성(Data Type : TEXT, NUMERIC INTEGER REAL BLOB)
c.execute("""
          CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY, 
            username text,
            email text,
            phone text,
            website text,
            regdate text
          )
          """)

# c.execute("""
#         INSERT INTO users VALUES(1, 'Kim', 'Kim@naver.com', '010-0000-0000', 'Kim.com', ?)
#           """, (nowDateTime,)
#           )
c.execute("""
        INSERT INTO users(id, username, email, phone, website, regdate) 
          VALUES(?,?,?,?,?,?)
          """, 
          (1, 'Kim', 'Kim@naver.com', '010-0000-0000', 'Kim.com', nowDateTime,)
          )

# Many 삽입(튜플, 리스트)
userList = (
    (3, 'Kim', 'Kim@naver.com', '010-0000-0000', 'Kim.com', nowDateTime,),
    (4, 'Kim', 'Kim@naver.com', '010-0000-0000', 'Kim.com', nowDateTime,),
    (5, 'Kim', 'Kim@naver.com', '010-0000-0000', 'Kim.com', nowDateTime,),
)

c.executemany("""
        INSERT INTO users(id, username, email, phone, website, regdate) 
          VALUES(?,?,?,?,?,?)
          """, userList)