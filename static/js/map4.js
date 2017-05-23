var container = document.getElementById("vimage");
var x = container.getAttribute("width")/2;
var y = container.getAttribute("height")/2;



var drawMap = function () {
	var room = document.createElementNS("http://www.w3.org/2000/svg", "rect");
	room.setAttribute("style", "fill:blue;stroke:black;stroke-width:5;");
	room.setAttribute("x",0);
	room.setAttribute("y",0);
	room.setAttribute("height",50);
	room.setAttribute("width",50);
	container.appendChild(room);
}


drawMap();