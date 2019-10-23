#!/usr/bin/python
'''
A COSYLIGHTS script intended to set up and control socket number 2.
Remember that socket 1 is reserved for COSYHUTCH.
'''
import os
import sys
if sys.platform == 'darwin':
  from energeniesim import switch_on, switch_off
else:
  import RPi.GPIO as GPIO
  from energenie import switch_on, switch_off

def main():
  try:
    print "Cycling socket 2 ON and OFF..."
    while True:
      raw_input('hit return key to send socket 2 ON code')
      switch_on(2)
      raw_input('hit return key to send socket 2 OFF code')
      switch_off(2)
  except KeyboardInterrupt:
    print "Interrupted!"
    if sys.platform != 'darwin':
      GPIO.cleanup()

if __name__=="__main__":
  main()
