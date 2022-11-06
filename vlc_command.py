#!/usr/bin/python
import sys
import telnetlib

cmd = " ".join(sys.argv[1:])
tn = telnetlib.Telnet("localhost", 4212)
tn.read_until("Password: ")
tn.write("admin\n")
tn.read_until("> ")
tn.write(cmd + "\n")
tn.close()
