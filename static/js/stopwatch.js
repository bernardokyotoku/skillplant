var ms = 0;
var state = 0;
var stop_watch_display = 0;

function set_stop_watch_display(evt){
	stop_watch_display = getLeafNode(evt.target);
}

function getLeafNode(node){
	if (node.hasChildNodes()) {
		return getLeafNode(node.firstChild);
		}
	return node;
	}

function startstop() {
	update_display();
	if (state == 0) {
		state = 1;
		then = new Date();
		then.setTime(then.getTime() - ms);
	} else {
		state = 0;
		now = new Date();
		ms = now.getTime() - then.getTime();
		stop_watch_display.text(parseFloat(Math.round(ms/100)/10));
	   }
}

function swreset() {
	state = 0;
	ms = 0;
	stop_watch_display.text(ms);
}

function update_display() {
	setTimeout("update_display();", 50);
	if (state == 1)  {
		now = new Date();
		ms = now.getTime() - then.getTime();
		stop_watch_display.text(parseFloat(Math.round(ms/100)/10));
   }
}
