from flask import Flask, render_template
import pymysql.cursors
from datetime import datetime

app = Flask(__name__)

# MySQL 데이터베이스에 연결하는 함수
def connect_to_database():
    return pymysql.connect(
        host='localhost',          # 호스트 주소
        user='root',               # 사용자 이름
        password='ScE1234**',      # 비밀번호
        db='client_information',   # 데이터베이스 이름
        charset='utf8mb4',         # 문자 인코딩 설정
        cursorclass=pymysql.cursors.DictCursor
    )

# 데이터베이스에서 데이터를 가져오는 함수
def get_data_from_database():
    conn = connect_to_database()
    try:
        with conn.cursor() as cursor:
            # SQL 쿼리를 실행하여 모든 결과를 가져옵니다.
            sql = 'SELECT * FROM Expenditures'
            cursor.execute(sql)
            results = cursor.fetchall()

            # 데이터를 처리하고 원하는 형태로 반환합니다.
            data = {}
            for row in results:
                time_value = row['time_column']  # 예시에서 시간 값이 'time_column' 열에 있다고 가정합니다.
                formatted_time = datetime.strftime(time_value, "%Y-%m-%d")  # 년-월-일 형식으로 변환
                if formatted_time not in data:
                    data[formatted_time] = {'titles': [], 'prices': []}
                data[formatted_time]['titles'].append(row['title_column'])
                data[formatted_time]['prices'].append(row['price_column'])
                print(data)

            return data
    finally:
        conn.close()

@app.route('/calendar')
def calendar():
    data = get_data_from_database()  # 데이터베이스에서 데이터를 가져옵니다.
    return render_template('calendat2.html', data=data)  # calendar2.html을 렌더링하고 데이터를 전달합니다.

if __name__ == '__main__':
    app.run(debug=True)