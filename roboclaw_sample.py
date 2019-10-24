'''
# brief : This file is sample code for roboclaw driver.
# @author : koji kawabata
# @date : 2019/9/27
'''
import sys,signal
import roboclaw_driver.roboclaw_driver as rc

def handler(signal,frame):
	rc.ForwardMixed(address,0)
	sys.exit(0)

rc.Open('/dev/ttyACM0',115200)
address = 0x80
rc.ForwardMixed(address, 0)
signal.signal(signal.SIGINT,handler)

try:
	# loop until ctl + c
	while True:
	'''
	# write thread
	'''

except Exception as e:
	print(e)
