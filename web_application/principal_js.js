var map;

function initMap() {
    var track_id = location.pathname.split("/map/")[1];
    var flightPlanCoordinates;

    $.get('http://127.0.0.1:5000/find_track/' + track_id, function(data) {
        resp = JSON.parse(data);
        map = new google.maps.Map(document.getElementById('map'), {
          center: resp['center'],
          zoom: 13,
          mapTypeId: 'terrain',
          styles: map_styles
        });

        coordinates = resp['coordinates'];
        phenomenons = resp['phenomenons'];

        vel_max = resp['vel']['max'];

        // colocar tb o tipo de gasosa, para paoder comparar com o co2.

        dashboard_string =
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
            "</ul> <br/>"
        ;

        $("div.main-dashboard").html(dashboard_string);


        /*
        - graficozinhos relacionando cada uma das coisas visualizadas no mapa.
        Rpm
        Engine Load
        time inicio
        time fim
        --- procurar, tb, aqueles heatmaps.


        partes mais de inteligencia.
            - dada uma rota, quero saber quais os carros que passaram por ali.
            - dado um ponto (exemplo, porto alegre), saber quais carros
              passaram por ali.
            - tentar identificar quais são os usuários das rotas.s

        -- tb posso pegar os dados do cara para ver se ele está
           acima ou abaixo do limite de velocidade.
        */


        for (i = 0 ; i < coordinates.length-1; i++) {
          a = coordinates[i];
          b = coordinates[i+1];

          var vel = phenomenons[i]['Speed']['value'];
          kol = getColorForPercentage(1-vel/vel_max);

          var flightPath_1 = new google.maps.Polyline({
            path: [a, b],
            geodesic: true,
            strokeColor: kol,
            strokeOpacity: 1.0,
            strokeWeight: 4
          });

          flightPath_1.setMap(map);
        }
    });
}
