$(document).ready(function() {
    
    $("#dashboard-text").hide();
    $("#dashboard-charts").hide();
    $("#dashboard-rota").hide();

    $( "#dashboard-texto-button" ).click(function() {
  		$("#dashboard-charts").hide("fast", function(){});
  		$("#dashboard-rota").hide("fast", function(){});
  		$("#dashboard-text").show("fast", function(){});
	});

    $( "#dashboard-graficos-button" ).click(function() {
    	$("#dashboard-text").hide("fast", function(){});
    	$("#dashboard-rota").hide("fast", function(){});
  		$("#dashboard-charts").show("fast", function(){});
	});

    $( "#dashboard-rota-button" ).click(function() {
    	$("#dashboard-text").hide("fast", function(){});
    	$("#dashboard-charts").hide("fast", function(){});
    	$("#dashboard-rota").show("fast", function(){});
	});

});
