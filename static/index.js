$(function(){
	$(".nav-item").find("a").hover(
		function(){
			$(this).css("opacity", "1");
		},
		function(){
			$(this).css("opacity", "0.8");
		}
		);

	$('.log-in').hover(
		function(){
			$('.user-menu').css('display', 'block');
		},
		function(){
			$('.user-menu').css('display', 'none');
		}
		);
})