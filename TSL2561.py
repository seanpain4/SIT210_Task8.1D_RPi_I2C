import smbus
import time

# Get I2C bus
bus = smbus.SMBus(1)

# Setup sensor
bus.write_byte_data(0x39, 0x00 | 0x80, 0x03)
bus.write_byte_data(0x39, 0x01 | 0x80, 0x02)

time.sleep(0.5)

# Read full spectrum lux
luxFull = bus.read_i2c_block_data(0x39, 0x0C | 0x80, 2)

# Read IR lux
luxIR = bus.read_i2c_block_data(0x39, 0x0E | 0x80, 2)

# Convert the data
luxFullOutput = luxFull[1] * 256 + luxFull[0]
luxIROutput = luxIR[1] * 256 + luxIR[0]

luxVisibleOutput = luxFullOutput - luxIROutput

if luxVisibleOutput >= 1200:
	print("Too bright")
elif (1200 > luxVisibleOutput >= 900):
	print("Bright")
elif (900 > luxVisibleOutput >= 600):
	print("Medium")
elif (600 > luxVisibleOutput >= 300):
	print("Dark")
elif (luxVisibleOutput < 300):
	print("Too dark")
