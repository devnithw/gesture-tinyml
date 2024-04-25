import csv
import serial
import signal
import sys

# Function to handle keyboard interrupt
def signal_handler(sig, frame):
    print("Exiting...")
    ser.close()  # Close serial connection
    csv_file.close()  # Close CSV file
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

# Open serial connection
ser = serial.Serial('/dev/cu.usbmodem1101', 9600)  # Adjust baud rate as needed

# Open CSV file for writing
csv_file = open('data.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)

try:
    while True:
    # Read data from Arduino
        line = ser.readline().decode().strip()
        
        # Split the line into separate values based on space delimiter
        values = line.split(",")
        
        # Write each value to a separate cell in the CSV file
        csv_writer.writerow(values)
        
except KeyboardInterrupt:
    print("Keyboard interrupt detected.")
    ser.close()  # Close serial connection
    csv_file.close()  # Close CSV file
    sys.exit(0)