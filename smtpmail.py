import smtplib
from email.mime.text import MIMEText

title = 'Hello'
msg_content = '<h2>{title} > <font color="green">OK</font></h2>\n'.format(title=title)
message = MIMEText(msg_content, 'html')

message['From'] = 'SPARROWZ <sparrowtestuser@gmail.com>'
message['To'] = 'Hari <lookworld4@gmail.com>'
message['Subject'] = 'Welcome Mail'

msg_full = message.as_string()

server = smtplib.SMTP('smtp.gmail.com:465')
server.starttls()
server.login('sparrowtestuser@gmail.com', 'Test@123')
server.sendmail('sparrowtestuser@gmail.com',
                ['lookworld4@gmail.com'],
                msg_full)
server.quit()
