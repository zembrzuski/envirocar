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
          if (maxspeed == -1) {
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




















        

        var vis = d3.select("#visualisation"),
            WIDTH = 500,
            HEIGHT = 200,
            MARGINS = {
                top: 20,
                right: 20,
                bottom: 20,
                left: 50
            },
            xScale = d3.scale.linear().range([MARGINS.left, WIDTH - MARGINS.right]).domain([0, 500]),
            yScale = d3.scale.linear().range([HEIGHT - MARGINS.top, MARGINS.bottom]).domain([0,100]),
            xAxis = d3.svg.axis().scale(xScale),
            yAxis = d3.svg.axis().scale(yScale);

            vis.append("svg:g")
              .attr("transform", "translate(0," + (HEIGHT - MARGINS.bottom) + ")")
              .call(xAxis);

            yAxis = d3.svg.axis()
              .scale(yScale)
              .orient("left");

            vis.append("svg:g")
              .attr("transform", "translate(" + (MARGINS.left) + ",0)")
              .call(yAxis);

          var lineGen = d3.svg.line()
              .x(function(d) {
                return xScale(d.index);
              })
              .y(function(d) {
                return yScale(d.phenomenons.Speed.value);
              })
              .interpolate("basis");;


            vis.append('svg:path')
              .attr('d', lineGen(coordinates))
              .attr('stroke', 'green')
              .attr('stroke-width', 2)
              .attr('fill', 'none');

          vis.append("svg:g")
              .attr("class","axis")
              .attr("transform", "translate(0," + (HEIGHT - MARGINS.bottom) + ")")
              .call(xAxis);
           
          vis.append("svg:g")
              .attr("class","axis")
              .attr("transform", "translate(" + (MARGINS.left) + ",0)")
              .call(yAxis);


    });
}
