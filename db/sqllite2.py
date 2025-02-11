import sqlite3

#SQLite通常适合作为嵌入式数据库用于程序内的数据存储和持久化。它具有以下优点，使它成为这些用途的良好选择：

# 1. **轻量级和嵌入式：** SQLite是一个轻量级的嵌入式数据库引擎，不需要独立的数据库服务器。它将整个数据库存储在一个单独的文件中，这使得在应用程序中使用它非常方便。

# 2. **SQL支持：** SQLite支持标准的SQL查询语言，您可以使用SQL来执行数据检索、插入、更新和删除等操作。这使得它在处理结构化数据时非常强大。

# 3. **跨平台：** SQLite可在多个平台上运行，包括Windows、Linux和macOS，因此它是跨平台的数据库解决方案。

# 4. **零配置：** 您无需进行复杂的数据库配置或管理，只需创建连接并开始使用。数据库文件的创建和维护都是自动的。

# 5. **事务支持：** SQLite支持事务，这意味着您可以确保数据的一致性和完整性。

# 6. **高性能：** 尽管SQLite适用于小型应用程序，但它在性能方面表现出色，可以处理大量数据。

# 7. **自包含：** SQLite数据库是自包含的，这意味着它不依赖于外部库或进程，因此不容易出现配置问题。

# 总之，SQLite是一个适用于小型应用程序、原型开发和需要简单持久化数据存储的理想选择。对于大型应用程序或需要高度并发支持的应用程序，可能需要考虑更复杂的数据库系统。但对于许多普通用例，SQLite提供了一种轻便且易于使用的解决方案。

# 连接到数据库文件
def connect_database(database_name):
    return sqlite3.connect(database_name)

def drop_table(connection, table_name, fields):
    cursor = connection.cursor()
    create_table_sql = f'Drop TABLE IF EXISTS {table_name}'
    cursor.execute(create_table_sql)
    connection.commit()

# 创建表格
def create_table(connection, table_name, fields):
    cursor = connection.cursor()
    field_str = ', '.join(fields)
    create_table_sql = f'CREATE TABLE IF NOT EXISTS {table_name} ({field_str})'
    cursor.execute(create_table_sql)
    connection.commit()

# 插入数据
def insert_record(connection, table_name, values):
    cursor = connection.cursor()
    field_str = ', '.join(['?' for _ in values])
    insert_sql = f'INSERT INTO {table_name} VALUES ({field_str})'
    cursor.execute(insert_sql, values)
    connection.commit()

# 查询所有记录
def get_all_records(connection, table_name):
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM {table_name}')
    return cursor.fetchall()

# 查询单条记录
def get_record_by_field(connection, table_name, field_name, field_value):
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM {table_name} WHERE {field_name} = ?', (field_value,))
    return cursor.fetchone()

# 更新记录
def update_record(connection, table_name, set_fields, where_field, where_value):
    cursor = connection.cursor()
    set_str = ', '.join([f'{field} = ?' for field in set_fields])
    update_sql = f'UPDATE {table_name} SET {set_str} WHERE {where_field} = ?'
    cursor.execute(update_sql, (*set_fields, where_value))
    connection.commit()

# 删除记录
def delete_record(connection, table_name, field_name, field_value):
    cursor = connection.cursor()
    cursor.execute(f'DELETE FROM {table_name} WHERE {field_name} = ?', (field_value,))
    connection.commit()

# 断开连接
def disconnect_database(connection):
    connection.close()

# 示例使用
if __name__ == "__main__":
    db_conn = connect_database('mydatabase.db')
    table_name = 'users'
    fields = ['id INTEGER PRIMARY KEY', 'username TEXT', 'email TEXT']

    drop_table(db_conn, table_name, fields)
    
    create_table(db_conn, table_name, fields)

    insert_record(db_conn, table_name, (1, 'user1', 'user1@example.com'))
    insert_record(db_conn, table_name, (2, 'user2', 'user2@example.com'))

    records = get_all_records(db_conn, table_name)
    for record in records:
        print(record)

    record = get_record_by_field(db_conn, table_name, 'username', 'user1')
    print("User by username:", record)

    update_record(db_conn, table_name, ['email'], 'username', 'user1')

    delete_record(db_conn, table_name, 'username', 'user2')

    records = get_all_records(db_conn, table_name)
    for record in records:
        print(record)

    disconnect_database(db_conn)
