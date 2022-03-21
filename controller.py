from pyfirmata import Arduino, SERVO , boards,util,STRING_DATA
#import serial

#ser = serial.Serial("COM3",9600)
port='COM3'
#Now using 2 servo motors
#pin=10

board=Arduino(port)

board.digital[9].mode=SERVO
board.digital[6].mode=SERVO


def rotateServo(pin,angle):
    board.digital[9].write(angle)
    board.digital[6].write(angle)
    
def doorAutomate(val):
      if val == 1:
          rotateServo(9,90)
          rotateServo(6,90)
          
      elif val == 0:
          rotateServo(9,90)
          rotateServo(6,180)
          
          
