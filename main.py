import RPi.GPIO as GPIO  # pip install RPi.GPIO
import smtplib
from email.mime.text import MIMEText
import time
import json
import random
import logging

# open configuration file and load json
with open('config.json') as f:
    config = json.load(f)

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email account setup
smtp_server = config['email']['smtp_server']
smtp_port = config['email']['smtp_port']
sender_email = config['email']['sender_email']
sender_password = config['email']['sender_password']

# Recipients
recipients = config['recipients']

# Messages
messages = config['messages']

# Constants
VIBRATION_PIN = config["dryer"]["vibration_pin"]
WAIT_TIME = config["dryer"]["wait_time"]
VIBRATION_CONFIRMATION_TIME = config["dryer"]["confirmation_time"]


def init_vibration_sensor(pin):
    """Setup GPIO pin for input."""
    GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering
    GPIO.setup(pin, GPIO.IN)  # Set pin as input
    logging.info(f"GPIO pin {pin} set up for input.")


def text_dryer_done_email():
    """Text via email gateway to receipients that the dryer has finished."""
    selected_message = random.choice(messages[1:])  # Randomly select a message. Leave messages[0] for future welcome message
    msg = MIMEText(selected_message)
    msg["From"] = sender_email
    msg["To"] = ", ".join(recipients)
    msg["Subject"] = ""

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipients, msg.as_string())
        logging.info("SMS messages sent!")
        logging.info("The Dryer is done!")
    except Exception as e:
        logging.error(f"Failed to send SMS: {e}")


def vibration_detected():
    """These sensors are very fickle. You have to check them for a period of time to determine if vibration is occuring
    
       This function samples the GPIO for 30 seconds. If the number of vibration detections exceeds a threshold, assume vibration is occurring."""
    detection_hits = 0
    end_time = time.time() + 30  # number of seconds to poll GPIO pin
    while time.time() < end_time:
        pin_status = GPIO.input(VIBRATION_PIN)
        detection_hits += (1 - pin_status)  # the pin on this sensor is normally OPEN. So a "1" indicates vibration
        time.sleep(WAIT_TIME)
    logging.info(f"{detection_hits} in 30 seconds")
    
    return detection_hits > 10  # Threshold is set to 10. So if >10 vibration detects are recorded during the timespan, vibration is in progress.


def main():
    """This is the main function loop"""
    init_vibration_sensor(VIBRATION_PIN)
    dryer_running = False
    vibration_start_time = None

    while True:
        if vibration_detected():
            # Vibration detected
            if vibration_start_time is None:  # start timing to determine if the dryer is running.
                vibration_start_time = time.time()
                logging.info("Vibration detected. Starting timer...")
            else:
                elapsed = time.time() - vibration_start_time
                if not dryer_running and elapsed >= VIBRATION_CONFIRMATION_TIME:  # if vibration is detected long enough, the dryer is running.
                    dryer_running = True
                    logging.info("Dryer is confirmed to be running!")
        else:
            # No vibration detected
            if dryer_running:
                dryer_running = False
                text_dryer_done_email()  # send a text (via email) that the dryer cycle has completed.
            vibration_start_time = None  


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.info("Program interrupted by user.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        GPIO.cleanup()  # Clean up GPIO settings
        logging.info("GPIO cleanup done. Exiting program.")
