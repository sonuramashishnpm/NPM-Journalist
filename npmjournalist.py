from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from npmai import Ollama
import smtplib
import imaplib
import base64
import os

class npm_journalist:
  def __init__(self,officer,subject,body):
    self.officer=officer
    self.subject=subject
    self.body=body

  def _send_email(self,to, subject, body):
    off_emails={
      "Kota_DM":"dm-kot-rj@nic.in",
      "Rajasthan_CM":"cmrajasthan@nic.in",
      "Bihar_CM":"cmbihar@nic.in",
      "Delhi_CM":"cmdelhi@nic.in",
      "Patna_DM":"dm-patna-bih@nic.in",
      "Nalanda_DM":"dm-nalanda-bih@nic.in",
      "Kota_SP":"pcr.kotacity@rajpolice.gov.in",
      "Nalanda_SP":"sp-nalanda-bih@nic.in",
      "Patna_SP":"spcity-patna-bih@nic.in",
      "Sonu":"sonukumarviral123@gmail.com",
    }
    SCOPES = ["https://www.googleapis.com/auth/gmail.send",]
    
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    message = MIMEText(body)
    message["to"] = to
    message["subject"] = subject

    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()

    return gmail.users().messages().send(
        userId="me",
        body={"raw": raw}
    ).execute()
    

  def npmai(self):
    officer=self.officer
    subject=self.subject
    body=self.body
    return self._send_email(officer,subject,body)
    #llm=Ollama(
        #model="llama3.2",
        #temperature="0.2"
    #)

    #prompt=f"""
    #Hello you are an AI assistant which review the emails and just respond Yes or No by considering following conditions:-
    #1.Any Offensive word is here or such sign
    #2.Any threat here to the respected officer he is sending the complain like in this email he is sending to {officer}

    #now see these conditions in this email:-
    #Subject:- {subject}
    #Complain:- {body}

    #and please respond just "Yes" if you think the above conditions does not apply in the email and if apply then just write "No" nothing else of it no responmse to instruction or
    #anything, even you think that half it is correct but half not again say "No" when you are sure that this email do not violate the above conditons then only say "Yes"
    #"""

    #response=llm.invoke(prompt)

    #if response=="Yes":
      #return self._send_email(officer,subject,body)
    #else:
      #return """
      #Sorry your email contains some elements which violates rules please identify them and correct them possible reason:-
      #1.Any offensive word or sign
      #2.Any threat or message seems threat
      #"""

