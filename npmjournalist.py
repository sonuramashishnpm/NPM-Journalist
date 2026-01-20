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
  def __init__(self,officer,subject,body,filepath=None):
    self.officer=officer
    self.subject=subject
    self.body=body
    self.filepath=filepath

  def _send_email(self,to, subject, body,filepath=None):
    self.filepath=filepath
    USER = "sonuramashishnpm@gmail.com"
    PASS = "hpfj raoj iqel canu"
    off_emails={
        "Kota_DM":"kotadm@gmail.com",
        "Rajasthan_CM":"rajasthancm@gmail.com"
    }
    msg = MIMEMultipart()
    msg["to"] = off_emails[to]
    msg["subject"] = subject

    msg.attach(MIMEText(body))

    if filepath and os.path.exists(filepath):
      filename = os.path.basename(filepath)
      attachment = MIMEBase("application", "octet-stream")
      attachment.set_payload(open(filepath, "rb").read())
      encoders.encode_base64(attachment)
      attachment.add_header("Content-Disposition", f"attachment; filename={filename}")
      msg.attach(attachment)
    else:
      pass

    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(USER, PASS)
        server.send_message(msg)
        return "Email sent"

  def npmai(self):
    officer=self.officer
    subject=self.subject
    body=self.body
    llm=Ollama(
        model="llama3.2",
        temperature="0.2"
    )

    prompt=f"""
    Hello you are an AI assistant which review the emails and just respond Yes or No by considering following conditions:-
    1.Any Offensive word is here or such sign
    2.Any threat here to the respected officer he is sending the complain like in this email he is sending to {officer}

    now see these conditions in this email:-
    Subject:- {subject}
    Complain:- {body}

    and please respond just "Yes" if you think the above conditions does not apply in the email and if apply then just write "No" nothing else of it no responmse to instruction or
    anything, even you think that half it is correct but half not again say "No" when you are sure that this email do not violate the above conditons then only say "Yes"
    """

    response=llm.invoke(prompt)

    if response=="Yes":
      return self._send_email(officer,subject,body,filepath=None)
    else:
      return """
      Sorry your email contains some elements which violates rules please identify them and correct them possible reason:-
      1.Any offensive word or sign
      2.Any threat or message seems threat
      """

