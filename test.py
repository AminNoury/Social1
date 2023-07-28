import aspose.email as ae
from aspose.email import SecurityOptions, SmtpClient

# create a new message
eml = ae.MailMessage()

# set subject, body, to and from addresses
eml.subject = "Message with Html Body"
eml.is_body_html = True
eml.html_body = "<html><body>This is the <b>HTML</b>body</body></html>"
eml.from_address = "from@gmail.com"
eml.to.append(ae.MailAddress("to@gmail.com", "Recipient 1"))

# send email using Smtp Client
client = SmtpClient("smtp.gmail.com", 995, "username", "password")
client.security_options = SecurityOptions.AUTO
client.send(eml)
