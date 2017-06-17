//blocking
whichRoomBlock = document.getElementById("whichRoomBlock");

var linkA = window.location['href']
//console.log(link);

var appleA = linkA.split("/")
var dateA = appleA[appleA.length-2];
//console.log(date)

var actionLinkA =   "/block/" + dateA + "/"
whichRoomBlock.setAttribute("action", actionLinkA);
//console.log(actionLink);
