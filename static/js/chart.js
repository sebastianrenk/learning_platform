const pie = document.getElementById('pie_chart');

let keys = Object.keys(learningData);
let values = Object.values(learningData)
const pieColors = ['#18231E', '#26372E', '#A2B99F', '#E5EDE6', '#3A5042'];

new Chart(pie, {
  type: 'pie',
  data: {
    labels: keys,
    datasets: [{
      label: 'Time per subject',
      data: values,
      borderWidth: 1.5,
      borderColor: '#3A5042',
      backgroundColor: pieColors,
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
      y: {
        beginAtZero: true
      }
    }
  }
});

const bar = document.getElementById('bar-chart');

new Chart(bar, {
  type: 'bar',
  data: {
    labels: keys,
    datasets: [{
      label: 'Time per subject',
      data: values,
      borderWidth: 1.5,
      borderColor: '#3A5042',
      backgroundColor: pieColors
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
      y: {
        beginAtZero: true
      }
    }
  }
});