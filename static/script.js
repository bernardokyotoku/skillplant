var dom = null;
var question_key = null;

var setQuestion = function (){
	if (request.readyState != 4)  { return; }
	question = JSON.parse(request.responseText);
	dom.getElementById("first_number").childNodes[0].childNodes[0].nodeValue=question.first;
	dom.getElementById("second_number").childNodes[0].childNodes[0].nodeValue=question.second;
	question_key = question.key
}

var answer_evaluation_result = function(){
	if (request.readyState != 4) {return;}
	alert(request.responseText);

}

function on_load(evt,op){
	O = evt.target
	dom = O.ownerDocument;
	URL = "../addition/get_question";
	request = new XMLHttpRequest();
	request.open("GET", URL); 
	request.onreadystatechange = setQuestion ;
	request.send(null); 
	dom.getElementById("ans_first_digit").childNodes[0].childNodes[0].nodeValue="";
	dom.getElementById("ans_second_digit").childNodes[0].childNodes[0].nodeValue="";
}


function send_answer(evt){
	dom = evt.target.ownerDocument;
	var ans_first_digit = dom.getElementById("ans_first_digit").childNodes[0].childNodes[0].nodeValue;
	var ans_second_digit = dom.getElementById("ans_second_digit").childNodes[0].childNodes[0].nodeValue;
	var answer = ans_first_digit + ans_second_digit;
	var answer_dict = {"answer":answer,'question_key':question_key};
	request = new XMLHttpRequest();
	request.open("POST","../addition/post_answer");
	request.onreadystatechange = answer_evaluation_result;
	request.send(answer_dict);
}


function ans(evt) {
	var dom
	dom = evt.target.ownerDocument;
	var v = evt.target.childNodes[0].nodeValue;
	var ans_first_digit = dom.getElementById("ans_first_digit").childNodes[0].childNodes[0].nodeValue;
	var ans_second_digit = dom.getElementById("ans_second_digit").childNodes[0].childNodes[0].nodeValue;
	if (ans_second_digit == ""){
		dom.getElementById("ans_second_digit").childNodes[0].childNodes[0].nodeValue = ans_first_digit ;
		dom.getElementById("ans_first_digit").childNodes[0].childNodes[0].nodeValue  = v;
	}
	else {
		dom.getElementById("ans_first_digit").childNodes[0].childNodes[0].nodeValue  = v;
	}
}
