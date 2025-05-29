from twilio.rest import Client
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Twilio credentials
TWILIO_ACCOUNT_SID = "REMOVED"
TWILIO_AUTH_TOKEN = "REMOVED"
MESSAGING_SERVICE_SID = "REMOVED"
RECIPIENT_PHONE_NUMBER = "+REMOVED"  # e.g., your phone number

# Initialize Twilio client
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def text_dryer_done():
    """Send an SMS using the Twilio Messaging Service."""
    message_body = "The dryer has finished running."
    try:
        message = twilio_client.messages.create(
            body=message_body,
            to=RECIPIENT_PHONE_NUMBER,
            messaging_service_sid=MESSAGING_SERVICE_SID
        )
        logging.info(f"Notification sent. Message SID: {message.sid}")
    except Exception as e:
        logging.error(f"Failed to send SMS: {e}")

# Example usage
if __name__ == "__main__":
    text_dryer_done()
