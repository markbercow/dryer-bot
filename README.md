# dryer-bot

## Description and Initial Goals

- Build a simple vibration detector that notifies users via text when the drying cycle has completed
- After initializing the GPIO pin and configuring SMTP, the main loop detects (if vibrations are felt for more than two minutes) if the dryer is running. Once the vibrations stop, a text is sent via the carrier's email gateway notifying the user that it's time to remove the clothes
- Include a simple web interface to monitor dryer status
- Create both a funcational and object oriented design for fun and learning (Object oriented implemention not completed - future project)

## Hardware

A Raspberry Pi Zero 2 W is used for this project. Any Raspberry Pi will work, even a RPi 1 or a Pico. After experimenting with SW-420, SW-18010 and a piezoelectric vibration tapping sensor, I found the best luck with the SW-18010. Note that the SW-18010 is normally OPEN, so vibration = 0. If using a SW-420, vibration is = 1. I'm using GPIO pin 17, which is physical pin 11 on all Pi models. Note that you'll want to use a sensor with digital output

## Setup

- Clone the repository
- Create a virtual environment
- pip install -r requirements.txt
- use config.json.example as an example to create your own config.json
  - create an application password from your email service
  - enter the phone numbers of those who should receive a text
    - check with your carrier for the email address format
      - example for ATT - "<phone_number>@txt.att.net"
      - example for Google Fi - "<phone_number>@fi.google.com"
  - set constants:
    - 'VIBRATION_PIN" - GPIO pin number (not physical pin no)
    - 'WAIT_TIME' - time in seconds to wait before checking pin status again. For me it's 0.1 for a SW-420 vibration sensor, and 0.01 for a SW-18010
    - 'CONFIRMATION_TIME' - time window for continuous vibration detection to confirm dryer is in fact running

## Skills and Tech Used

- Python, vibration sensor (digital input) logic, threading and socket IO to provide status updates to a simple web front end, SMTP based-based messaging for notificatoins via the carrier's email-to-text gateways. Credit to ChatGPT for helping with the CSS (I really wanted a pulsating status indicator!) - most everything else was done by me

## Results and Key Learnings

- You just can't depend on a single reading of the sensor to know if a vibration is taking place. I learned that I had to sample the pin for a period of time to determine if an actual vibration (in this case, the dryer) was actually occuring. More over, some vibrations can occur when the dryer is not running, such as when it's being loaded, or perhaps some residiual "noise" if thw washer or fan was running in close proximity. So I also decided to wait for a consistent vibration over a period of 2 minutes to conclude the dryer was in fact running. In the end, this all seems to work well with no false positives (or negatives)
- Texting through the email gateway is required because carriers no longer let you simply text programmatically. Twilio and other similar services require authorization which is very difficult for hobbiest or students. And it can get pricy registering for campaigns and leasing phone numbers, all of which is required.

## Roadmap

- Move to a RPi Pico. This should be straight forward
- Improve the simple web interface to include setting config parameters
- I would like to refactor using an object oriented design. Some day
- Since carriers are eliminating their email-to-text gateways, I'll need to come up with another way of triggering text-based notifications

## Team Members

Mark Bercow
