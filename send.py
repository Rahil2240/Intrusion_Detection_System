from twilio.rest import Client
import os

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

# Check if the environment variables are set
if not account_sid or not auth_token:
    print("Error: Missing Twilio credentials. Please set the TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN environment variables.")
    exit()

# Initialize the Twilio client
client = Client(account_sid, auth_token)

def sendSms():
    try:
        message = client.messages.create(
            from_='+12568263040',  # Your Twilio number
            body='Alert: Human detected!',  # The message to send
            to='+18777804236'  # The recipient's phone number
        )
        
        print("Message sent successfully. SID:", message.sid) 

    except Exception as e:
        print(f"Error occurred while sending SMS: {e}")
