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
	var csrftoken = $.cookie('csrftoken');

	function csrfSafeMethod(method) {
		// these HTTP methods do not require CSRF protection
		return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}
	$.ajaxSetup({
	    crossDomain: false, // obviates need for sameOrigin test
	    beforeSend: function(xhr, settings) {
	        if (!csrfSafeMethod(settings.type)) {
	            xhr.setRequestHeader("X-CSRFToken", csrftoken);
	        }
	    }
	});

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