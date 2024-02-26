const ctx = document.getElementById('myChart');

new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: ['식당', '쇼핑', '취미', '교통', '기타'],
        datasets: [{
            label: '# of Votes',
            data: [23, 7, 10, 30, 15],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});