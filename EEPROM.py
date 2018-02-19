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

iodir = os.path.dirname(os.path.abspath(dumpfile_path))
dumpfile_abspath = os.path.abspath(dumpfile_path)

print("Input/Output directory: "+iodir)

# Do replace with "empty" and then add the new extension, in case the original save file has an unexpected extension.
outputfile_abspath = dumpfile_abspath.replace(".sav", "").replace(".SAV","") + ".converted.sav"

print("Output file will be: " + outputfile_abspath)

with open(dumpfile_abspath, "rb") as infile, open(outputfile_abspath, "wb") as outfile:
	while True:
		inchunk = infile.read(8)

		if not inchunk: # no more data (EOF)
			break

		outfile.write(inchunk[::-1])

# Since we're only reversing the order of data, in- and output should be the same size,
# let's just check in case something dodgy happened:
if os.path.getsize(outputfile_abspath) == dumpfile_size:
	print("In/Out sizes match!")
	print("All done!")
else:
	print("FAIL! In/Out sizes do not match!")
	# File is obviously bad, let's delete it.
	try:
		os.remove(outputfile_abspath)
	except OSError:
		pass
