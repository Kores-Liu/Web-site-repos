import connectsql

def get_content():
    conn = connectsql.sqlconnection(database='messageboard')
    cursor = conn.cursor()
    cursor.execute("select * from dbo.messages")
    return cursor.fetchall()

def insert_content(username, message):
    try:
        conn = connectsql.sqlconnection(database='messageboard')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO dbo.Users (username, password) VALUES (?, ?)", (username, message))
        conn.commit()  # 提交事务以确保数据被插入到数据库
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()
        
# if __name__ == '__main__':
#     print(get_content())

