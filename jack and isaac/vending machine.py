import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(3, GPIO.IN)
GPIO.setup(5, GPIO.OUT)



while True:

  val = GPIO.input(3)
  print (val)
  if val == 1:
     GPIO.output(5, GPIO.LOW)
  else: 
   GPIO.output(5, GPIO.HIGH)
