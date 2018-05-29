/**
 * Created by Eggie on 5/8/18.
 */

// Load the Visualization API and the piechart package.
google.charts.load('current', {'packages': ['corechart']});

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(drawChart);

function reformat_Hashtag_Data(jsonData){
    var temp= jsonData.Hashtag_count;
    console.log("temp: " + JSON.stringify(temp));
    var result = [];
    var i;
    var row;
    for (i=0; i < temp.length; ++i){
        row= temp[i]
        dataElement = [];
        dataElement.push(row.hashtag);
        dataElement.push(row.count);
        result.push(dataElement);
    }
    console.log("Data: " + JSON.stringify(result));
    return result;
}

function reformat_Messages_Data(jsonData) {
    var temp = jsonData.Message_count;
    console.log("temp: " + JSON.stringify(temp));
    var result = [];
    var i;
    var row;
    for (i = 0; i < temp.length; ++i) {
        row = temp[i]
        dataElement = [];
        dataElement.push(row.date);
        dataElement.push(row.count);
        result.push(dataElement);
    }
    console.log("Data: " + JSON.stringify(result));
    return result;
}

function drawChart() {
    var jsonData = $.ajax({
        url: "http://localhost:5000/MessageApp/dashboard/toptenhashtags",
        dataType: "json",
        async: false
    }).responseText;

    console.log("jsonData: " + JSON.parse(jsonData));

    // Create our data table out of JSON data loaded from server.
    var Hash_data = new google.visualization.DataTable();
    Hash_data.addColumn('string', 'hashtag');
    Hash_data.addColumn('number', 'Tags');
    Hash_data.addRows(reformatData(JSON.parse(jsonData)));

    // Create our data table out of JSON data loaded from server.
    var Mess_data = new google.visualization.DataTable();
    Mess_data.addColumn('string', 'Date');
    Mess_data.addColumn('number', 'Messages');
    Mess_data.addRows(reformatData(JSON.parse(jsonData)));

    var Hash_options = {
        title: 'Trending Topics',
        width: 400,
        height: 300,
        chartArea: {width: '50%'},
        hAxis: {
            title: 'Hashtag',
            minValue: 0
        },
        vAxis: {
            title: 'Messages Tagged'
        }
    };
    var Hash_chart = new google.visualization.ColumnChart(document.getElementById('hashtag_chart_div'));
    Hash_chart.draw(Hash_data, Hash_options);

    var Mess_options = {
        title: 'Messages Per Day',
        width: 400,
        height: 300,
        chartArea: {width: '50%'},
        hAxis: {
            title: 'Date',
            minValue: 0
        },
        vAxis: {
            title: 'Total Messages Posted'
        }
    };
    var Mess_chart = new google.visualization.ColumnChart(document.getElementById('message_chart_div'));
    Mess_chart.draw(Mess_data, Mess_options)
}


