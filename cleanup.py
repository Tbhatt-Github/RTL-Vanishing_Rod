import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
motorpins = [27, 22, 23, 24]

for pin in motorpins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

GPIO.cleanup()