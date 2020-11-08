from pwn import *
from ctypes import *

hostname = "chals.damctf.xyz"
port = int(31932)

conn = remote(hostname, port)

#PIN 3

conn.sendline(b"3")
conn.sendline(b"-845500968")

#PIN 1

conn.sendline(b"1")
conn.sendline(b"99")

#PIN 5
conn.sendline(b"5")
conn.sendline(b"1413036362")

#PIN 2
conn.sendline(b"2")
conn.recvline_startswithS((b'I wonder what'))
#Here we will set up the ability to call c functions
cdll.LoadLibrary("libc.so.6")
libc = CDLL("libc.so.6")

timeSeed = conn.recvline()
#print(timeSeed)
libc.srand(int(timeSeed))
favNumber = libc.rand()
conn.sendline(str(favNumber))

#PIN 4
conn.sendline(b"4")
iVar = (libc.rand())
result = ""

runningTally = 0
charChoice = 100
temp = 0
while runningTally <= 291:
	result = result + chr(charChoice)
	runningTally += charChoice ^ ((iVar % 10) + 0x41)
	temp = charChoice ^ ((iVar % 10) + 0x41)

#Here we back up becuase last char goes over the 291
if runningTally != 291:
	result = result[:-1]
	runningTally -= temp
	while(((charChoice ^ (iVar % 10) + 0x41) + runningTally) != 291):
		charChoice -= 1 
	result = result + chr(charChoice)
	#charChoice = charChoice - (runningTally - 291)
	#result = result + chr(charChoice)

conn.sendline(result)

#DONE!

conn.interactive()