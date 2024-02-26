// 현재 날짜를 가져와서 표시하는 함수
function displayDate() {
    var today = new Date(); // 현재 날짜 및 시간 가져오기
    var month = today.getMonth() + 1; // 월 가져오기 (0부터 시작하므로 +1)
    var day = today.getDate(); // 일 가져오기
    var dayOfWeek = today.toLocaleDateString('en-US', { weekday: 'long' }); // 요일 가져오기
    var hour = today.getHours(); // 시간 가져오기
    var minute = today.getMinutes(); // 분 가져오기

    minute = minute < 10 ? '0' + minute : minute;

    // HTML 요소에 날짜와 요일 표시
    document.getElementById('date').innerHTML = month + '월 ' + day + '일 ' + dayOfWeek;
    document.getElementById('time').innerHTML = hour + ':' + minute;
    document.getElementById('month').innerHTML = month + '월 지출 내역은?';
    document.getElementById('month').innerHTML = month + '원';
}

// 페이지가 로드될 때 displayDate 함수 실행
window.onload = function () {
    // 매 초마다 updateDateTime 함수를 호출하여 시간을 업데이트
    setInterval(displayDate, 1000); // 1000ms = 1초
    // 최초 로드시 한번 호출하여 초기화
    displayDate();
};