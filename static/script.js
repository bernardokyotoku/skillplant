var dom = null;
var first_number = null;
var second_number = null;

var setQuestion = function (){
	if (request.readyState != 4)  { return; }
//	alert(request.responseText)
	question = JSON.parse(request.responseText);
	first_number = question.first;
	second_number = question.second;
	dom.getElementById("first_number").childNodes[0].childNodes[0].nodeValue=first_number;
	dom.getElementById("second_number").childNodes[0].childNodes[0].nodeValue=second_number;
	startstop()
}

var answer_evaluation_result = function(){
	if (request.readyState != 4) {return;}
	var result = request.responseText;
	//alert(result);
	if (result == "correct"){
		window.location = './correct.html';
	}else{
		window.location = './incorrect.html';
	}
	return;
}

function backspace(evt){
	dom = evt.target.ownerDocument;
	var ans = dom.getElementById("answer").childNodes[0].childNodes[0].nodeValue;
	dom.getElementById("answer").childNodes[0].childNodes[0].nodeValue = ans.slice(0,-1);
}

function on_load(evt,op){
	O = evt.target;
	dom = O.ownerDocument;
	URL = "../addition/get_question";
	request = new XMLHttpRequest();
	request.open("GET", URL); 
	request.onreadystatechange = setQuestion ;
	request.send(null); 
	dom.getElementById("answer").childNodes[0].childNodes[0].nodeValue="";
}

function send_answer(evt){
	startstop();
	dom = evt.target.ownerDocument;
	var answer = dom.getElementById("answer").childNodes[0].childNodes[0].nodeValue;
	var answer_dict = "answer="+answer+"&first="+first_number+"&second="+second_number+"&time="+stop_watch_display.nodeValue/1000;
	
	request = new XMLHttpRequest();
	request.open("POST","../addition/post_answer");
	request.onreadystatechange = answer_evaluation_result;
	request.send(answer_dict);
}


function ans(evt,n) {
	var dom;
	dom = evt.target.ownerDocument;
	var cur = dom.getElementById("answer").childNodes[0].childNodes[0].nodeValue;
	dom.getElementById("answer").childNodes[0].childNodes[0].nodeValue = cur+n;
}
