
var createDashboardString = function(resp) {
    var mystring =
            "velocidade:" +
            "<ul>" +
            "<li>maxima: " + resp['vel']['max'].toFixed(2) + " " + resp['vel']['unit'] + "</li>" +
            "<li>media: "  + resp['vel']['med'].toFixed(2) + " " + resp['vel']['unit'] + "</li>" +
            "<li>minima: " + resp['vel']['min'].toFixed(2) + " " + resp['vel']['unit'] + "</li>" +
            "</ul> <br/>" +

            "co2:" +
            "<ul>" +
            "<li>maxima: " + resp['co2']['max'].toFixed(2) + " " + resp['co2']['unit'] + "</li>" +
            "<li>media: "  + resp['co2']['med'].toFixed(2) + " " + resp['co2']['unit'] + "</li>" +
            "<li>minima: " + resp['co2']['min'].toFixed(2) + " " + resp['co2']['unit'] + "</li>" +
            "</ul> <br/>" +

            "rpm:" +
            "<ul>" +
            "<li>maxima: " + resp['rpm']['max'].toFixed(2) + " " + resp['rpm']['unit'] + "</li>" +
            "<li>media: "  + resp['rpm']['med'].toFixed(2) + " " + resp['rpm']['unit'] + "</li>" +
            "<li>minima: " + resp['rpm']['min'].toFixed(2) + " " + resp['rpm']['unit'] + "</li>" +
            "</ul> <br/>" +

            "engine load:" +
            "<ul>" +
            "<li>maxima: " + resp['engine-load']['max'].toFixed(2) + " " + resp['engine-load']['unit'] + "</li>" +
            "<li>media: "  + resp['engine-load']['med'].toFixed(2) + " " + resp['engine-load']['unit'] + "</li>" +
            "<li>minima: " + resp['engine-load']['min'].toFixed(2) + " " + resp['engine-load']['unit'] + "</li>" +
            "</ul> <br/>" +

            "deslocamento:" +
            "<ul>" +
            "<li>inicio: " + resp['tempo-inicio'] + "</li>" +
            "<li>fim: " + resp['tempo-fim'] + "</li>" +
            "<li>duracao: " + resp['duracao'] + "</li>" +
            "<li>vm: " + resp['vm'].toFixed(2) + "km/h</li>" +
            "<li>distancia total: " + resp['total-distance'].toFixed(2) + "km </li>" +
            "<li>distancia linha reta: " + resp['linha-reta-distance'].toFixed(2) + "km </li>" +
            "</ul> <br/>";
        return mystring;
}
