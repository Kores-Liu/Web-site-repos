import connectsql

def get_content():
    conn = connectsql.sqlconnection(database='messageboard')
    cursor = conn.cursor()
    cursor.execute("select * from dbo.messages")
    return cursor.fetchall()


    
# if __name__ == '__main__':
#     print(get_content())

