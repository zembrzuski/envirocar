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

        var dashboard_string = createDashboardString(resp);
        console.log(dashboard_string);
        $("div.main-dashboard").html(dashboard_string);


        /*
        // colocar tb o tipo de gasosa, para paoder comparar com o co2.
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
