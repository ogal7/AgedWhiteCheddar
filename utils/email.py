import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 
def sendEmail(clubuser):
	sender = "YOUR ADDRESS"

	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = clubuser
	msg['Subject'] = "SUBJECT OF THE MAIL"
 
	body = "YOUR MESSAGE HERE"
	msg.attach(MIMEText(body, 'plain'))
 
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(sender, "YOUR PASSWORD")
	text = msg.as_string()
	server.sendmail(sender, clubuser, text)
	server.quit()