// the previously commented out calendar javascript
// is in calendar.js.old

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
    dayNum = firstDay.getDay();
    if (dayNum != 0) {
	for(i = 0; i < dayNum; i++) { 
	    numTags += "<li></li>\n";
	}
    }
    for (i = 1; i <= 31; i++) {
	numTags += "<li>" + i.toString() + "</li>\n "
	dayNum++;
	if (dayNum == 7) {
	    numTags += "<br/>";
	    dayNum = 0;
	}
    }
    return numTags;
}

function displayDays(year, month) {    
    $('.weekdays').append(weekdays());
    $('.days').append(numDays(year, month));
}

function manageDates(date, month, year) {
    console.log(year);
    $('.days li').each(function(){
	
	if (parseInt($(this).text()) <= parseInt(date)) {
	    $(this).html('<a style="color: #2ba6cb;" href=' + month.toString() + "-" + $(this).text() + "-" + year.toString() + '>' + $(this).text() + '</a>\n')
	} else if ($(this).text() == date){
	    $(this).html('<span class = "active"> <a href=' + month.toString() + "-" + date + "-" + year.toString() + '>' + date + '</a> </span>\n')
	} else if ($(this).text() > date) {
	    $(this).html('<p style="color: lightgray;" href=' + month.toString() + "-" + $(this).text() + "-" + year.toString() + '>' + $(this).text() + '</p>\n');
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
    console.log("hi");
}

var d = new Date();
var monthNum = parseInt(d.getMonth());
var currentYear = parseInt(d.getFullYear());
var currentDate = parseInt(d.getDate());
var currentMonth = getMonthName(monthNum);

$(document).ready(function(){
    $('.m').html(currentMonth);
    $('.y').html(currentYear);
    displayDays(currentYear, monthNum);
    fixDays(monthNum);
    manageDates(currentDate, monthNum, currentYear);
    //events(currentDate);

    $(".prev").on("click", function(){
	console.log("what");
	$('.weekdays').empty();
	$('.days').empty();
	monthNum -= 1;
	if (monthNum == -1) {
	    monthNum = 11;
	    currentYear -= 1;
	}
	displayDays(currentYear, monthNum);
	manageDates(currentDate, monthNum, currentYear);
	currentMonth = getMonthName(monthNum);
	fixDays(monthNum);
	$('.m').html(currentMonth);
	$('.y').html(currentYear);
    });

    $(".next").on("click", function() {
	$('.weekdays').empty();
	$('.days').empty();
	monthNum += 1;
	if (monthNum == 12) {
	    monthNum = 0;
	    currentYear += 1;
	}
	displayDays(currentYear, monthNum);
	manageDates(currentDate, monthNum, currentYear);
	currentMonth = getMonthName(monthNum);
	fixDays(monthNum);
	$('.m').html(currentMonth);
	$('.y').html(currentYear);
    });
});
