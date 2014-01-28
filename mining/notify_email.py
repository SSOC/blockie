import os
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from stratum import settings

import stratum.logger
log = stratum.logger.get_logger('Notify_Email')

class NOTIFY_EMAIL():

    def notify_start(self):
            subject = ('Mine-Litecoin Stratum ALERT: Stratum started!')
            text = ('Stratum service has started!')
            message = MIMEText(text, 'plain')
            self.send_email(settings.NOTIFY_ADMIN,subject,message)
    
    def notify_found_block(self,worker_name):
            subject = ('Mine-Litecoin Stratum ALERT: Found Block by ' % worker_name)
            text = ('%s on Stratum server found a block!' % worker_name)
            message = MIMEText(text, 'plain')
            self.send_email(settings.NOTIFY_ADMIN,subject,message)

    def notify_dead_coindaemon(self,worker_name):
            subject = ('Mine-Litecoin Stratum ALERT: Stratum down!')
            text = ('Stratum is down!')
            message = MIMEText(text, 'plain')
            self.send_email(settings.NOTIFY_ADMIN,subject,message)

    def notify_dead_miner(self,username,email):
                    log.info("Attempting to send email to: %s" % username)
                    subject = ('Mine-Litecoin Stratum ALERT:  ' + username + ' not authenticating properly!')
                    text = ('<p>Your miner is unable to authenticate to the mine-litecoin.com stratum server.<br> <ol><li>You have  <a href="http://www.mine-litecoin.com/index.php?page=register">registered an account</a> at Mine-Litecoin.com</li><li>Please verify that your worker name: ' + str(username) + ' is correctly named.</li><ol> <br>The correct format is <strong>Username.WorkerName</strong>.<br> For Example <strong>Neozonz.1</strong><font color="red"> Neozonz being your username</font> and <font color="green">1 being your worker name</font>.<br><br><br> If you require more assistance please visit the following:</p><ul><li><a href="https://www.mine-litecoin.com/index.php?page=faq">FAQ</a></li><li><a href="https://www.mine-litecoin.com/index.php?page=guide">Our litecoin mining guide</a></li><li><a href="https://www.mine-litecoin.com/index.php?page=video%20tutorials">Our mining video tutorials</a></li><li><a href="https://www.mine-litecoin.com/index.php?page=chat">Our live webchat</a></li></ol></p>')
                    message = MIMEText(text, 'html')
                    self.send_email(email,subject,message)
                    log.info("Sent to %s" % email)

    def send_email(self,to,subject,message):
        log.info("Send attempt to %s" % to)

        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = settings.NOTIFY_EMAIL_FROM
        msg['To'] = to
	msg.attach(message)
        try:
            s = smtplib.SMTP(settings.NOTIFY_EMAIL_SERVER,settings.NOTIFY_EMAIL_SERVER_PORT)
            s.login(settings.NOTIFY_EMAIL_USERNAME,settings.NOTIFY_EMAIL_PASSWORD)
            s.sendmail(msg['From'], msg['To'], msg.as_string())
            s.quit()
        except smtplib.SMTPAuthenticationError as e:
            log.error('Error sending Email: %s' % e[1])
        except Exception as e:
            log.error('Error sending Email: %s' % e[0])
