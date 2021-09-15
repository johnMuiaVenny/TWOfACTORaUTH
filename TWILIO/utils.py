import os 
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure


account_sid = 'AC18c00c7f303c45e398b05f15dadcc9ab' 
auth_token = '1718758248a5aec7d602cd6b5f85e443' 
client = Client(account_sid, auth_token)

def send_sms(user_code, Phone_Number): 
    message = client.messages.create( 
        body = f'Your verification code is {user_code}',
        from_ = '+12018028298', 
        to = f'{Phone_Number}'
    )