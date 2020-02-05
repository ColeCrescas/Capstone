#!/home/pi/Desktop/Capstone
#Projectile motion calculator using LIDAR Reading
import random
import math
import sys
import time
import RPi.GPIO as GPIO

#call motor function
Motors_And_Actuator()
#pip install RPistepper
#import RPistepper as stp

#from lidar_lite import Lidar_Lite
#lidar = Lidar_Lite()

#connected = lidar.connect(1)

#if connected < -1:
    #print “Not Connected”
#else:
    #print “Connected”

number_list = []
# Example to find the average of the list
for i in range(0,25):
    #distance = lidar.getDistance()
    distance = random.randint(9,16)
    number_list.append(distance)

print(number_list)
#Function to calculate the average
def Average(number_list):
    return sum(number_list) / len(number_list)

avg = Average(number_list)

print("The average is ", round(avg,2))

#Heights subtracted .75 to account for initial height
#Center is (0,9")
Horz_dis_from_center = 2.25
Low_vert_dis_from_center = 1.25
High_vert_dis_from_center = 3.25
#Angle Calculation
Rightside_angle = ((math.tanh(Horz_dis_from_center/avg))*57.2958)
Leftside_angle = ((math.tanh(-Horz_dis_from_center/avg))*57.2958)
Low_vertical_height = ((math.tanh(Low_vert_dis_from_center/avg))*57.2958)
High_vertical_height = ((math.tanh(High_vert_dis_from_center/avg))*57.2058)

print("The right side angle is", round(Rightside_angle,2))
print("The left side angle is", round(Leftside_angle,2))
print("The low vertical angle is", round(Low_vertical_height,2))
print("The high vertical angle is", round(High_vertical_height,2))

stepper_motor_center_command = 0
stepper_motor_right_command = round((Rightside_angle/1.8),0)
stepper_motor_left_command = round((Leftside_angle/1.8),0)
stepper_motor_low_height_command = round((Low_vertical_height/1.8),0)
stepper_motor_high_height_command = round((High_vertical_height/1.8),0)

#Non rounded pulse readings
#print("The right side pulses are", round(stepper_motor_right_command,2))
#print("The left side pulses are", round(stepper_motor_left_command,2))
#print("The low vertical pulses are", round(stepper_motor_low_height_command,2))
#print("The high vertical pulses are", round(stepper_motor_high_height_command,2))

#Integer Pulses
print("The right side pulses are", stepper_motor_right_command)
print("The left side pulses are", stepper_motor_left_command)
print("The low vertical pulses are", stepper_motor_low_height_command)
print("The high vertical pulses are", stepper_motor_high_height_command)

#setup first stepper motor
#M1_pins = [17, 27, 10, 9]
#with stp.Motor(M1_pins) as M1:
#M1 = stp.Motor(M1_pins)
#M1.zero()
#print("M1:", M1)

#setup second steper motor
#M2_pins = [17, 27, 10, 9]
#with stp.Motor(M2_pins) as M2:
#M2 = stp.Motor(M12pins)
#M2.zero()
#print("M2:", M2)

for i in range(0,15):
    spot = random.randint(1,5)

    if spot == 1:
        #M1.move(stepper_motor_left_command)
        #M1.reset()
        #M1.cleanup()
        #M2.move(stepper_motor_low_height_command)
        #M2.reset()
        #M2.cleanup()
        print("Spot 1:", stepper_motor_left_command, stepper_motor_low_height_command)
    elif spot == 2:
        #M1.move(stepper_motor_left_command)
        #M1.reset()
        #M1.cleanup()
        #M2.move(stepper_motor_high_height_command)
        #M2.reset()
        #M2.cleanup()
        print("Spot 2:", stepper_motor_left_command, stepper_motor_high_height_command)
    elif spot == 3:
        #M1.move(stepper_motor_right_command)
        #M1.reset()
        #M1.cleanup()
        #M2.move(stepper_motor_high_height_command)
        #M2.reset()
        #2.cleanup()
        print("Spot 3:", stepper_motor_right_command, stepper_motor_high_height_command)
    elif spot == 4:
        #M1.move(stepper_motor_right_command)
        #M1.reset()
        #M1.cleanup()
        #M2.move(stepper_motor_low_height_command)
        #M2.reset()
        #M2.cleanup()
        print("Spot 4:", stepper_motor_right_command, stepper_motor_low_height_command)
    elif spot == 5:
        #M1.move(stepper_motor_center_command)
        #M1.reset()
        #M1.cleanup()
        #M2.move(stepper_motor_low_height_command)
        #M2.reset()
        #M2.cleanup()
        print("Spot 5:", stepper_motor_center_command, Low_vert_dis_from_center)

def zero(self):
    '''
    Sets the motor to the next position which
    Coil_A1 and Coil_A2 are on. Sets this position
    as the reference (steps = 0).
    '''
def move(self, steps):
    '''
    Moves the motor 'steps' steps. Negative steps moves the motor backwards
    '''
def cleanup(self):
    '''
    Cleans the GPIO resources
    '''
def reset(self):
    '''
    Returns the motor to it's initial position
    '''
def Motors_And_Actuators():

    # Declare the GPIO settings
    GPIO.setmode(GPIO.BOARD)

    #Remove warnings
    GPIO.setwarnings(False)

    #Motor A = Top motor
    #Motor B = Bottom motor
    # set up GPIO pins
    GPIO.setup(33, GPIO.OUT) # Connected to PWMA
    GPIO.setup(31, GPIO.OUT) # Connected to AIN1
    GPIO.setup(29, GPIO.OUT) # Connected to AIN2
    #GPIO.setup(13, GPIO.OUT) # Connected to STBY
    GPIO.setup(16, GPIO.OUT) # Connected to BIN1
    GPIO.setup(18, GPIO.OUT) # Connected to BIN2
    GPIO.setup(32, GPIO.OUT) # Connected to PWMB

    print("Motors and actuators are setup")

    # Set the motor speed
    # Motor A:
    GPIO.output(33, GPIO.HIGH) # Set PWMA
    # Motor B:
    GPIO.output(32, GPIO.HIGH) # Set PWMB

    # Drive motor A clockwise
    GPIO.output(31, GPIO.HIGH) # Set AIN1
    GPIO.output(29, GPIO.LOW) # Set AIN2

    #Trigger Actuator
    GPIO.output(16, GPIO.LOW) # Set AIN1
    GPIO.output(18, GPIO.HIGH) # Set AIN2

    time.sleep(1.6)

    GPIO.output(16, GPIO.HIGH) # Set AIN1
    GPIO.output(18, GPIO.LOW) # Set AIN2

    time.sleep(1.6)

    #Trigger Actuator
    GPIO.output(16, GPIO.LOW) # Set AIN1
    GPIO.output(18, GPIO.HIGH) # Set AIN2

    time.sleep(1.6)

    GPIO.output(16, GPIO.HIGH) # Set AIN1
    GPIO.output(18, GPIO.LOW) # Set AIN2

    # Disable STBY (standby)
    #GPIO.output(13, GPIO.HIGH)

    # Wait 5 seconds
    time.sleep(8)

    # Reset all the GPIO pins by setting them to LOW
    GPIO.output(31, GPIO.LOW) # Set AIN1
    GPIO.output(29, GPIO.LOW) # Set AIN2
    GPIO.output(33, GPIO.LOW) # Set PWMA
    #GPIO.output(13, GPIO.LOW) # Set STBY
    GPIO.output(16, GPIO.LOW) # Set BIN1
    GPIO.output(18, GPIO.LOW) # Set BIN2
    GPIO.output(32, GPIO.LOW) # Set PWMB
    Print("Pins have been reset")
