from gpiozero import LED, Button
# Using RGB LED
# Set up pins for each color and buttons
red_led = LED(19)
green_led = LED(12)
blue_led = LED(21)

red_button = Button(20)
green_button = Button(6)
blue_button = Button(26)

# Define function for checking button states
def check_buttons():

    # Check for button state changes
    if red_button.is_pressed:
        print("Red is pressed")
        red_led.on()
    else:
        red_led.off()

    if green_button.is_pressed:
        print("Green is pressed")
        green_led.on()
    else:
        green_led.off()

    if blue_button.is_pressed:
        print("Blue is pressed")
        blue_led.on()
    else:
        blue_led.off()

# Loop to run code constantly
while True:
    check_buttons()
