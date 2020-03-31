import yagmail
yag = yagmail.SMTP("tradestockswithfriends@gmail.com")

def sendMail(recipient="amascillaro@olin.edu", subject = "Stock API Update", body="test", attachment=[])
	global yag
	yag.send(
	    to=recipient,
	    subject=subject,
	    contents=body, 
	    attachments=attachment
	)

if __name__ == "__main__":

	recipient = "amascillaro@olin.edu"
	body = "Hello there from Yagmail"
	filename = "test.json"
