from flask import Flask, render_template
from test_M1 import Dict

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
    return render_template("detail.html")

@app.route("/h")
def calendar999():
    # 캘린더 화면 -> 태랑
    return render_template("calendar999.html", data=('2023-03-12',sum(Dict['2023-03-12'][1])))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
    