import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime
import matplotlib.dates as mdates

# Setup serial connection
ser = serial.Serial('COM3', 9600, timeout=1)

# Lists to store time and NPK values
time_data = []
nitrogen_data = []
phosphorous_data = []
potassium_data = []

def update(frame):
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        now = datetime.now()
        if "Nitrogen" in line:
            val = float(line.split(" ")[1])
            nitrogen_data.append(val)
            time_data.append(now)
        elif "Phosphorous" in line:
            val = float(line.split(" ")[1])
            phosphorous_data.append(val)
        elif "Potassium" in line:
            val = float(line.split(" ")[1])
            potassium_data.append(val)
        
        # Clear the current plot
        plt.cla()
        
        # Plot each nutrient if there's data
        if nitrogen_data:
            plt.plot(time_data, nitrogen_data, label='Nitrogen (mg/kg)')
        if phosphorous_data:
            plt.plot(time_data, phosphorous_data, label='Phosphorous (mg/kg)')
        if potassium_data:
            plt.plot(time_data, potassium_data, label='Potassium (mg/kg)')
        
        # Formatting the plot
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
        plt.gca().xaxis.set_major_locator(mdates.SecondLocator())
        plt.gcf().autofmt_xdate()
        plt.legend()
        plt.tight_layout()

# Create figure for plotting
plt.figure(figsize=(10, 6))

# Start the animation
ani = FuncAnimation(plt.gcf(), update, interval=1000)

# Show plot
plt.show()
