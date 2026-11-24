// global values

const subjects = Object.keys(learningData);
const durations = Object.values(learningData)
const chartColors = ['#A2B99F', '#829B78', '#668C78', '#C5D5C0', '#526B5B'];

Chart.defaults.font.family = 'sans-serif';
Chart.defaults.color = '#E5EDE6';

const colors = subjects.map(
    (_, index) => chartColors[index % chartColors.length]
);

// bar chart

const bar = document.getElementById('bar-chart');

new Chart(bar, {
    type: 'bar',

  	data: {
    	labels: subjects,

        datasets: [{
            label: 'Time',
            data: durations,
            borderColor: colors,
            backgroundColor: colors,
            borderWidth: 1,
            borderRadius: 6,
            maxBarThickness: 55
        }]
    },

    options: {
        responsive: true,
        maintainAspectRatio: false,

        animation: {
            duration: 700
        },

        plugins: {
            legend: {
                display: false
            },

            tooltip: {
                backgroundColor: '#26372E',
                titleColor: '#E5EDE6',
                bodyColor: '#E5EDE6',
                borderColor: '#3A5042',
                borderWidth: 1,
                padding: 10,

                callbacks: {
                    label: function(context) {
                        return context.parsed.y + ' minutes';
                    }
                }
            }
        },

        scales: {
            x: {
                grid: {
                    display: false
                },
                ticks: {
                    color: '#E5EDE6',
                    maxRotation: 45
                }
            },

            y: {
                beginAtZero: true,

                title: {
                    display: true,
                    text: 'Minutes',
                    color: '#A2B99F'
                },

                grid: {
                    color: '#3A5042'
                },

                ticks: {
                    color: '#E5EDE6'
                },
            }
        }
    }
});

// pie chart

const pie = document.getElementById('pie-chart');

new Chart(pie, {
    type: 'pie',
    
    data: {
        labels: subjects,

        datasets: [{
            data: durations,
            borderColor: '#18231E',
            backgroundColor: chartColors,
            borderWidth: 2,
            hoverOffset: 8
        }]
    },

    options: {
        responsive: true,
        maintainAspectRatio: false,
    
        animation: {
            duration: 700
        },

        plugins: {
            legend: {
                position: 'bottom',
                
                labels: {
                    color: '#E5EDE6',
                    usePointStyle: true,
                    pointStyle: 'circle',
                    padding: 16
                }
            },
        
    
            tooltip: {
                backgroundColor: '#26372E',
                titleColor: '#E5EDE6',
                bodyColor: '#E5EDE6',
                borderColor: '#3A5042',
                borderWidth: 1,
                padding: 10,

                callbacks: {
                    label: function(context) {
                        const total = context.dataset.data.reduce(
                            (sum, value) => sum + value, 0
                        );

                        const percentage = (
                            context.parsed / total * 100
                        ).toFixed(1);

                        return `${context.label}: ${context.parsed} min (${percentage}%)`;
                    }
                }
            }
        }
    }
});