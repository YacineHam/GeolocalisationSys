import RPi.GPIO as GPIO
import time
import serial  

port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1)

while True :
    try:
        port.write(('AT'+'\r\n').encode())
        rcv = port.read(20)
        if 'OK' not in rcv.decode() :
            print('Powering up the GPRS Module')
            GPIO.setmode(GPIO.BCM)

            GPIO.setwarnings(False)
            GPIO.setup(21,GPIO.OUT)

            GPIO.output(21,GPIO.HIGH)
            time.sleep(2)
            GPIO.output(21,GPIO.LOW)
        else :
            print('GPRS is Connected')
            break
    except Exception as e:
        print(e)

print('GPRS Module is ON')
GPIO.cleanup()