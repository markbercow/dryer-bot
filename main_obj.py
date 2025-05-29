import RPi.GPIO as GPIO
import time
import logging
from typing import Final


# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

VIBRATION_PIN: Final[int] = 17
WAIT_TIME: Final[float] = 2.0  # seconds


class DryerMonitor:
    def __init__(self, pin: int):
        self.pin = pin
        self.dryer_running = False

    def __enter__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN)
        logging.info(f"GPIO pin {self.pin} set up for input.")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        GPIO.cleanup()
        logging.info("GPIO cleanup done. Exiting program.")

    def send_notification(self):
        """Placeholder for sending a notification (e.g., Twilio)"""
        # TODO: Add Twilio logic here
        logging.info("The Dryer is done!")

    def check_sensor(self):
        """Check vibration sensor and update dryer status."""
        if self.dryer_running:
            if not GPIO.input(self.pin):
                self.dryer_running = False
                self.send_notification()
        else:
            if GPIO.input(self.pin):
                self.dryer_running = True

    def run(self):
        """Main loop to monitor the dryer status."""
        try:
            while True:
                self.check_sensor()
                time.sleep(WAIT_TIME)
        except KeyboardInterrupt:
            logging.info("Program interrupted by user.")
        except Exception as e:
            logging.error(f"An error occurred: {e}")


def main():
    with DryerMonitor(VIBRATION_PIN) as monitor:
        monitor.run()


if __name__ == "__main__":
    main()
