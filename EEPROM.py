#!/bin/python
#
# EEPROM .sav dump to emulator/flashcard .sav converter.
# Copyright (C) 2018 Sindastra <https://github.com/sindastra/gbasavcnv>.
# All rights reserved.
#
# The above copyright notice and this notice shall be included in all
# copies or substantial portions of the Software. Do not remove this.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# included LICENSE file.

print("Copyright (C) 2018 Sindastra <https://github.com/sindastra/gbasavcnv>.")
print("All rights reserved.")
print("")
print("This program is distributed in the hope that it will be useful,")
print("but WITHOUT ANY WARRANTY; without even the implied warranty of")
print("MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the")
print("included LICENSE file.")
print("")

def printhelp():
	print("Usage: "+sys.argv[0]+" <dumped_file.sav>")

import sys

if len(sys.argv) < 2:
	printhelp()
	sys.exit(0)

dumpfile_path = sys.argv[len(sys.argv)-1]

import os.path

if not os.path.isfile(dumpfile_path):
	print("File '"+dumpfile_path+"' not found.")
	sys.exit(0)

dumpfile_size = os.path.getsize(dumpfile_path)

print("File '"+dumpfile_path+"' has size: "+str(dumpfile_size)+" bytes")

if dumpfile_size % 8 == 0:
	print("File can nicely be divided into blocks of 8 bytes! Continuing...")
else:
	print("File does not divide into blocks of 8 bytes... exiting!")
	sys.exit(0)
