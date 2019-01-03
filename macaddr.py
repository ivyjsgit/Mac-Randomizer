import random
import subprocess
import os

def randomMAC():
    return [evenHex(), random.randint(0x00, 0xff), random.randint(0x00, 0x7f),
            random.randint(0x00, 0x7f),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff)]


def MACprettyprint(mac):
    return ':'.join(map(lambda x: "%02x" % x, mac))


def evenHex():
	first = random.randint(0x0, 0xf)
	# first = 0
	second = random.randint(0,9)
	while ((second % 2) != 0):
		second = random.randint(0,9)
	return int(str(first)+str(second))

if __name__ == '__main__':
	ourMacAddr = MACprettyprint(randomMAC())
	ourCommand = "ifconfig en0 ether " + ourMacAddr
	os.system(ourCommand)
	os.system("ifconfig en0 ether down")
	os.system("ifconfig en0 ether up")
	print(ourCommand)
	

