# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List
from rasa_sdk.forms import FormAction
from rasa_sdk import Action, Tracker
import smtplib
from email.message import EmailMessage

def SendEmail(toaddr,subject,message):

	fromaddr = 'prasadmdone@gmail.com'
	msg = EmailMessage()
	msg.set_content(message)

	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = subject

	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.ehlo()
	s.starttls()
			
	try:
		s.login(fromaddr, 'Jan292019!')
		s.send_message(msg)
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

	
