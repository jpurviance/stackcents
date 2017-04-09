/**
 * Created by John on 4/8/17.
 */


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
        plotBorderColor: '#606063',

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
            },
            marker: {
                lineColor: '#333'
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
    function dynamicSort(property) {
        var sortOrder = 1;
        if (property[0] === "-") {
            sortOrder = -1;
            property = property.substr(1);
        }
        return function (a, b) {
            var result = (a[property] < b[property]) ? -1 : (a[property] > b[property]) ? 1 : 0;
            return result * sortOrder;
        }
    }

    var ec2s = json["total"];
    ec2s.sort(dynamicSort("id"));
    for (var i = 0; i < ec2s.length; i++) {
        var ec2 = ec2s[i];
        var line = "<tr id=" + ec2["id"] + "><td>" + ec2["id"] + "</td><td>" + ec2["cpu"] + "</td><td>" + ec2["memory"] + "</td ><td>" + ec2["storage"] + "</td></tr>";
        $("#ec2_total").append(line);
        $("#" + ec2["id"]).click(function (event) {
            window.location.href = "/ec2/?instance=" + $(this)[0]["id"];
        });
    }
}

function draw_multi_chart(data) {
    Highcharts.theme = master_theme;
    return Highcharts.chart('total', Highcharts.merge(Highcharts.theme, {

        title: {
            text: "AWS Cluster Resource Consumption"
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
            }, line: {
                animation: false
            }
        },

        series: data

    }));
}

var chart;

$(document).ready(function () {

    Highcharts.theme = master_theme;
    $.get("/get_instances_summary/", populate_cloud_stats);
    setInterval(function () {
        $.get("/get_instances_summary/", populate_cloud_stats);
    }, 5000);
    $.get("/get_all_time_series/", function (data) {
        var draw = [];
        draw.push({"name": "CPU", "data": data["CPU"]});
        draw.push({"name": "Memory", "data": data["MEM"]});
        draw.push({"name": "Disk Read-Write", "data": data["STORAGE"]});
        draw.push({"name": "Swap Usage", "data": data["SWAP"]});
        chart = draw_multi_chart(draw);
    });

    setInterval(function () {
        // $("#total_wrapper").empty();
        // $("#total_wrapper").append('<div id="total" style="min-width: 310px; height: 400px; margin: 0 auto"></div>');
        $.get("/get_all_time_series/", function (data) {
            var draw = [];
            draw.push({"name": "CPU", "data": data["CPU"]});
            draw.push({"name": "Memory", "data": data["MEM"]});
            draw.push({"name": "Disk Read-Write", "data": data["STORAGE"]});
            draw.push({"name": "Swap Usage", "data": data["SWAP"]});
            chart = draw_multi_chart(draw);
        });
    },3000);

});

