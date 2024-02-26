import pymysql.cursors

# MySQL 데이터베이스에 연결합니다.
conn = pymysql.connect(host='orion.mokpo.ac.kr',  # 호스트 주소
                       user='root',               # 사용자 이름
                       password=None,             # 비밀번호 (없는 경우 None으로 둡니다)
                       db='Client_information',   # 사용할 데이터베이스 이름
                       charset='utf8utf8_bin')         # 문자 인코딩 설정

try:
    # 커서를 사용하여 쿼리를 실행합니다.
    with conn.cursor() as cursor:
        # SQL 쿼리를 준비합니다.
        sql = 'SELECT * FROM users WHERE email = %s'
        # 쿼리를 실행하고 필요한 파라미터를 함께 전달합니다.
        cursor.execute(sql, ('test@test.com',))
        # 결과를 가져옵니다. 여기서는 하나의 레코드만 가져옵니다.
        result = cursor.fetchone()
        # 결과를 출력합니다.
        print('--------------------')
        print(result[0])
        # 출력: (1, 'test@test.com', 'my-passwd')
finally:
    # 연결을 닫습니다.
    conn.close()