

var adminRegButton = document.getElementById("adminRegister");
var studentRegButton = document.getElementById("studentRegister");
//var loginButton = document.getElementById("login");


var aR = function() {
	var xhttp = new XMLHttpRequest();
  	xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
    	document.getElementById("beyonce").innerHTML = this.responseText;
    }
  	};
  	xhttp.open("GET", "static/ajax_request_files/adminForm.txt", true);
  	xhttp.send();
}

var sR = function() {
	var xhttp = new XMLHttpRequest();
 	xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
    	document.getElementById("beyonce").innerHTML = this.responseText;
    }
  	};
  	xhttp.open("GET", "static/ajax_request_files/studentForm.txt", true);
  	xhttp.send();
}


adminRegButton.addEventListener("click", aR);
studentRegButton.addEventListener("click", sR);
