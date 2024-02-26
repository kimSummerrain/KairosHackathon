import pymysql.cursors

# MySQL 데이터베이스에 연결합니다.
conn = pymysql.connect(host='localhost',          # 호스트 주소
                       user='root',               # 사용자 이름
                       password='ScE1234**',      # 비밀번호 (없는 경우 None으로 둡니다)
                       db='client_information',   # 사용할 데이터베이스 이름
                       charset='utf8mb4')         # 문자 인코딩 설정

try:
    # 커서를 사용하여 쿼리를 실행합니다.
    with conn.cursor() as cursor:
        # SQL 쿼리를 준비합니다.
        sql = 'SELECT * FROM Expenditures'
        # 쿼리를 실행하고 필요한 파라미터를 함께 전달합니다.
        cursor.execute(sql)
        # 결과를 가져옵니다. 여기서는 하나의 레코드만 가져옵니다.
        results = cursor.fetchall()
        # 결과를 출력합니다.
        for result in results:
            print(result)
        # 출력: (1, 'test@test.com', 'my-passwd')
        # 출력: (2, 'test@test.com', 'my-passwd')
        # 출력: (3, 'test@test.com', 'my-passwd')
        #                 .
        #                 .
        #                 .
finally:
    # 연결을 닫습니다.
    conn.close()