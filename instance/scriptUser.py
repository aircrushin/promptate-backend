import sqlite3
from werkzeug.security import generate_password_hash

def create_connection(db_file):
    """ 创建数据库连接到 SQLite 数据库 """
    conn = sqlite3.connect(db_file)
    return conn

def create_user_table(conn):
    """ 在给定的数据库连接中创建 user 表 """
    try:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        );
        """)
        conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")

def add_user(conn, username, password):
    """ 向 user 表中添加新用户 """
    hashed_password = generate_password_hash(password)
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO user (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Username {username} already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

# 现在，我们将使用这些函数来修改您的数据库
db_file = 'D:\桌面\毕业设计\代码\promptate\server\instance\promptate.db'  # 指定数据库文件的路径
print("add now")
# 创建数据库连接
conn = create_connection(db_file)

# 创建 user 表
create_user_table(conn)

# 如需添加用户，调用 add_user 函数
add_user(conn, 'admin', 'admin123')

# 关闭数据库连接
conn.close()
