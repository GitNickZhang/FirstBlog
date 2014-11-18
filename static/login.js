$(function(){
	// 登录和注册之间的切换
	$('.direct-to-register').click(function(){
		$('.login').css('display', 'none');
		$('.register').css('display', 'block');
	});
	$('.btn-back').click(function(){
		$('.login').css('display', 'block');
		$('.register').css('display', 'none');
	});

	// 表单验证插件
	$('.register').Validform();

	// 注册Ajax
	$('.btn-register-submit').click(function(){
		$.ajax({
			url: '/register/',
			data: {
				username: $('.username').val(),
				password1: $('.password1').val(),
				password2: $('.password2').val(),
			},
			type: 'POST',
			success: function(data){
				alert(data);
			}
		})
	});
})