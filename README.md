# dryer bot

## Description and Initial Goals

- Build a simple vibration detector that notifies users via text when the drying cycle has completed

- After initializing the GPIO pin and configuring SMTP, the main loop detects, if vibrations are felt for more than five minutes, the dryer is running. Once the vibrations stop, a text is sent via the carrier's email gateway notifying the user that it's time to remove the clothes

- Create both a funcational and object oriented design for fun and learning

## Setup

- Clone the repository
- Create a virtual environment
- pip install -r requirements.txt
- use config.json.example to create your own config.json
    - create an applicatoin password from your email service
    - enter the phone numbers of those who should receive a text. 
        - check with your carrier
        - example for ATT - "<phone_number>@txt.att.net"
        - example for Google Fi - "<phone_number>@fi.google.com"
    - set constants:
        - 'VIBRATION_PIN" - GPIO pin number (not physical pin no)
        - 'WAIT_TIME' - time in seconds to wait before checking pin status again. Recommend 0.1 for a SW-420 vibration sensor
        - 'CONFIRMATION_TIME' - time window for continuous vibration detection to confirm dryer is in fact running

## Skills and Tech Used

- Python, vibration sensor (digital input) logic, SMTP based-based messaging for notificatoins via the carrier's email-to-text gateways

## Results and Key Learnings

- 

## Roadmap

- Nothing else planned for this project.

## Team Members

Mark Bercow
