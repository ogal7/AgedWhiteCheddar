import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def sendEmail(clubuser, code):
	sender = "suclubscheduling@gmail.com"

	msg = MIMEMultipart()
	msg['From'] = sender
	msg['To'] = clubuser
	msg['Subject'] = "Your Club is Approved"

	body = "Congratulations, your club has been approved use the code:" + code + " To register your club"
	msg.attach(MIMEText(body, 'plain'))

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.login(sender, "fwdfkwe;pjgt4ierpgm349-itwmitomko4qejlrh3128042389045j90rj23490gfmwer") # server.login(username, password)
	text = msg.as_string()
	server.sendmail(sender, clubuser, text)
	server.quit()
