$(function(){
	$('.direct-to-register').click(function(){
		$('.login').css('display', 'none');
		$('.register').css('display', 'block');
	});

	$('.btn-back').click(function(){
		$('.login').css('display', 'block');
		$('.register').css('display', 'none');
	});
})