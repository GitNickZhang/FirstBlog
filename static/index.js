$(function(){
	$(".nav-list-item").find("a").hover(
		function(){
			$(this).css("opacity", "1");
		},
		function(){
			$(this).css("opacity", "0.8");
		}
		);

	$(".log-in").find("a").hover(
		function(){
			$(this).css("opacity", "1");
		},
		function(){
			$(this).css("opacity", "0.5");
		}
		);

	if ($('.username').css('display') != null) {
		$('.log-in').html('<a href="/logout/">Log out</a>');
	};
})