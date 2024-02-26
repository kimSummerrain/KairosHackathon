const ctx = document.getElementById('myChart');

new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: ['음식', '교통', '의료', '쇼핑', '교육', '기타'],
        datasets: [{
            label: '# of Votes',
            data: [23, 7, 10, 30, 15, 15],
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