// function to animate txt on home page
var textWrapper = document.querySelector('.ml14 .letters');
textWrapper.innerHTML = textWrapper.textContent.replace(/\S/g, "<span class='letter'>$&</span>");

anime.timeline({loop: true})
  .add({
    targets: '.ml14 .line',
    scaleX: [0,1],
    opacity: [0.5,1],
    easing: "easeInOutExpo",
    duration: 900
  }).add({
    targets: '.ml14 .letter',
    opacity: [0,1],
    translateX: [40,0],
    translateZ: 0,
    scaleX: [0.3, 1],
    easing: "easeOutExpo",
    duration: 800,
    offset: '-=600',
    delay: (el, i) => 150 + 25 * i
  }).add({
    targets: '.ml14',
    opacity: 0,
    duration: 1000,
    easing: "easeOutExpo",
    delay: 1000
  });

/* parallax image resize */

  /* resize the image(s) on page load */
	$(document).ready(function() {
		resize_all_parallax();
	});

	/* resize the image(s) on page resize */
	$(window).on('resize', function(){
		resize_all_parallax();
	});

	
	function resize_all_parallax() {
		var div_id = 'img1,' + 'img2'; 
		var img_w = 1000; /* the width of your image, in pixels */
		var img_h = 864; /* the height of your image, in pixels */
		resize_parallax(div_id,img_w,img_h);
	}

	/* this resizes the parallax image down to an appropriate size for the viewport */
	function resize_parallax(div_id,img_w,img_h) {
		var div = $('#' + div_id);
		var divwidth = div.width();
		if (divwidth < 769) { var pct = (img_h/img_w) * 105; } /* show full image, plus a little padding, if on static mobile view */
		else { var pct = 60; } /* this is the HEIGHT as percentage of the current div WIDTH. you can change it to show more (or less) of your image */
		var newheight = Math.round(divwidth * (pct/100));
		newheight = newheight  + 'px';
		div.height(newheight);
	}