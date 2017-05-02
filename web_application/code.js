var map;

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
      center: {lat: 0, lng: 0},
      zoom: 7,
      mapTypeId: 'terrain'
    });
}

function do_the_plotting(track_id) {

    /*
    map = new google.maps.Map(document.getElementById('map'), {
      center: {lat: 51.13344993777271, lng: 2.303557851685234},
      zoom: 7,
      mapTypeId: 'terrain'
    });
    */

    $.get('http://localhost:9200/envirocar/group/' + track_id, function(data) {
        alert('ae');
        console.log(data);
    });

    var flightPlanCoordinates = [
        {lat: 37.772, lng: -122.214, strokeColor: '#0000FF'},
        {lat: 21.291, lng: -157.821},
        {lat: -18.142, lng: 178.431},
        {lat: -27.467, lng: 153.027}
    ];

    var flightPath = new google.maps.Polyline({
        path: flightPlanCoordinates,
        geodesic: true,
        strokeColor: '#FF0000',
        strokeOpacity: 1.0,
        strokeWeight: 2
    });

    flightPath.setMap(map);
}
