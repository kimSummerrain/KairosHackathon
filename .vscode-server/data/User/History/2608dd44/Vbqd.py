from flask import Flask, render_template
from test_M1 import List
import doeun_test 

app = Flask(__name__)

# 정적 파일을 서빙할 때 사용할 경로 및 폴더 설정
app.static_folder = "static"

# doeun_test.month_chart_data를 result에 할당
result = doeun_test.month_chart_data

@app.route("/")
def main():
    # 메인 화면
    return render_template("startscreen3.html", result=result)

@app.route("/calendar")
def calendar():
    # 캘린더 화면
    return render_template("calendar.html", data=List)

@app.route("/detail")
def detail():
    # 상세사항
    return render_template("detail.html", result=result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
    