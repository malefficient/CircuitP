## Time_and_temp_and_UART.py
## Simple test: writes a status update to the VCP and UART once a sec.
import time
import board
import busio

from adafruit_circuitplayground.express import cpx

uart = busio.UART(board.TX, board.RX, baudrate=115200)
def output(s):
    print(s)
    uart.write(bytearray(s))

cnt=0
while True:
    if (cnt % 15 ==0):
        s1="Time|temp|lumens|\r"
        output(s1)
    s1 = "%08.2f| %08.2d| %03.2f\r\n" % (time.monotonic(),  cpx.temperature, cpx.light)
    output(s1)
    cnt+=1
    time.sleep(1.0)
