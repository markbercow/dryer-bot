import time
import RPi.GPIO as GPIO
import logging
from datetime import datetime
from app.status import dryer_status
from app.notify import text_dryer_done_email
from app.config import config

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

VIBRATION_PIN = config["dryer"]["vibration_pin"]
WAIT_TIME = config["dryer"]["wait_time"]
CONFIRM_TIME = config["dryer"]["confirmation_time"]

GPIO.setmode(GPIO.BCM)
GPIO.setup(VIBRATION_PIN, GPIO.IN)
logging.info(f"GPIO pin {VIBRATION_PIN} set up for input.")

def vibration_detected():
    detection_hits = 0
    end_time = time.time() + 30
    while time.time() < end_time:
        pin_status = GPIO.input(VIBRATION_PIN)
        detection_hits += (1 - pin_status)
        time.sleep(WAIT_TIME)
    logging.info(f"{detection_hits} hits in 30 seconds.")
    return detection_hits > 10

def monitor_dryer():
    dryer_running = False
    vibration_start_time = None
    while True:
        if vibration_detected():
            if vibration_start_time is None:
                vibration_start_time = time.time()
                logging.info("Vibration detected. Starting timer...")
            else:
                elapsed = time.time() - vibration_start_time
                dryer_status["elapsed_time"] = round(elapsed)
                if not dryer_running and elapsed >= CONFIRM_TIME:
                    dryer_running = True
                    dryer_status["running"] = True
                    logging.info("Dryer is confirmed to be running!")
        else:
            if dryer_running:
                dryer_running = False
                dryer_status["running"] = False
                dryer_status["elapsed_time"] = 0
                dryer_status["last_completed"] = datetime.now().isoformat()
                logging.info("Dryer has stopped. Sending notification...")
                text_dryer_done_email()
            vibration_start_time = None
