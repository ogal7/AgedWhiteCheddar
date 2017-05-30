var container = document.getElementById("vimage");
var x1 = container.getAttribute("width")/2;
var y1 = container.getAttribute("height")/2;
buttonDiv = document.getElementById("roomButtons");
whichRoom = document.getElementById("whichRoom");


var link = window.location['href']
console.log(link);

var apple = link.split("/")
var date = apple[apple.length-2];
console.log(date)

var actionLink =   "/reserve/" + date + "/"
whichRoom.setAttribute("action", actionLink);
console.log(actionLink);


var drawMap = function() {
	

	//three boxy things
	var escalator = document.createElementNS("http://www.w3.org/2000/svg", "rect");
	escalator.setAttribute("style", "fill:black;stroke:black;stroke-width");
	escalator.setAttribute("x", 100)
	escalator.setAttribute("y", 150)
	escalator.setAttribute("width", 200);
	escalator.setAttribute("height", 75);
	container.appendChild(escalator);

	var escalator3 = document.createElementNS("http://www.w3.org/2000/svg", "rect");
	escalator3.setAttribute("style", "fill:black;stroke:black;stroke-width");
	escalator3.setAttribute("x", 305)
	escalator3.setAttribute("y", 150)
	escalator3.setAttribute("width", 90);
	escalator3.setAttribute("height", 75);
	container.appendChild(escalator3);


	var escalator1 = document.createElementNS("http://www.w3.org/2000/svg", "rect");
	escalator1.setAttribute("style", "fill:black;stroke:black;stroke-width");
	escalator1.setAttribute("x", 430)
	escalator1.setAttribute("y", 110)
	escalator1.setAttribute("width", 140);
	escalator1.setAttribute("height", 135);
	container.appendChild(escalator1);

	var escalator2 = document.createElementNS("http://www.w3.org/2000/svg", "rect");
	escalator2.setAttribute("style", "fill:black;stroke:black;stroke-width");
	escalator2.setAttribute("x", 630)
	escalator2.setAttribute("y", 110)
	escalator2.setAttribute("width", 260);
	escalator2.setAttribute("height", 135);
	container.appendChild(escalator2);



	

	//loop for the others
	var starter = 229;
	var xS = 500;
	var xT = 485;
	for (i = 0; i < 5; i++) {
		var room5 = document.createElementNS("http://www.w3.org/2000/svg", "text");
		room5.setAttribute("x", xS );
		room5.setAttribute("y", 25);
		room5.innerHTML = starter.toString();
		room5.setAttribute("fill", "blue");
		room5.setAttribute("font-size", "16px");
		container.appendChild(room5);
		starter += 2;
		
		var roomBox3 = document.createElementNS("http://www.w3.org/2000/svg", "rect");
		roomBox3.setAttribute("style", "fill:white;fill-opacity:0;stroke:black;stroke-width");
		roomBox3.setAttribute("x", xT)
		roomBox3.setAttribute("y", 5)
		roomBox3.setAttribute("rx", 5)
		roomBox3.setAttribute("ry", 5)
		roomBox3.setAttribute("width", 50);
		roomBox3.setAttribute("height", 40);
		container.appendChild(roomBox3);
		xS += 54;
		xT += 56;
	}


	//451
	var room8 = document.createElementNS("http://www.w3.org/2000/svg", "text");
	room8.setAttribute("x", 645);
	room8.setAttribute("y", 330);
	room8.innerHTML = "251";
	room8.setAttribute("fill", "blue");
	room8.setAttribute("font-size", "16px");
	container.appendChild(room8);

	var roomBox8 = document.createElementNS("http://www.w3.org/2000/svg", "rect");
	roomBox8.setAttribute("style", "fill:white;fill-opacity:0;stroke:black;stroke-width");
	roomBox8.setAttribute("x", 638)
	roomBox8.setAttribute("y", 305)
	roomBox8.setAttribute("rx", 5)
	roomBox8.setAttribute("ry", 5)
	roomBox8.setAttribute("width", 50);
	roomBox8.setAttribute("height", 40);
	container.appendChild(roomBox8);


	//var halfBar = document.createElementNS("http://www.w3.org/2000/svg", "path");
	//halfBar.setAttribute("d", "M 100 350 q 150 -300 300 0");
	//halfBar.setAttribute("fill", "green");
	//container.appendChild(halfBar);
}



drawMap();