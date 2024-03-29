#!/usr/bin/python
#import the required modules
import RPi.GPIO as GPIO
import time

# set the pins numbering mode
GPIO.setmode(GPIO.BOARD)

# Select the GPIO pins used for the encoder K0-K3 data inputs
GPIO.setup(11, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

# Select the signal to select ASK/FSK
GPIO.setup(18, GPIO.OUT)

# Select the signal used to enable/disable the modulator
GPIO.setup(22, GPIO.OUT)

# Disable the modulator by setting CE pin lo
GPIO.output (22, False)

# Set the modulator to ASK for On Off Keying
# by setting MODSEL pin lo
GPIO.output (18, False)

# Initialise K0-K3 inputs of the encoder to 0000
GPIO.output (11, False)
GPIO.output (15, False)
GPIO.output (16, False)
GPIO.output (13, False)

# The On/Off code pairs correspond to the hand controller codes.
# True = '1', False ='0'

print "OUT OF THE BOX: Plug the Pi Transmitter board into the Raspberry Pi"
print "GPIO pin-header ensuring correct polarity and pin alignment."
print ""
print "The sockets will need to be inserted into separate mains wall sockets."
print "with a physical separation of at least 2 metres to ensure they don't"
print "interfere with each other. Do not put into a single extension lead."
print ""
print "For proper set up the sockets should be in their factory state with"
print "the red led flashing at 1 second intervals. If this is not the case for"
print "either socket, press and hold the green button on the front of the unit"
print "for 5 seconds or more until the red light flashes slowly."
print ""
print "A socket in learning mode will be listening for a control code to be"
print "sent from a transmitter. A socket can pair with up to 2 transmitters"
print "and will accept the following code pairs"
print ""
print "0011 and 1011 all sockets ON and OFF"
print "1111 and 0111 socket 1 ON and OFF"
print "1110 and 0110 socket 2 ON and OFF"
print "1101 and 0101 socket 3 ON and OFF"
print "1100 and 0100 socket 4 ON and OFF"
print ""
print "A socket in learning mode should accept the first code it receives"
print "If you wish the sockets to react to different codes, plug in and"
print "program first one socket then the other using this program."
print ""
print "When the code is accepted you will see the red lamp on the socket"
print "flash quickly then extinguish"
print ""
print "The program will now loop around sending codes as follows when you"
print "hit a key:"
print "socket 2 on"
print "socket 2 off"
print "Hit CTL C for a clean exit"
try:
	# We will just loop round switching the units on and off
	while True:
		raw_input('hit return key to send socket 2 ON code')
		# Set K0-K3
		print "sending code 1110 socket 2 on"
		GPIO.output (11, False)
		GPIO.output (15, True)
		GPIO.output (16, True)
		GPIO.output (13, True)
		# let it settle, encoder requires this
		time.sleep(0.1)
		# Enable the modulator
		GPIO.output (22, True)
		# keep enabled for a period
		time.sleep(0.25)
		# Disable the modulator
		GPIO.output (22, False)

		raw_input('hit return key to send socket 2 OFF code')
		# Set K0-K3
		print "sending code 0110 socket 2 off"
		GPIO.output (11, False)
		GPIO.output (15, True)
		GPIO.output (16, True)
		GPIO.output (13, False)
		# let it settle, encoder requires this
		time.sleep(0.1)
		# Enable the modulator
		GPIO.output (22, True)
		# keep enabled for a period
		time.sleep(0.25)
		# Disable the modulator
		GPIO.output (22, False)

# Clean up the GPIOs for next time
except KeyboardInterrupt:
	GPIO.cleanup()
