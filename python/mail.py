import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def mailx():
	fromadd="jbond11909@gmail.com"
	toadd="sagarsr04@riseup.net"

	msg=MIMEMultipart()
	msg['From']=fromadd
	msg['To']=toadd
	msg['Subject']="Survelliance report"
	body="Intrusion Detected"
	msg.attach(MIMEText(body,'plain'))
	s=smtplib.SMTP('smtp.gmail.com',587)
	s.starttls()
	s.login(fromadd, "qwerty@123fuck")
	text=msg.as_string()
	s.sendmail(fromadd,toadd,text)
	s.quit()
	return	
	