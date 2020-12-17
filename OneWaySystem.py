import statistics
from gpiozero import Buzzer 
from time import sleep
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
import csv
from gpiozero import Buzzer 
buzzer = Buzzer(21)

TRIG = 18   #When we say TRIG, we mean 18. Makes the code easier to understand.
ECHO = 24  #When we say ECHO, we mean 24. Makes the code easier to understand.

print ("Distance Measurement In Progress")

GPIO.setup(TRIG,GPIO.OUT)    #sets up TRIG (that's PIN 23) to an outout for the speaker to trigger sending a PING!
GPIO.setup(ECHO,GPIO.IN)     #sets up ECHO (that's PIN 23) to an input microphone to listen for the echo PONG back.

GPIO.output(TRIG, False)     #Makes sure the Trigger speaker isn't sending out anything and is quiet to start.
print ("Waiting For Sensor To Settle")



def distcheck():  #defines a neat function to gather up all the code needed for one single distance measurement.

    GPIO.output(TRIG, True)  #fires a pulse by setting the trigger speaker to high
    time.sleep(0.00001)      #wait's a fraction of a second, it's a very short pulse!!!!
    GPIO.output(TRIG, False) #turns the trigger speaker off again.

    while GPIO.input(ECHO)==0:    #measure some times
        pulse_start = time.time()   #records the time the pulse was sent

    while GPIO.input(ECHO)==1:    #records the time the echo was heard
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start  #finds the differnce between sent and recieved pulses

    distance = pulse_duration * 17150         #multiply by a fudge factor to convert to seconds

    distance = round(distance, 2)             #rounds off the number
    
    #print ("Distance:",distance,"cm")         #prints it
    return distance


    ######## Start of program #########
while True:
    lister = []
    for x in range(20):
        lister.append(round(distcheck(),-1)) 
    print(lister)
    moe = statistics.median(lister)
    

    zap1 = moe
    print("First distance is ",zap1)#printsmoe
    time.sleep(1)
    
    lister2 = []
    for x in range(20):
        lister.append(round(distcheck(),-1))
    print(lister2)
    moe2 = statistics.median(lister)
    

    zap2 = moe2
    
    print("Second distance is ",zap2)
    if zap1 < zap2:
        print("getting further away")
        buzzer.on()
        import RPi.GPIO as GPIO
        
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(4,GPIO.OUT)
        GPIO.output(4,GPIO.HIGH)
        sleep(5)
        buzzer.off()
        GPIO.output(4,GPIO.LOW)
        sleep(2)
                
