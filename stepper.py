import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
motorpins = [27, 22, 23, 24]

for pin in motorpins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

myseq = [  [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]]

myseq_i = [  [0, 0, 0, 1],
                [0, 0, 1, 0],
                [0, 1, 0, 0],
                [1, 0, 0, 0]]

# 4 steps for 1 revolution and geared down by 1/64, thus 1 revolution of the stepper motor requires 4*64 = 256 steps

for i in range(1024):
    for step in range(4):
        for pin in range(4):
            GPIO.output(motorpins[pin], myseq[step][pin])
        time.sleep(0.003) # This delay is very important as it allows the hardware to react to the changing of voltages

time.sleep(1)

for i in range(1024):
    for step in range(4):
        for pin in range(4):
            GPIO.output(motorpins[pin], myseq_i[step][pin])
        time.sleep(0.003)

GPIO.cleanup()