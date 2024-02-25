import serial
import time

# Establish a connection to the COM port the Arduino is connected to.
ser = serial.Serial('COM4', 9600)
time.sleep(2)  # Wait for the connection to establish

def read_line():
    # Reads a single line from the serial port and parses the sensor values.
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').strip()
        # Split the line into a list of values based on space
        values = line.split(' ')
        if len(values) == 6:  # Ensure there are exactly 6 values
            # Convert each value to the appropriate type and assign it
            nitrogen = int(values[0])
            phosphorus = int(values[1])
            potassium = int(values[2])
            soil_mois = int(values[3])
            temp = float(values[4])
            humid = float(values[5])
            return nitrogen, phosphorus, potassium, soil_mois, temp, humid
    return None

def testing():
    while True:
        sensor_values = read_line()
        if sensor_values:
            nitrogen, phosphorus, potassium, soil_mois, temp, humid = sensor_values
            print("N: {}, P: {}, K: {}, Soil Moisture: {}, Temp: {}, Humidity: {}".format(nitrogen, phosphorus, potassium, soil_mois, temp, humid))
        time.sleep(2)  # Delay for 2 seconds before reading again
