import pymysql.cursors
from datetime import datetime

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

    Dict = {}

    # 결과를 출력합니다.
    for row in results:
        # 시간 값을 년-월-일 형식으로 변환하여 출력합니다.
        time_value = row[3]  # 예시에서 시간 값이 결과의 4번째 열 (0부터 시작)에 있다고 가정합니다.
        formatted_time = datetime.strftime(time_value, "%Y-%m-%d")  # 년-월-일 형식으로 포맷팅합니다.

        if not Dict.get(formatted_time):         # 날짜가 없다면 날짜를 추가
            Dict[formatted_time] = [[],[]]
        
        if row[1]in Dict[formatted_time][0]:       # 중복이 되는가?
            Dict[formatted_time][1] += row[2]      # 된다면 가격 추가
        else:
            Dict[formatted_time][0].append(row[1]) # 중복이 안되어 있다면
            Dict[formatted_time][1].append(row[2]) # 그냥 추가
    print(Dict)
finally:
    # 연결을 닫습니다.
    conn.close()