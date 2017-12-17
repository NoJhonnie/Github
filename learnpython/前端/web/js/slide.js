$(function(){
	
	var $li = $('.slide_pics li');
	var len = $li.length;       //获取li的长度
	var $prev = $('.prev');     //获取上一张的div
	var $next = $('.next');     //获取下一张的div


	//将要运动过来的li
	var nowli = 0;

	//当前要离开的li
	var prevli = 0;

	var timer = null;



	$li.not(':first').css({left:760});  //不是第一张的放在右侧760位置

	$li.each(function(index){

		var $sli = $('<li>');   //创建li元素

		if(index==0)        //如果是当前li，则添加active的class
		{
			$sli.addClass('active');
		}

		$sli.appendTo('.points')    //将li加在points里面

	})

	$points = $('.points li');      //取出points下有多少li


	$points.click(function(){
		nowli = $(this).index();

		if(nowli==prevli){
			return;
		}

		move();
		$(this).addClass('active').siblings().removeClass('active');
	});


	$prev.click(function(){
		nowli--;
		move();
		$points.eq(nowli).addClass('active').siblings().removeClass('active');	

	})

	$next.click(function(){
		nowli++;
		move();
		$points.eq(nowli).addClass('active').siblings().removeClass('active');	

	})

	$('.slide').mouseenter(function() {
		clearInterval(timer);
	});

	$('.slide').mouseleave(function() {
		timer = setInterval(autoplay,2000);
	});



	timer = setInterval(autoplay,2000);
    
    //自动播放图片
	function autoplay(){
		nowli++;
		move();
		$points.eq(nowli).addClass('active').siblings().removeClass('active');
	}

    //图片移动方法
	function move(){

		if(nowli<0)
		{
			nowli = len-1;
			prevli = 0;
			$li.eq(nowli).css({left:-760});
			$li.eq(prevli).stop().animate({left:760});
			$li.eq(nowli).stop().animate({left:0});
			prevli=nowli;
			return;
		}

		if(nowli>len-1)
		{
			nowli = 0;
			prevli = len-1;
			$li.eq(nowli).css({left:760});
			$li.eq(prevli).stop().animate({left:-760});
			$li.eq(nowli).stop().animate({left:0});
			prevli=nowli;
			return;
		}



		if(nowli>prevli){

			$li.eq(nowli).css({left:760});
			$li.eq(prevli).stop().animate({left:-760});			
		}
		else
		{
			$li.eq(nowli).css({left:-760});
			$li.eq(prevli).stop().animate({left:760});
					
		}

		$li.eq(nowli).stop().animate({left:0});
		prevli=nowli;	



	}







})