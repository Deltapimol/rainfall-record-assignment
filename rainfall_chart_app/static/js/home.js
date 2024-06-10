// d3.csv('{{ rainfall_data|tojson }}', function (err, rows) {
//   function unpack(rows, key) {
//     return rows.map(function (row) {
//       return row[key];
//     });
//   }

//   var trace1 = {
//     type: 'scatter',
//     mode: 'lines',
//     name: 'AAPL High',
//     x: unpack(rows, 'time'),
//     y: unpack(rows, 'RG_A'),
//     line: { color: '#17BECF' },
//   };

//   var data = [trace1];

//   var layout = {
//     title: 'Rainfall Record',
//   };
//   Plotly.newPlot('chartDiv', data, layout);
// });
