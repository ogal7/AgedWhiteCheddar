var container = document.getElementById("vimage");
var x1 = container.getAttribute("width")/2;
var y1 = container.getAttribute("height")/2;



var drawMap = function () {
	var x = 0;
	var y = 0;
	for (i = 0; i < 7; i++) {
	var room = document.createElementNS("http://www.w3.org/2000/svg", "rect");
	room.setAttribute("style", "fill:white;stroke:black;stroke-width:2;");
	room.setAttribute("x",x);
	room.setAttribute("y",y);
	x += 60;
	room.setAttribute("id", i);
	room.setAttribute("height",80);
	room.setAttribute("width",60);
	room.addEventListener("click", clickRoom);
	container.appendChild(room);
	}
	y = 2*y1;
	y -= 82;
	x = 0;
	for (i = 0; i < 7; i++) {
	var room = document.createElementNS("http://www.w3.org/2000/svg", "rect");
	room.setAttribute("style", "fill:white;stroke:black;stroke-width:2;");
	room.setAttribute("x",x);
	room.setAttribute("y",y);
	x += 60;
	room.setAttribute("id", i);
	room.setAttribute("height",80);
	room.setAttribute("width",60);
	room.addEventListener("click", clickRoom);
	container.appendChild(room);
	}

	var escalator = document.createElementNS("http://www.w3.org/2000/svg", "rect");
	escalator.setAttribute("style", "fill:black;stroke:black;stroke-width");
	escalator.setAttribute("x", x1 - 100)
	escalator.setAttribute("y", y1 - 30)
	escalator.setAttribute("width", 200);
	escalator.setAttribute("height", 75);
	container.appendChild(escalator);

	var escalator1 = document.createElementNS("http://www.w3.org/2000/svg", "rect");
	escalator1.setAttribute("style", "fill:black;stroke:black;stroke-width");
	escalator1.setAttribute("x", x1 + 200)
	escalator1.setAttribute("y", y1 - 30)
	escalator1.setAttribute("width", 200);
	escalator1.setAttribute("height", 75);
	container.appendChild(escalator1);

	//var label = document.createElementNS("http://www.w3.org/2000/svg", "text")

}


var clickRoom = function() {
	console.log("ugh");
}


drawMap();