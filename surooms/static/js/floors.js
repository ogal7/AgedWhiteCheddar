var link = window.location['href']
console.log(link);

var apple = link.split("/")
var date = apple[apple.length-1];

//http://127.0.0.1:5000/homepage/4-27-2017/


olivia = document.getElementById("shawty");
olivia.setAttribute("action", date);