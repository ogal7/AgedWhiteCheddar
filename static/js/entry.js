

var regButton = document.getElementById("register");
//var studentRegButton = document.getElementById("studentRegister");
//var loginButton = document.getElementById("login");

//hhahaha i hate gio
var R = function() {
	var xhttp = new XMLHttpRequest();
  	xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
    	document.getElementById("beyonce").innerHTML = this.responseText;
    }
  	};
  	xhttp.open("GET", "static/ajax_request_files/adminForm.html", true);
  	xhttp.send();
}


adminRegButton.addEventListener("click", aR);
studentRegButton.addEventListener("click", sR);
