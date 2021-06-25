
import smtplib


def sendmail(subject, body):


    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login("prasadmdone@gmail.com", "Jan292019!")
    message_body = f"Subject:{subject}\n\n{body}"
    smtp.sendmail('prasadmdone@gmail.com', 'dpmudra@gmail.com', message_body)
    smtp.quit()

sendmail('test subject', 'test body')
