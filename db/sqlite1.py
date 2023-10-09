import sqlite3

# 创建或连接到数据库文件（如果不存在，则会自动创建）
conn = sqlite3.connect('mydatabase.db')

# 创建一个名为 'users' 的表格
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT,
                    email TEXT
                )''')
conn.commit()

# 插入数据
cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", ('user1', 'user1@example.com'))
conn.commit()

# 查询数据
cursor.execute("SELECT * FROM users")
result = cursor.fetchall()

for row in result:
    print(row)

# 更新数据
cursor.execute("UPDATE users SET email = ? WHERE username = ?", ('new_email@example.com', 'user1'))
conn.commit()

# 删除数据
cursor.execute("DELETE FROM users WHERE username = ?", ('user1',))
conn.commit()

# 断开连接
conn.close()
