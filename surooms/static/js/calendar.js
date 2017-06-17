// =======================================
// DATE VARIABLE
// =======================================
var d = new Date();
d.setHours(0, 0, 0, 0);

// =======================================
// FUNCTIONS
// =======================================
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
    var daysInMonth = new Date(year, month + 1, 0).getDate();
    // getDay() returns 0 if the day is Sunday, so we make sure that
    // we do not prepend a placeholder if the day is Sunday
    // Otherwise, there would be an extra <li> prepended, messing up
    // the layout of the calendar
    dayNum = firstDay.getDay();
    // redList = weekends(dayNum, daysInMonth);
    if (dayNum != 0) {
	for(i = 0; i < dayNum; i++) {
	    numTags += "<li></li>\n";
	}
    }
    for (i = 1; i <= daysInMonth; i++) {
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

function withinTwoWeeks(d2) {
    var diff = d2.getTime() - d.getTime();
    var diffDays = diff / (1000 * 60 * 60 * 24);

    return diffDays >= 0 && diffDays <= 13;
}

function manageDates(month, year) {
    var curDate = d.getDate();
    var curMonth = d.getMonth();

    // DISPLAY ALL DATES FOR RESERVING ROOMS
    $('.days li').each(function(){
	var monthPadding = "";
	var datePadding = "";

	// HIGHLIGHT CURRENT DATE
	if ($(this).text() == curDate && month === curMonth) {
	    if (month < 10) {
		monthPadding = "0";
	    }

            if (parseInt($(this).text()) < 10) {
		datePadding = "0";
            }

	    $(this).html('<span class = "active-closed"> <a href="' + monthPadding + month.toString() + "-" + datePadding + ($(this).text()).trim() + "-" + year.toString() + '">' + ($(this).text()) + '</a> </span>\n');
	}

	monthPadding = "";
	datePadding = "";

	// COLOR DATE FOR NEXT TWO WEEKS
	var d2 = new Date(year, month, $(this).text());
	if ( withinTwoWeeks(d2)) {
	    if (month < 10) {
		monthPadding = "0";
	    }

            if (parseInt($(this).text()) < 10) {
		datePadding = "0";
            }

	    console.log($(this).text());

	    if (parseInt(d2.getDay()) == 0 || parseInt(d2.getDay()) == 6) {
		if ($(this).text() == curDate && month === curMonth) {
		    $(this).html('<span class="active">' + $(this).text() + '</span>');
		} else {
		    $(this).html('<p class="closed" href=' + monthPadding + month.toString() + "-" + datePadding +
				 ($(this).text()) + "-" + year.toString() + '>' + $(this).text() + '</p> </font>\n');
		}
	    } else {
		$(this).html('<a class="open" href=' + monthPadding + month.toString() + "-" + datePadding +
			     ($(this).text()) + "-" + year.toString() + '>' + $(this).text() + '</a> </font>\n');
	    }
	}
    });


}
// =======================================
// ON DOCUMENT READY
// =======================================

$(document).ready(function(){
    var monthNum = parseInt(d.getMonth());
    var currentYear = parseInt(d.getFullYear());
    var currentMonth = getMonthName(monthNum);
    $('.m').html(currentMonth);
    $('.y').html(currentYear);
    displayDays(currentYear, monthNum);
    manageDates(monthNum, currentYear);

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
    	manageDates(monthNum, currentYear);
    	currentMonth = getMonthName(monthNum);
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
    	manageDates(monthNum, currentYear);
    	currentMonth = getMonthName(monthNum);
    	$('.m').html(currentMonth);
    	$('.y').html(currentYear);
    });
});
