/*
cal = document.getElementById("cal")
month = document.getElementById("month")//table header element
week1 = document.getElementById("1stWeek");
week2 = document.getElementById("2ndWeek");
week3 = document.getElementById("3rdWeek");
week4 = document.getElementById("4thWeek");
week5 = document.getElementById("5thWeek");
var weeks = [ week1, week2, week3, week4, week5];
var todaysCalendar = function () {
	var d = new Date();
	dayNum = d.getDate()//returns day of the month (1-31)
	dayWeek = d.getDay()//returns day of the week (0-6)
	year = d.getFullYear()//gets the year
	month1 = d.getMonth()// returns month from 0-11
	month.innerHTML = getMonthName(month1);
	days = getDaysInMonth(month1, year);
	console.log(days);
	//listOfWeeks = getWholeMonth(month1,year);
	//console.log(listOfWeeks);
}
function getDaysInMonth(month, year) {
     var date = new Date(year, month, 1);
     var days = [];
     //console.log();
     while (date.getMonth() === month) {
        days.push(new Date(date));
        date.setDate(date.getDate() + 1);
     }
     //console.log(days);
     return days;
}
var updateCalendar = function () {
	//what is called when the arrows are pushed
}
var checkDate = function() {
	//what is called when a date is clicked
}
var getWholeMonth = function(month,year) {
	var mon = [
		[0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0]
	]
	//console.log(mon);
	var listOfDays = getDaysInMonth(month, year);
	var j = 0;
	for (list in mon){
		for ( i=0; i < 7; i++) {
			//console.log(list[i]);
			console.log(listOfDays[j]);
			list[i] = listOfDays[j];
			//console.log(list[i]);
			j++ ;
		}
	}
	//console.log(mon);
	return mon;
}
function getMonthName(month) {
    var monthName = "";
    switch(month){
    case 0:
	monthName = "January";
	break;
    case 1:
	monthName = "February";
	break;
    case 2:
	monthName = "March";
	break;
    case 3:
	monthName = "April";
	break;
    case 4:
	monthName = "May";
	break;
    case 5:
	monthName = "June";
	break;
    case 6:
	monthName = "July";
	break;
    case 7:
	monthName = "August";
	break;
    case 8:
	monthName = "September";
	break;
    case 9:
	monthName = "October";
	break;
    case 10:
	monthName = "November";
	break;
    case 11:
	monthName = "December";
	break;
    }
    return monthName;
}
todaysCalendar();*/

function getMonthName(month) {
    var monthName = "";
    switch(month){
    case 0:
	monthName = "January";
	break;
    case 1:
	monthName = "February";
	break;
    case 2:
	monthName = "March";
	break;
    case 3:
	monthName = "April";
	break;
    case 4:
	monthName = "May";
	break;
    case 5:
	monthName = "June";
	break;
    case 6:
	monthName = "July";
	break;
    case 7:
	monthName = "August";
	break;
    case 8:
	monthName = "September";
	break;
    case 9:
	monthName = "October";
	break;
    case 10:
	monthName = "November";
	break;
    case 11:
	monthName = "December";
	break;
    }
    return monthName;
}

function fixDays(monthNum){
    if(monthNum == 1){
	$('.days li').each(function(){
	    if($(this).text() >= 29){
		$(this).hide();
	    } 
	});
    } else if(monthNum == 3 || monthNum == 5 || monthNum == 8 || monthNum == 10){
	$('.days li').each(function(){
	    if($(this).text() == 31){
		$(this).hide();
	    } 
	    if($(this).text() == 29 || $(this).text() == 30){
		$(this).show();
	    } 
	});
    } else {
	$('.days li').each(function(){
	    if($(this).text() >= 29){
		$(this).show();
	    } 
	});
    }
}

function weekdays() {
    var dayTags = "<li>Su</li>\n" +
	    "<li>Mo</li>\n" +
	    "<li>Tu</li>\n" +
	    "<li>We</li>\n" + 
	    "<li>Th</li>\n" +
	    "<li>Fr</li>\n" +
            "<li>Sa</li>\n"
    return dayTags;
}

function numDays(year, month) {
    var numTags = "";
    var firstDay = new Date(year, month, 1);
    // getDay() returns 0 if the day is Sunday, so we make sure that
    // we do not prepend a placeholder if the day is Sunday
    // Otherwise, there would be an extra <li> prepended, messing up
    // the layout of the calendar
    if (firstDay.getDay() != 0) {
	for(i = 0; i < firstDay.getDay(); i++) { 
	    numTags += "<li></li>\n";
	}
    }
    for (i = 1; i <= 31; i++) {
	numTags += "<li>" + i.toString() + "</li>\n "
    }
    return numTags;
}

function displayDays(year, month) {    
    $('.weekdays').append(weekdays());
    $('.days').append(numDays(year, month));
}

function activeDay(date, month, year) {
	console.log(year);
	//var month = date.getMonth();
    $('.days li').each(function(){
	
	//console.log(parseInt($(this).text()));
	//console.log(parseInt(date) + 14);
	if (  parseInt($(this).text()) <= parseInt(date) + 14 && parseInt($(this).text()) >= parseInt(date)) {
		$(this).html('<font color = green> <a href=' + month.toString() + "-" + $(this).text() + "-" + year.toString() + '>' + $(this).text() + '</a> </font>\n')
		//console.log('<a href=' + month.toString() + "-" + $(this).text() + "-" + year.toString() + '>');
		//<a href=4- 27  -2017>
	}
	if ($(this).text() == date){
	    $(this).html('<span class = "active"> <a href=' + month.toString() + "-" + date + "-" + year.toString() + '>' + date + '</a> </span>\n')
	}
    });
}

function events(date) {
	li = document.getElementsByClassName("days")[0].childNodes;
	for (i in li) {
		if (i in document.getElementsByTagName("li")) {
			i.addEventListener("click", launch);
		}
	}
}

var launch = function(e) {
	console.log("hi")
}


$(document).ready(function(){
    var d = new Date();
    var monthNum = d.getMonth();
    var currentYear = d.getFullYear();
    var currentDate = d.getDate();
    var currentMonth = getMonthName(monthNum);
    $('.m').html(currentMonth);
    $('.y').html(currentYear);
    displayDays(currentYear, monthNum);
    fixDays(monthNum);
    activeDay(currentDate, monthNum, currentYear);
    //events(currentDate);

    $(document).on("click", ".prev", function(){
	$('.weekdays').empty();
	$('.days').empty();
	monthNum -= 1;
	if (monthNum == -1) {
	    monthNum = 11;
	    currentYear -= 1;
	}
	displayDays(currentYear, monthNum);
	activeDay(currentDate);
	currentMonth = getMonthName(monthNum);
	fixDays(monthNum);
	$('.m').html(currentMonth);
	$('.y').html(currentYear);
    });

    $(document).on("click", ".next", function() {
	$('.weekdays').empty();
	$('.days').empty();
	monthNum += 1;
	if (monthNum == 12) {
	    monthNum = 0;
	    currentYear += 1;
	}
	displayDays(currentYear, monthNum);
	activeDay(currentDate);
	currentMonth = getMonthName(monthNum);
	fixDays(monthNum);
	$('.m').html(currentMonth);
	$('.y').html(currentYear);
    });
});