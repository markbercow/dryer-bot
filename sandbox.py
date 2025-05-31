import RPi.GPIO as GPIO  # pip install RPi.GPIO
import time
import logging

VIBRATION_PIN = 17

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def init_vibration_sensor(pin):
    """Setup GPIO pin for input."""
    GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering
    GPIO.setup(pin, GPIO.IN)  # Set pin as input
    logging.info(f"GPIO pin {pin} set up for input.")


def vibration_detected():
    detection_hits = 0
    end_time = time.time() + 5
    while time.time() < end_time:
        pin_status = GPIO.input(VIBRATION_PIN)
        detection_hits = detection_hits + pin_status
        time.sleep(.1)
    logging.info(f"{detection_hits} in 5 seconds")
    if detection_hits > 0:
        return True


init_vibration_sensor(VIBRATION_PIN)
try:
    while True:
        logging.info(vibration_detected())

except KeyboardInterrupt:
    logging.info("Program interrupted by user.")
except Exception as e:
    logging.error(f"An error occurred: {e}")
finally:
    GPIO.cleanup()  # Clean up GPIO settings
    logging.info("GPIO cleanup done. Exiting program.")

