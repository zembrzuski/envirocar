var map;


function plota(track_id, instantiate_map) {

    $.get('http://127.0.0.1:5000/find_track/' + track_id, function(data) {
        resp = JSON.parse(data);

        if (instantiate_map) {
            map = new google.maps.Map(document.getElementById('map'), {
              center: resp['center'],
              zoom: 8,
              mapTypeId: 'terrain'
              //, styles: map_styles
            });

            return;
        }

        coordinates = resp['coordinates'];

        vel_max = resp['vel']['max'];

        var dashboard_string = createDashboardString(resp);
        console.log(dashboard_string);
        $("div.dashboard-text").html(dashboard_string);
        $("#dashboard-rota").html(resp['all_streets']);

        for (i = 0 ; i < coordinates.length-1; i++) {
          a = coordinates[i];
          b = coordinates[i+1];

          var vel = parseFloat(coordinates[i]['phenomenons']['GPS Speed']['value']);

          // kol = getColorForPercentage(1-vel/vel_max);
          kol = 'black';

          var flightPath_1 = new google.maps.Polyline({
            path: [a, b],
            geodesic: true,
            strokeColor: kol,
            strokeOpacity: 0.1,
            strokeWeight: 2
          });

          flightPath_1.setMap(map);
        }

        plot_speed_limit(coordinates);
        plot_speed_limit2(resp['consumption_scaled'], resp['rpm_scaled']);

    });
}


function initMap() {
    var track_id = location.pathname.split("/map/")[1];
    plota(track_id, true)
}
