var master_theme = {
    colors: ['#2b908f', '#90ee7e', '#f45b5b', '#7798BF', '#aaeeee', '#ff0066', '#eeaaee',
        '#55BF3B', '#DF5353', '#7798BF', '#aaeeee'],
    chart: {
        backgroundColor: {
            linearGradient: {x1: 0, y1: 0, x2: 1, y2: 1},
            stops: [
                [0, '#2a2a2b'],
                [1, '#3e3e40']
            ]
        },
        style: {
            fontFamily: '\'Unica One\', sans-serif'
        },
        plotBorderColor: '#606063'
    },
    title: {
        style: {
            color: '#E0E0E3',
            textTransform: 'uppercase',
            fontSize: '20px'
        }
    },
    subtitle: {
        style: {
            color: '#E0E0E3',
            textTransform: 'uppercase'
        }
    },
    xAxis: {
        gridLineColor: '#707073',
        labels: {
            style: {
                color: '#E0E0E3'
            }
        },
        lineColor: '#707073',
        minorGridLineColor: '#505053',
        tickColor: '#707073',
        title: {
            style: {
                color: '#A0A0A3'

            }
        }
    },
    yAxis: {
        gridLineColor: '#707073',
        labels: {
            style: {
                color: '#E0E0E3'
            }
        },
        lineColor: '#707073',
        minorGridLineColor: '#505053',
        tickColor: '#707073',
        tickWidth: 1,
        title: {
            style: {
                color: '#A0A0A3'
            }
        }
    },
    tooltip: {
        backgroundColor: 'rgba(0, 0, 0, 0.85)',
        style: {
            color: '#F0F0F0'
        }
    },
    plotOptions: {
        series: {
            dataLabels: {
                color: '#B0B0B3'
            }
        },
        boxplot: {
            fillColor: '#505053'
        },
        candlestick: {
            lineColor: 'white'
        },
        errorbar: {
            color: 'white'
        },
        marker: {
            enabled: false
        }
    },
    legend: {
        itemStyle: {
            color: '#E0E0E3'
        },
        itemHoverStyle: {
            color: '#FFF'
        },
        itemHiddenStyle: {
            color: '#606063'
        }
    },
    credits: {
        style: {
            color: '#666'
        }
    },
    labels: {
        style: {
            color: '#707073'
        }
    },

    drilldown: {
        activeAxisLabelStyle: {
            color: '#F0F0F3'
        },
        activeDataLabelStyle: {
            color: '#F0F0F3'
        }
    },

    navigation: {
        buttonOptions: {
            symbolStroke: '#DDDDDD',
            theme: {
                fill: '#505053'
            }
        }
    },

    // scroll charts
    rangeSelector: {
        buttonTheme: {
            fill: '#505053',
            stroke: '#000000',
            style: {
                color: '#CCC'
            },
            states: {
                hover: {
                    fill: '#707073',
                    stroke: '#000000',
                    style: {
                        color: 'white'
                    }
                },
                select: {
                    fill: '#000003',
                    stroke: '#000000',
                    style: {
                        color: 'white'
                    }
                }
            }
        },
        inputBoxBorderColor: '#505053',
        inputStyle: {
            backgroundColor: '#333',
            color: 'silver'
        },
        labelStyle: {
            color: 'silver'
        }
    },

    navigator: {
        handles: {
            backgroundColor: '#666',
            borderColor: '#AAA'
        },
        outlineColor: '#CCC',
        maskFill: 'rgba(255,255,255,0.1)',
        series: {
            color: '#7798BF',
            lineColor: '#A6C7ED'
        },
        xAxis: {
            gridLineColor: '#505053'
        }
    },

    scrollbar: {
        barBackgroundColor: '#808083',
        barBorderColor: '#808083',
        buttonArrowColor: '#CCC',
        buttonBackgroundColor: '#606063',
        buttonBorderColor: '#606063',
        rifleColor: '#FFF',
        trackBackgroundColor: '#404043',
        trackBorderColor: '#404043'
    },

    // special colors for some of the
    legendBackgroundColor: 'rgba(0, 0, 0, 0.5)',
    background2: '#505053',
    dataLabelsColor: '#B0B0B3',
    textColor: '#C0C0C0',
    contrastTextColor: '#F0F0F3',
    maskColor: 'rgba(255,255,255,0.3)'
};

function populate_cloud_stats(json) {
    $("#ec2_total").empty();
    var ec2s = json["total"];
    for (var i = 0; i < ec2s.length; i++) {
        var ec2 = ec2s[i];
        var line = "<tr><td>" + ec2["id"] + "</td><td>" + ec2["cpu"] + "</td><td>" + ec2["memory"] + "</td ><td>" + ec2["storage"] + "</td></tr>";
        $("#ec2_total").append(line);
    }
}

function ec2_data(json) {
    console.log(json);
    $("#ec2_name").text(json["id"]);
    $("#hostname").text("Hostname: " + json["metadata"]["hostname"]);
    $("#os").text("OS: " + json["metadata"]["os"]);
    $("#type").text("Type: " + json["metadata"]["type"]);
    $("#cpu").text("Number of CPUs: " + json["metadata"]["num_cpu"]);
    $("#ip").text("IP: " + json["metadata"]["ip"]);

    $("#top_cpu").empty();
    $("#top_mem").empty();
    for (var i = 0; i < json["top_25_cpu"].length; i++) {
        var place = '<li class="list-group-item"><h4>' + json['top_25_cpu'][i]["name"] + "</h4>";
        place = place + "<br><h4>Command: " + json['top_25_cpu'][i]["command_line"].join(" ");
        place = place + '</h4><div class="table-responsive" >' +
            '<table class="table table-striped">' +
            '<thead><tr>' +
            '<th>PID</th>' +
            '<th>CPU %</th>' +
            '<th>Memory %</th>' +
            '<th>Thread Count</th>' +
            '</tr></thead>' +
            "<tbody>" +
            '<tr>' +
            '<td>' + json['top_25_cpu'][i]["pid"] + '</td>' +
            '<td>' + json['top_25_cpu'][i]["cpu"].toFixed(2) + '</td>' +
            '<td>' + json['top_25_cpu'][i]["memory"].toFixed(2) + '</td>' +
            '<td>' + json['top_25_cpu'][i]["threads"] + '</td>' +
            '</tr>' +
            "</tbody>" +
            '</table>';
        place = place + '</div>';
        place = place + "<h4>Flagged for: </h4>" + json['top_25_cpu'][i]["justification"] + "<br>";
        place = place + "<h4>Recommendation: </h4> " + json['top_25_cpu'][i]["recommendation"] + "<br>";
        place = place + "</li>";
        $("#top_cpu").append(place);
    }

    for (var i = 0; i < json["top_25_mem"].length; i++) {
        var place = '<li class="list-group-item"><h4>' + json['top_25_mem'][i]["name"] + "</h4>";
        place = place + "<br><h4>Command: " + json['top_25_mem'][i]["command_line"].join(" ");
        place = place + '</h4><div class="table-responsive" >' +
            '<table class="table table-striped">' +
            '<thead><tr>' +
            '<th>PID</th>' +
            '<th>CPU %</th>' +
            '<th>Memory %</th>' +
            '<th>Thread Count</th>' +
            '</tr></thead>' +
            "<tbody>" +
            '<tr>' +
            '<td>' + json['top_25_mem'][i]["pid"] + '</td>' +
            '<td>' + json['top_25_mem'][i]["cpu"].toFixed(2) + '</td>' +
            '<td>' + json['top_25_mem'][i]["memory"].toFixed(2) + '</td>' +
            '<td>' + json['top_25_mem'][i]["threads"] + '</td>' +
            '</tr>' +
            "</tbody>" +
            '</table>';
        place = place + '</div>';
        place = place + "<h4>Flagged for: </h4>" + json['top_25_mem'][i]["justification"] + "<br>";
        place = place + "<h4>Recommendation: </h4> " + json['top_25_mem'][i]["recommendation"] + "<br>";
        place = place + "</li>";
        $("#top_mem").append(place);
    }

    $("#bot_cpu").empty();
    $("#bot_mem").empty();

    for (var i = 0; i < json["bottom_25_cpu"].length; i++) {
        var place = '<li class="list-group-item"><h4>' + json['bottom_25_cpu'][i]["name"] + "</h4>";
        place = place + "<br><h4>Command: " + json['bottom_25_cpu'][i]["command_line"].join(" ");
        place = place + '</h4><div class="table-responsive" >' +
            '<table class="table table-striped">' +
            '<thead><tr>' +
            '<th>PID</th>' +
            '<th>CPU %</th>' +
            '<th>Memory %</th>' +
            '<th>Thread Count</th>' +
            '</tr></thead>' +
            "<tbody>" +
            '<tr>' +
            '<td>' + json['bottom_25_cpu'][i]["pid"] + '</td>' +
            '<td>' + json['bottom_25_cpu'][i]["cpu"].toFixed(2) + '</td>' +
            '<td>' + json['bottom_25_cpu'][i]["memory"].toFixed(2) + '</td>' +
            '<td>' + json['bottom_25_cpu'][i]["threads"] + '</td>' +
            '</tr>' +
            "</tbody>" +
            '</table>';
        place = place + '</div>';
        place = place + "<h4>Flagged for: </h4>" + json['bottom_25_cpu'][i]["justification"] + "<br>";
        place = place + "<h4>Recommendation: </h4> " + json['bottom_25_cpu'][i]["recommendation"] + "<br>";
        place = place + "</li>";
        $("#bot_cpu").append(place);
    }

    for (var i = 0; i < json["bottom_25_mem"].length; i++) {
        var place = '<li class="list-group-item"><h4>' + json['bottom_25_mem'][i]["name"] + "</h4>";
        place = place + "<br><h4>Command: " + json['bottom_25_mem'][i]["command_line"].join(" ");
        place = place + '</h4><div class="table-responsive" >' +
            '<table class="table table-striped">' +
            '<thead><tr>' +
            '<th>PID</th>' +
            '<th>CPU %</th>' +
            '<th>Memory %</th>' +
            '<th>Thread Count</th>' +
            '</tr></thead>' +
            "<tbody>" +
            '<tr>' +
            '<td>' + json['bottom_25_mem'][i]["pid"] + '</td>' +
            '<td>' + json['bottom_25_mem'][i]["cpu"].toFixed(2) + '</td>' +
            '<td>' + json['bottom_25_mem'][i]["memory"].toFixed(2) + '</td>' +
            '<td>' + json['bottom_25_mem'][i]["threads"] + '</td>' +
            '</tr>' +
            "</tbody>" +
            '</table>';
        place = place + '</div>';
        place = place + "<h4>Flagged for: </h4>" + json['bottom_25_mem'][i]["justification"] + "<br>";
        place = place + "<h4>Recommendation: </h4>" + json['bottom_25_mem'][i]["recommendation"] + "<br>";
        place = place + "</li>";
        $("#bot_mem").append(place);
    }

    if (json["instance_recs"]["justification"] != "DO_NOT_USE") {
        var build = '<div class="panel-heading" style="background-color:#222222"><h3 style="text-align:center;color:white">Cost Optimization</h3>' +
            '</div><div class="panel-body">' +
            '<div class="col-xs-6"><h4>Optimization:</h4>'+json["instance_recs"]["recommendation"]+'</div>' + '<div class="col-xs-6"><h4>Configuration Limitations: </h4>'+json["instance_recs"]["justification"]+'</div>'+
            '</div>';
        $("#recs").append(build);
        console.log(build);
    }
}

function draw_instance_metrics(data, name) {
    Highcharts.theme = master_theme;
    Highcharts.chart('total', Highcharts.merge(Highcharts.theme, {

        title: {
            text: 'System Resource Utilization:  ' + name
        },

        yAxis: {
            title: {
                text: 'Percentage of System Utilization'
            }
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle'
        },

        plotOptions: {
            series: {
                pointStart: 2010
            },
            line: {
                marker: {
                    enabled: false
                },
                animation: false
            }

        },

        series: data

    }));
}


$(document).ready(function () {


    $.get("/get_instance_details/?instance=" + $("#ec2_id").attr("data-id"), function (res) {
        ec2_data(res);
    });

    setInterval(function () {
        $.get("/get_time_series/?instance=" + $("#ec2_id").attr("data-id"), function (res) {
            var draw = [];
            console.log(res);
            draw.push({"name": "CPU", "data": res["CPU"]});
            draw.push({"name": "Memory", "data": res["MEM"]});
            draw.push({"name": "Disk Read-Write", "data": res["STORAGE"]});
            draw.push({"name": "Swap Usage", "data": res["SWAP"]});
            draw_instance_metrics(draw, res["id"])
        });
    }, 3000);


});

