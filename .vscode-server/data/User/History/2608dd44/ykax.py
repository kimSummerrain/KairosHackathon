from flask import Flask, render_template
from test_M1 import List
import doeun_test 

app = Flask(__name__)

# 정적 파일을 서빙할 때 사용할 경로 및 폴더 설정
app.static_folder = "static"


@app.route("/")
def main():
    # 메인 화면
    return render_template("startscreen.html")

@app.route("/calendar")
def calendar():
    # 캘린더 화면
    return render_template("calendar.html")

@app.route("/detail")
def detail():
    # 상세사항
    # doeun_test.month_chart_data를 result에 할당
    result = []
    result = doeun_test.month_chart_data
    return render_template("detail.html", result=result)

@app.route("/h")
def calendar999():
    return render_template("calendar999.html", data=List)



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
    