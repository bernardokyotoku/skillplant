var dom = null;
function on_load(evt){
	O = evt.target
	dom = O.ownerDocument;
	$.get("multiplication/question",setQuestion(question));
	dom.getElementById("ans_first_digit").childNodes[0].childNodes[0].nodeValue="";
	dom.getElementById("ans_second_digit").childNodes[0].childNodes[0].nodeValue="";
}

function send_answer(evt){
	dom = evt.target.ownerDocument;
	var ans_first_digit = dom.getElementById("ans_first_digit").childNodes[0].childNodes[0].nodeValue;
	var ans_second_digit = dom.getElementById("ans_second_digit").childNodes[0].childNodes[0].nodeValue;
	answer = {first_number:ans_first_number,second_number:ans_second_number}
	$.post('answer',answer,showAnswer(rsp))
}

function showAnswer(rsp){
	rsp.
}

function setQuestion(question){
	dom.getElementById("first_number").childNodes[0].childNodes[0].nodeValue=question.first_number;
	dom.getElementById("second_number").childNodes[0].childNodes[0].nodeValue=question.second_number;
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
