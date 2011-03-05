$(document).ready(function(){
	stop_watch_display = $("#stopwatch");
	$('.question').fadeOut('fast');
	var question;
	$.getJSON('../addition/get_question',function(data){set_question(data);});
	//$('progress_bar').load('progress_bar.html');
	$.get('numpad.html',function(data){
		$('numpad').html(data);
		$("div:hidden").fadeIn("slow");
	});
});

function blink(object){
	$(object).animate({ opacity:0 },100).animate({ opacity:1 },100);
}

function num_enter_delete(object){
	var key_pressed = $(object).text();
	var question = $('.question').text();
	if(key_pressed=="D"){$('.question').text(question.slice(0,-1))}
	else if(key_pressed=="E"){enter_pressed()}
	else{$(".question").text(question+key_pressed);}
}

function enter_pressed(){
	startstop();
	var question;
	var answer = {
		'answer':$('.question').text().slice(4),
		'first':$('.question').text().slice(0,1),
		'second':$('.question').text().slice(2,3),
		'time':$("#stopwatch").text()/1000,
	}
	$.post('../addition/post_answer',answer,function(data){question=data;},"json")//get_question(); 
	if(parseInt(answer.first)+parseInt(answer.second) == answer.answer){
		$('.question').fadeOut('slow',function(){$('.question').text('correct');
			$('.question').fadeIn('slow').fadeOut('slow',function(){set_question(question)});
		});
	} else {
		$('.question').fadeOut('slow',function(){$('.question').text('wrong');
			$('.question').fadeIn('slow').fadeOut('slow',function(){set_question(question)});
		});
	}
}

function get_question(question){
	$.getJSON('../addition/get_question',function(data){
		question =  data;
	
	});
}

function set_question(question){
	$('.question').text(question.first+'+'+question.second+'=').fadeIn("slow");
	swreset();
	startstop();
}
