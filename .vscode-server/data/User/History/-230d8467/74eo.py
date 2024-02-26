import pymysql.cursors
 
conn = pymysql.connect(host='orion.mokpo.ac.kr',
        user='root',
        password=None,
        db='test',
        charset='utf8mb4')
 
try:
    with conn.cursor() as cursor:
        sql = 'SELECT * FROM users WHERE email = %s'
        cursor.execute(sql, ('test@test.com',))
        result = cursor.fetchone()
        print(result)
        # (1, 'test@test.com', 'my-passwd')
finally:
    conn.close()