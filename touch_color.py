
## holla-back:
## Proxy bytes back and forth from VCP and UART
import time
import board
import busio

from adafruit_circuitplayground.express import cpx

uart = busio.UART(board.TX, board.RX, baudrate=115200)
def output(s):
    print(s)
    uart.write(bytearray(s))

cnt=0
output("holla-back.py: ver 1.0")
while True:
    d1 = uart.read(32)  # read up to 32 bytes
    if d1 is not None:
        output(d1)
    time.sleep(0.1)

output("##Error detected\r\n")