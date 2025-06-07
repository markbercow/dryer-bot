import threading
from app import create_app, socketio
from app.vibration import monitor_dryer
import RPi.GPIO as GPIO
import logging

# Set up application logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Suppress Werkzeug's access logs
werkzeug_log = logging.getLogger('werkzeug')
werkzeug_log.setLevel(logging.ERROR)

if __name__ == "__main__":
    try:
        logging.info("Starting dryer monitor and web server.")

        monitor_thread = threading.Thread(target=monitor_dryer)
        monitor_thread.daemon = True
        monitor_thread.start()

        socketio.run(create_app(), host="0.0.0.0", port=5000)
    except KeyboardInterrupt:
        logging.info("Program interrupted by user.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        GPIO.cleanup()
        logging.info("GPIO cleanup done. Exiting program.")
