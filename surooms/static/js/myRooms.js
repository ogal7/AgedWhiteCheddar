unreserveButtons = document.getElementsByTagName('button');
tableRows = document.getElementsByTagName("tr");
//console.log(unreserveButtons);


var unreserve = function(e) {
	console.log("tht girl is a real crowd pleaser");
	for (i = 0; i < tableRows.length; i++) {
		//console.log(row.id);
		console.log(tableRows[i].getAttribute("id"))
		if (row.id == this.id) {
			console.log("hi");
		}
	}
}


for (i = 0; i < unreserveButtons.length; i++) {
	//console.log("heloooo???")
	unreserveButtons[i].addEventListener("click", unreserve);
}



