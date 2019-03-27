#email_handler.py

import smtplib
import account_info

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(account_info.gmail_user, account_info.gmail_password)

except:
    print("Not working!")

class EmailHandler:

    def __init__(self, recipient):
        self.first_name = recipient.first_name
        self.last_name = recipient.last_name
        self.email = recipient.email
    
class RecommendationEmail:

    def __init__(self, recipient):
        super().__init__()
        self.recommender_first_name = recipient.recommender_first_name
        self.recommender_last_name = recipient.recommender_last_name
        self.recommender_email = recipient.recommender_email
