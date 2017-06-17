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
