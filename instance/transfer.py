import sqlite3
from pymongo import MongoClient

# 连接SQLite数据库
conn = sqlite3.connect('promptate.db')

# 创建一个 cursor 对象
cursor = conn.cursor()

# 从SQLite数据库读取数据
cursor.execute('SELECT * FROM user')
rows = cursor.fetchall()
print(rows)

# # 连接MongoDB
# client = MongoClient('mongodb://localhost:27017/')
# db = client['test']
# collection = db['employee']

# # 将数据导入MongoDB
# for row in rows:
#     data = {'name': row[0], 'age': row[1], 'salary': row[2]}
#     collection.insert_one(data)

# # 关闭连接
# conn.close()
# client.close()