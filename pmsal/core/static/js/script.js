$(document).ready(function() {
	// Contact Maps
	$("#maps").gmap3({
		map: {
			options: {
			  center: [-8.975889, -36.688288],
			  zoom: 16,
			  scrollwheel: false
			}
		 },
		marker:{
			latLng: [-8.975889, -36.688288],
			options: {
			 icon: new google.maps.MarkerImage(
			   "https://dl.dropboxusercontent.com/u/29545616/Preview/marker.png",
			   new google.maps.Size(48, 48, "px", "px")
			 )
			}
		 }
	});

	var height = $("#topbar").height();
	$("div.navbar").attr("data-offset-top", function(){
		return ""+height;
	});

	$(".gallery").fancybox({
		openEffect  : 'none',
		closeEffect	: 'none',

		helpers : {
			title : {
				type : 'over'
			}
		}
	});

	$(".gallery2").fancybox({
		wrapCSS    : 'fancybox-custom',
		closeClick : true,

		closeEffect	: 'elastic',

		helpers : {
			title : {
				type : 'inside'
			},
			overlay : {
				css : {
					'background' : 'rgba(238,238,238,0.85)'
				}
			}
		}
	});

	$(".galeri").fancybox({
		wrapCSS    : 'fancybox-custom',
		closeClick : true,
		openEffect : 'none',
		closeEffect	: 'elastic',

		helpers : {
			title : {
				type : 'inside'
			},
			overlay : {
				css : {
					'background' : 'rgba(238,238,238,0.85)'
				}
			}
		}
	});


	//Slider
	$("#homeslider").carousel({
		interval: 5000
	});

	$("#workslider").carousel({
		interval: 4000
	});
});
