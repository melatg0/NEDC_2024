import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

# Establish a connection to the COM port the Arduino is connected to.
ser = serial.Serial('COM4', 9600)

# Prepare the matplotlib plot.
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

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

# This function is called periodically from FuncAnimation.
def animate(i, xs, ys):
    # Extract the numerical value.
    value = get_soil_value()
    # Append the time (x) and soil moisture value (y) to the lists.
    xs.append(time.time())
    ys.append(value)

    # Limit the x and y lists to 20 items.
    xs = xs[-20:]
    ys = ys[-20:]

    # Draw the line graph.
    ax.clear()
    ax.plot(xs, ys)
    
    # Format plot.
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Soil Moisture over Time')
    plt.ylabel('Moisture Value')

ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=500)
plt.show()