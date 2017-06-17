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

// function makeRed(redRooms) {
//     var toRed = redRooms.split(",");

//     for (i = 0; i < toRed.length; i++) {
// 	if (toRed[i] !== "") {
// 	    toRed[i] = parseInt(toRed[i]);
// 	} else {
// 	    toRed.splice(i, 1);
// 	}
//     }

//     rooms = document.getElementsByTagName("rect");
//     for (i = 0; i < rooms.length; i++) {
// 	if (toRed.indexOf(parseInt(rooms[i].getAttribute("id"))) > -1) {
// 	    var replaceIndex = rooms[i].getAttribute("style").indexOf(";");
// 	    console.log(replaceIndex);
// 	    rooms[i].setAttribute("style", "fill:pink" + rooms[i].getAttribute("style").substring(replaceIndex));
// 	}
//     }
// }

// function loadDoc() {
//     var xhttp = new XMLHttpRequest();
//     xhttp.onreadystatechange = function() {
// 	if (this.readyState == 4 && this.status == 200) {
//     	    makeRed(this.responseText);
// 	}
//     };
//     xhttp.open("GET", "/redRooms/" + date + "/", true);
//     xhttp.send();
// }
