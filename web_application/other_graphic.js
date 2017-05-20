function plot_speed_limit2(first, second) {

  var vis = d3.select("#visualisation2"),
      WIDTH = 600,
      HEIGHT = 200,
      MARGINS = {
          top: 20,
          right: 20,
          bottom: 20,
          left: 50
      },
      xScale = d3.scale.linear().range([MARGINS.left, WIDTH - MARGINS.right]).domain([0, 500]),
      yScale = d3.scale.linear().range([HEIGHT - MARGINS.top, MARGINS.bottom]).domain([0,1]),
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

    var speed = d3.svg.line()
        .x(function(d) {
          return xScale(d.index);
        })
        .y(function(d) {
          return yScale(d.value);
        })
        .interpolate("basis");;


    var maxSpeed = d3.svg.line()
        .x(function(d) {
          return xScale(d.index);
        })
        .y(function(d) {
          return yScale(d.value);
        })
        .interpolate("basis");;

      vis.append('svg:path')
        .attr('d', speed(first))
        .attr('stroke', 'green')
        .attr('stroke-width', 1)
        .attr('fill', 'none');

      vis.append('svg:path')
        .attr('d', maxSpeed(second))
        .attr('stroke', 'blue')
        .attr('stroke-width', 1)
        .attr('fill', 'none');


    vis.append("svg:g")
        .attr("class","axis")
        .attr("transform", "translate(0," + (HEIGHT - MARGINS.bottom) + ")")
        .call(xAxis);
     
    vis.append("svg:g")
        .attr("class","axis")
        .attr("transform", "translate(" + (MARGINS.left) + ",0)")
        .call(yAxis);

}
