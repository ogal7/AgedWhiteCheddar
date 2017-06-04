// the previously commented out calendar javascript
// is in calendar.js.old

// =======================================
// DATE VARIABLE
// =======================================
var d = new Date();

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

// function weekends(startDay, monthLength) {
//     var weekendList = []
//     if (startDay == 0){
// 	var i = 1;
// 	while (i <= monthLength) {
// 	    weekendList.push(i);
// 	    i += 6;
// 	}
// 	i = 8;
// 	while (i <= monthLength) {
// 	    weekendList.push(i)
// 	    i+=6;
// 	}
// 	return weekendList; //list of days that are weekends
//     }
//     else {
// 	var i = 7 - startDay;
// 	while (i <= monthLength) {
// 	    weekendList.push(i);
// 	    i+=7;
// 	}
// 	var i = 8 - startDay;
// 	while (i <= monthLength) {
// 	    weekendList.push(i);
// 	}
// 	return weekendList;
//     }
// }

function daysInMonth(iMonth, iYear){
    d3 = new Date(iYear, iMonth - 1, 32)
    x = d3.getDate()
    return 32 - x;
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
    	if (dayNum == 0 || dayNum == 6) {
	    numTags += "<li class='closed'>" + i.toString() + "</li>\n "
	} else {
	    numTags += "<li>" + i.toString() + "</li>\n "
	}
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
    // var daysInMonth = new Date(d.getFullYear(), d.getMonth() + 1, 0).getDate();

    $('.days li').each(function(){
	if( parseInt($(this).text()) <= parseInt(date) + 14 &&
	    parseInt($(this).text()) >= parseInt(date) && month >= 10 ) {

        if (parseInt($(this).text()) < 10) {
	    $(this).html('<a class="open" href=' + month.toString() + "-0" +
			 $(this).text() + "-" + year.toString() + '>' + $(this).text() + '</a> </font>\n')
        }
        else {
        $(this).html('<a class="open" href=' + month.toString() + "-" +
             $(this).text() + "-" + year.toString() + '>' + $(this).text() + '</a> </font>\n')
        }
	}

    if( parseInt($(this).text()) <= parseInt(date) + 14 &&
        parseInt($(this).text()) >= parseInt(date) && month < 10) {
        
        if (parseInt($(this).text()) < 10) {
        $(this).html('<a class="open" href=' + '0' + month.toString() + "-0" +
             ($(this).text()) + "-" + year.toString() + '>' + $(this).text() + '</a> </font>\n')
        }
        else {
            $(this).html('<a class="open" href=' + '0' + month.toString() + "-" +
             ($(this).text()) + "-" + year.toString() + '>' + $(this).text() + '</a> </font>\n')
        }
    }
	// implement 14 days or more and prevent from selecting weekends
	
	if ($(this).text() == d.getDate() && month === d.getMonth() && month < 10) {
        if (parseInt(d.getDate()) < 10) {
	       $(this).html('<span class = "active"> <a href=' + "0" + month.toString() + "-0" + date + "-" + year.toString() + '>' + date + '</a> </span>\n')
        }
        else {
           $(this).html('<span class = "active"> <a href=' + "0" + month.toString() + "-" + date + "-" + year.toString() + '>' + date + '</a> </span>\n')
        }
	}

    if ($(this).text() == d.getDate() && month === d.getMonth() && month >= 10) {
        if (parseInt(d.getDate()) < 10) {
            $(this).html('<span class = "active"> <a href=' + month.toString() + "-0" + date + "-" + year.toString() + '>' + date + '</a> </span>\n')
        }
        else {
            $(this).html('<span class = "active"> <a href=' + month.toString() + "-" + date + "-" + year.toString() + '>' + date + '</a> </span>\n')
        }
    }

    if (month > d.getMonth() || month < d.getMonth()) {
        console.log(month)
        console.log(d.getMonth())
        if (month == d.getMonth() + 1) {
            //console.log("spill")
            //if this two week span goes into the next month
            //onsole.log(daysInMonth(year, d.getMonth()))
            if (d.getDate() >= daysInMonth(year, d.getMonth()) - 14) {
                
                var daysIntoNewMonth = 14 - (daysInMonth(year, d.getMonth()) - d.getDate());
                console.log($(this).text())
                console.log("days into new month" + daysIntoNewMonth)
                if (parseInt($(this).text()) <= daysIntoNewMonth) {
                    console.log("ugh")
                    $(this).html('<a class="open" href=' + '0' + month.toString() + "-0" +
                    ($(this).text()) + "-" + year.toString() + '>' + $(this).text() + '</a> </font>\n')
                }
                else {
                    $(this).html('<li class="normal">'+ $(this).text() + '</font>\n')
                }
            }
        }
        else {
           $(this).html('<li class="normal">'+ $(this).text() + '</font>\n')
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
    var currentDate = parseInt(d.getDate());
    var currentMonth = getMonthName(monthNum);
    $('.m').html(currentMonth);
    $('.y').html(currentYear);
    displayDays(currentYear, monthNum);
    manageDates(currentDate, monthNum, currentYear);

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
    	$('.m').html(currentMonth);
    	$('.y').html(currentYear);
    });
});
