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

        vel_max = resp['vel']['max'];

        console.log('vel_max: ' + vel_max);
        console.log('vel_med: ' + resp['vm']);

        //var dashboard_string = createDashboardString(resp);
        //console.log(dashboard_string);
        //$("div.main-dashboard").html(dashboard_string);

        for (i = 0 ; i < coordinates.length-1; i++) {
          a = coordinates[i];
          b = coordinates[i+1];

          var maxspeed = parseFloat(coordinates[i]['trace']['maxspeed']);
          var vel = parseFloat(coordinates[i]['phenomenons']['Speed']['value']);

          //kol = getColorForPercentage(1-vel/vel_max);

          kol = 'black';
          if (vel > maxspeed + maxspeed * 5/100) {
            kol = 'red';
          } else {
            kol = 'blue';
          }
          if (maxspeed == 0) {
            kol = 'yellow';
          }

          var flightPath_1 = new google.maps.Polyline({
            path: [a, b],
            geodesic: true,
            strokeColor: kol,
            strokeOpacity: 1.0,
            strokeWeight: 4
          });

          flightPath_1.setMap(map);
        }

        plot_speed_limit(coordinates);
        plot_speed_limit2(resp['consumption_scaled'], resp['rpm_scaled']);

    });
}
