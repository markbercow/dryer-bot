import threading
from app import create_app
from app.vibration import monitor_dryer
import RPi.GPIO as GPIO
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    try:
        logging.info("Starting dryer monitor and web server.")

        monitor_thread = threading.Thread(target=monitor_dryer)
        monitor_thread.daemon = True
        monitor_thread.start()

        app = create_app()
        app.run(host="0.0.0.0", port=5000)
    except KeyboardInterrupt:
        logging.info("Program interrupted by user.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        GPIO.cleanup()
        logging.info("GPIO cleanup done. Exiting program.")
