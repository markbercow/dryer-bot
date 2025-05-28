import RPi.GPIO as GPIO  # pip install RPi.GPIO
import time
import logging


# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

VIBRATION_PIN = 17
WAIT_TIME = 10  # seconds

def init_vibration_sensor(pin):
    """Setup GPIO pin for input."""
    GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering
    GPIO.setup(pin, GPIO.IN)  # Set pin as input
    logging.info(f"GPIO pin {pin} set up for input.")


def text_dryer_done():
    """Text to receipients that the dryer has finished."""
    # TODO: add twilio logic
    logging.info("The Dryer is done!")


def main():
    """This is the main function loop"""
    init_vibration_sensor(VIBRATION_PIN)
    dryer_running = False

    while True:
        if dryer_running:
            if not GPIO.input(VIBRATION_PIN):
                dryer_running = False
                text_dryer_done()
            time.sleep(WAIT_TIME)
        else:
            if GPIO.input(VIBRATION_PIN):
                dryer_running = True
            time.sleep(WAIT_TIME)


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
