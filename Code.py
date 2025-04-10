from gpiozero import LED, Button
# Using RGB LED
# Set up pins for each color and buttons
red_led = LED(19)
green_led = LED(12)
blue_led = LED(21)

red_button = Button(20)
green_button = Button(6)
blue_button = Button(26)
