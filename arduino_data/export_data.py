import serial
import time
# Establish a connection to the COM port the Arduino is connected to.
ser = serial.Serial('COM4', 9600)

def get_soil_value():
    time.sleep(2)
    # Read the line from serial (and decode it to UTF-8).
    line = ser.readline().decode('utf-8').rstrip()

    # Filter out lines that don't start with 'The soil'.
    if line.startswith("The soil"):
        value = int(line.split('(')[-1].split(')')[0])
    else:
         value = None
    return value 

def get_npk_values():
    pass

def get_temp_values():
    pass

def get_humidity_values():
    pass