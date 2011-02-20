var dom = null;
var question_key = null;

var setQuestion = function (){
	if (request.readyState != 4)  { return; }
	question = JSON.parse(request.responseText);
	dom.getElementById("first_number").childNodes[0].childNodes[0].nodeValue=question.first;
	dom.getElementById("second_number").childNodes[0].childNodes[0].nodeValue=question.second;
	question_key = question.key;
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
	dom = evt.target.ownerDocument;
	var answer = dom.getElementById("answer").childNodes[0].childNodes[0].nodeValue;
	var answer_dict = "answer="+answer+"&question_key="+question_key;
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
