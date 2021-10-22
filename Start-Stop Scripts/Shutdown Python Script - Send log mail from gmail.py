import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


# Variables to change
smtp_port = 587
smtp_server = 'smtp.gmail.com'
sender = ''
to = ''
server_user = ''
server_pass = ''

# FME variables.
import fme
status = fme.status
errorMsg = fme.failureMessage
logFile = fme.logFileName
workspacename = logFile.split('\\')[-1][:-4]

msg = MIMEMultipart("alternative")
msg['From'] = sender
msg['To'] = to


if status:
    msg['Subject'] = f'FME workspace: {workspacename} er kørt '
    html = """\
        <html>
          <body>
            <p>Hej,<br>
               FME Workflow : """ + workspacename + """ kørte som det skulle
            </p>
          </body>
        </html>
        """
else:
    msg['Subject'] = f'FME workspace: {workspacename} er kørt med fejl'
    f = open(logFile, 'r')
    lines = f.readlines()
    log_td = ""
    for line in lines:
        if '|ERROR |' in line:
          log_td = log_td + '<tr><td style="color:red;">' + line + '</td></tr>'
        elif '|WARNING |' in line:
          log_td = log_td + '<tr><td style="color:blue;">' + line + '</td></tr>'
        else:
            log_td = log_td + '<tr><td>' + line + '</td></tr>'

    log_table = """
    <table>
        
        """ + log_td + """
        
    </table>
    """
    
    html = f"""\
        <html>
          <body>
            <p>Hej,<br>
               FME Workflow : {workspacename} kørte med fejl<br>
               Fejlmeddelse: {errorMsg}<br>
               Se nedenstående log for mere information: <br><br>
               {log_table}
            </p>
          </body>
        </html>
        """

part = MIMEText(html, 'html')


msg.attach(part)

filename = logFile.split('\\')[-1]
attachment = open(logFile, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(p)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(server_user, server_pass)
server.sendmail(sender, to, msg.as_string())
server.close()

		
