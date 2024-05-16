# valorant_triggerbot

For the video tutorial guide, check out: https://youtu.be/g89zgO3F_J4
## arduino keyboard press
This code reads input from a button connected to pin 2 and sends keyboard commands based on the input received through serial communication. When the serial input is "left", it simulates pressing the 'l' key. The physical button functionality is commented out, so it's not currently active. 
The code initializes the keyboard and sets up serial communication for data input.

Here are other special character or keys to use: https://content.instructables.com/FKH/L2EK/J7AQRDSX/FKHL2EKJ7AQRDSX.pdf

## valorant triggerbot
This Python script is a "trigger bot" designed for use in a video game. Here's a summary of what it does and its potential use:
- Setup: It imports necessary libraries such as ctypes, winsound, random, time, cv2 (OpenCV), keyboard, numpy, and serial. It also defines a monitor area for screen capturing.
- Configuration: You can change the serial port and color to be detected (red, purple, or yellow) by modifying the port and color_to_use variables respectively.
- Color Detection: Based on the chosen color (color_to_use), it sets up lower and upper HSV (Hue, Saturation, Value) thresholds for color detection.
- Serial Communication: It initializes communication with an Arduino device connected to the specified serial port.
- Trigger Bot Logic: It defines a function triggerMain() which continuously monitors the screen for the specified color. When the color is detected, it sends a signal to the Arduino via serial communication to simulate a button press. This is intended to automate shooting - when the target (specified color) is detected on the screen.
- User Interaction: The script allows the user to toggle different modes (Pistol mode, AutoRifle mode, Triggerbot off) using the F1, F2, and F3 keys respectively.
- Arduino Click: Depending on the mode (Pistol or AutoRifle), it sends a signal to the Arduino to simulate a button press at random intervals to emulate human-like behavior.
- Screen Capturing: It captures screenshots of the specified monitor area using the MSS library.
- Continuous Execution: The script runs in an infinite loop, continuously monitoring the screen and reacting based on the detected color and user inputs.

In gaming contexts, such a script is controversial as this can provide unfair advantages and violate the terms of service of many online games.

### Amazon:

Arduino Pro Micro: https://amzn.to/3UY8ri1

### Aliexpress:

Arduino Pro Micro: https://s.click.aliexpress.com/e/_DdgYkVN

### Also works with Arduino Leonardo and/or usb host shield:

### Amazon:

Arduino USB Host Shield: https://amzn.to/3JKdJHn

Arduino Leonardo R3: https://amzn.to/4b0IUdS

Soldering Iron: https://amzn.to/4ba7R5W

Solder Wire: https://amzn.to/4ba7R5W

### Aliexpress:

Arduino USB Host Shield: https://s.click.aliexpress.com/e/_Dl8wK3l

Arduino Leonardo R3: https://s.click.aliexpress.com/e/_DkYWL1V
