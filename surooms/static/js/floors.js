var container = document.getElementById("vimage");
var x1 = container.getAttribute("width")/2;
var y1 = container.getAttribute("height")/2;
buttonDiv = document.getElementById("roomButtons");
whichRoom = document.getElementById("whichRoom");

var link = window.location['href']
console.log(link);

var apple = link.split("/");
var date = apple[apple.length-2];
console.log(date)

var actionLink = "/reserve/" + date + "/"
whichRoom.setAttribute("action", actionLink);
console.log(actionLink);

var redRooms = "";
function loadDoc() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
	if (this.readyState == 4 && this.status == 200) {
  	    console.log(this.responseText)
    	    redRooms += this.responseText;
	}
    };
    xhttp.open("GET", "/redRooms/" + date + "/", true);
    xhttp.send();
}

var makeRed = function() {
    toRed = redRooms.split("*");
    console.log(toRed);
    rooms = document.getElementsByTagName("rect");
    for (i = 0; i < rooms.length; i++) {
	if (rooms[i].getAttribute("id") in toRed) {
	    rooms[i].setAttribute("fill", "red");
	}
    }
}
