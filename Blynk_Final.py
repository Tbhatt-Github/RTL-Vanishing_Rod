import RPi.GPIO as GPIO
import BlynkLib
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
motorpins = [27, 22, 23, 24]

for pin in motorpins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

#cloud server
BLYNK_TEMPLATE_ID = 'TMPLJG3MN-9-'
BLYNK_DEVICE_NAME = 'Raspi LED'
BLYNK_AUTH = 'R77dMWPsQ8B7xavEV_HVjaVF01DklJji'

myseq = [  [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]]

myseq_i = [  [0, 0, 0, 1],
                [0, 0, 1, 0],
                [0, 1, 0, 0],
                [1, 0, 0, 0]]

blynk = BlynkLib.Blynk(BLYNK_AUTH)

level = 0
reset = 0

@blynk.on('V0')
def S2_write_handler(value):
    global reset
    if (int(value[0]) == 1):
        reset = int(value[0])

@blynk.on('V2')
def S1_write_handler(value):
    global level
    prevlevel = level
    level = int(value[0])*1050

    if (prevlevel < level):
        for i in range(level - prevlevel):
            for step in range(4):
                for pin in range(4):
                    GPIO.output(motorpins[pin], myseq[step][pin])
                time.sleep(0.003) # This delay is very important as it allows the hardware to react to the changing of voltages

    elif (prevlevel > level):
        for i in range(prevlevel - level):
            for step in range(4):
                for pin in range(4):
                    GPIO.output(motorpins[pin], myseq_i[step][pin])
                time.sleep(0.003)

    if (level == 1050):
        time.sleep(1)
        blynk.virtual_write(0, 0)
    

@blynk.on("connected")
def blynk_connected():
    print('If you see this statement, you are connected to the Blynk cloud...')

@blynk.on("disconnected")
def blynk_disconnected():
    blynk.connect()
    print("Blynk has been reconnected")

if __name__ == "__main__":
    
    while True:
        blynk.run()
        if (reset == 1):
            blynk.virtual_write(2, 1)
            reset = 0
            blynk.sync_virtual(2)