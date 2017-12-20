$(function(){
    
    var $li = $('.slide_pics li');  //选中slide_pics下的li
    var len = $li.length;   //记录有多少个li
    var $prev = $('.prev');
    var $next = $('.next');
    
    //将要运动过来的li
    var nowli = 0;
    
    //当前要离开的li
    var preli = 0;
    
    $li.not(':first').css({left:760});  //将不是第一个的li放在右侧760位置
    
    $li.each(function(index){
        var $sli = $('<li>');   //创建一个li
        
        //判断是否是第一个，激活第一个显示
        if(index==0){
            $sli.addClass('active');            
        }
        
        $sli.appendTo('.points');   //将li加到points里
    })
    
    $points = $('.points li');  //显示点
    
    //点击点发生的事件
    $points.click(function(){
        nowli = $(this).index();    //被点击的点为将要出现的
        if(nowli==preli){    //防止点了当前点还出现移动现象
            return;
        }
        move();        
        //被点击的点显示，而其他的显示没激活
        $(this).addClass('active').siblings().removeClass('active');
        
    });
    //点击，进入上一个
    $prev.click(function(){
        nowli--;
        move();
        $points.eq(nowli).addClass('active').siblings().removeClass('active');
    })
    //点击，进入下一个
    $next.click(function(){
        nowli++;
        move();
        $points.eq(nowli).addClass('active').siblings().removeClass('active');
    })
    
    //鼠标进入时，停止自动播放
    $('.slide').mouseenter(function(){
        clearInterval(timer);
    })
    //鼠标离开时，再次开始自动播放
    $('.slide').mouseleave(function(){
        timer = setInterval(autoplay,2000);
    })
    
    timer = setInterval(autoplay,2000);
    //自动播放幻灯片
    function autoplay(){
        nowli++;
        move();
        $points.eq(nowli).addClass('active').siblings().removeClass('active');
    }
    
    function move(){
        
        //形成循环
        if(nowli<0){
            nowli = len-1;
            preli = 0;
            $li.eq(nowli).css({left:-760}); 
            $li.eq(preli).stop().animate({left:760});
            $li.eq(nowli).stop().animate({left:0}); 
            preli = nowli;
            return;
        }
        if(nowli>len-1){
            nowli = 0;
            preli = len-1;
            $li.eq(nowli).css({left:760}); 
            $li.eq(preli).stop().animate({left:-760});
            $li.eq(nowli).stop().animate({left:0}); 
            preli = nowli;
            return;
        }
        
        //将要进来的在右边
        if(nowli>preli){
            $li.eq(nowli).css({left:760});  //将将要移动的放在右侧760位置
            $li.eq(preli).stop().animate({left:-760});     //将将要离开的移动到-760位置
        }
        else{   //将要进来的在左边
            $li.eq(nowli).css({left:-760}); //将其放在左侧760
            $li.eq(preli).stop().animate({left:760});  //将其移动到右侧760
                       
        }
        $li.eq(nowli).stop().animate({left:0});    //移动到显示位置
        preli = nowli;
    }
    
})