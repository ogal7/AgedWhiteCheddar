import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText





def sendEmail(clubuser):
	sender = "suclubscheduling@gmail.com"

	msg = MIMEMultipart()
	msg['From'] = sender
	msg['To'] = clubuser
	msg['Subject'] = "Your Club is Approved"
 
	body = "YOUR MESSAGE HERE"
	msg.attach(MIMEText(body, 'plain'))
 
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.login(sender, "fwdfkwe;pjgt4ierpgm349-itwmitomko4qejlrh3128042389045j90rj23490gfmwer")
	text = msg.as_string()
	server.sendmail(sender, clubuser, text)
	server.quit()
