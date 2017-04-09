function populate_cloud_stats(json) {
    $("#ec2_total").empty();
        function dynamicSort(property) {
        var sortOrder = 1;
        if(property[0] === "-") {
            sortOrder = -1;
            property = property.substr(1);
        }
        return function (a,b) {
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
            window.location.href = "/ec2/?instance="+$(this)[0]["id"];
        });
    }
}

$(document).ready(function () {
    $.get("/get_instances_summary/", populate_cloud_stats);
    setInterval(function () {
        $.get("/get_instances_summary/", populate_cloud_stats);
    }, 5000);
});
