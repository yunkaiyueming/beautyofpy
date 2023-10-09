import sqlite3

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
