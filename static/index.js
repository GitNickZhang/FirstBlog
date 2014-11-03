$(function(){
	$(".nav-item").find("a").hover(
		function(){
			$(this).css("opacity", "1");
		},
		function(){
			$(this).css("opacity", "0.8");
		}
		);
})