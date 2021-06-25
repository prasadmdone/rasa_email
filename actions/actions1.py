# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List
from rasa_sdk.forms import FormAction
from rasa_sdk import Action, Tracker
import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def SendEmail(toaddr,subject,message):

		fromaddr = 'lakshmipathiae021@gmail.com'
		msg = MIMEMultipart()

		msg['From'] = fromaddr
		msg['To'] = toaddr
		msg['Subject'] = subject
		body=message
		msg.attach(MIMEText(body,'plain'))

        # Create a secure SSL context
		
        #context = ssl.create_default_context()

		s = smtplib.SMTP('smtp.gmail.com', 587)
		s.ehlo()
		s.starttls()
        
		try:
			s.login(fromaddr, 'L99870@88420L')
			text = msg.as_string()
			s.sendemail(fromaddr,toaddr,text)
		except:
			print("An error occurred while sending an email")
		finally:
			s.quit()	

class ActionSubmit(Action):
	def name(self) -> Text:
		return "action_submit"
 
	def run(self, dispatcher, tracker: Tracker, domain: "DomainDict",) -> List[Dict[Text, Any]]:

		SendEmail(
				tracker.get_slot("email"),
				tracker.get_slot("subject"),
				tracker.get_slot("message")
			)
		dispatcher.utter_message("Thanks for providing the details. We have send an email at {}".format(tracker.get_slot("email")))
		return []

	
