import yagmail

try:
	from config import EMAIL_PASSWORD
	yag = yagmail.SMTP("tradestockswithfriends@gmail.com", EMAIL_PASSWORD)
except Exception:
	yag = yagmail.SMTP("tradestockswithfriends@gmail.com")

def send_mail(recipient="amascillaro@olin.edu", subject = "Stock API Update", body="test", attachment=[]):
	global yag
	yag.send(
	    to=recipient,
	    subject=subject,
	    contents=body, 
	    attachments=attachment
	)

def sold_stock_mail(symbol="JNUG", qty=1, price=1.00, trade="test.json"):
	send_mail(subject=f"Sold {symbol} at {price}", body=f"Sold {qty} shares of {symbol} at {price}.\n{trade}")

def bought_stock_mail(symbol="JNUG", qty=1, price=1.00, trade="test.json"):
	send_mail(subject=f"Bought {symbol} at {price}", body=f"Bought {qty} shares of {symbol} at {price}.\n{trade}")

def liquidate_stock_mail(trades):
	send_mail(subject=f"Liquidated All Stocks", body=f"See trade below.\n{trades}")

if __name__ == "__main__":

	recipient = "amascillaro@olin.edu"
	body = "Hello there from Yagmail"
	filename = "test.json"
