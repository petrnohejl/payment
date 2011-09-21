#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Payment version 1.1

Copyright (C)2009 Petr Nohejl, jestrab.net

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

This program comes with ABSOLUTELY NO WARRANTY!
"""

### IMPORT #####################################################################

import sys		# argv
import math		# floor



### ERRORS A HELP ##############################################################

def ErrorArg():
	print "Error: Incorrect arguments!\nTo show help, run program with parameter -h."
	return
	
def ErrorDict():
	print "Error: Cannot load text file!"
	return
	
def ErrorFile():
	print "Error: Incorrect data in text file!\nUse only integer, floating point numbers or ':' separators!"
	return
	
def Help():
	print "Payment version 1.1"
	print ""
	print "Copyright (c)2009 Petr Nohejl, project.jestrab.net"
	print ""
	print "Program count your payment and show statistics."
	print "You must set your payment per hour and name of text file,"
	print "where are numbers below, on lines. Numbers means hours, which you worked."
	print "Numbers must be in decimal or sexadecimal number system."
	print "You can use only integers, floating point numbers with '.' separator or ':' separators"
	print "to split hours and minutes, if you use sexadecimal number system."
	print ""
	print "Usage: payment -dec money_per_hour text_file"
	print "       payment -sexadec money_per_hour text_file"
	print "       payment -h"
	print ""
	print "Example: python payment.py -dec 120 work.txt"
	return
		
	
	
### DEC2SEXADEC ################################################################
	
def  DecToSexadec(num):
	base = int(math.floor(num))
	decimal = int((num - base) * 60)
	return "" + str(base) + ":" + str(decimal)

	
	
### PAY ########################################################################
	
def  Payment():
	if(len(sys.argv) == 4):
		filename = sys.argv[3]
		total = 0.0
		count = 0
		maximum = 0.0
		minimum = 10000.0
		
		# parametr notace
		if(sys.argv[1] == "-dec"):
			notation = 10
		elif(sys.argv[1] == "-sexadec"):
			notation = 60
		else:
			ErrorArg()
			return
			
		# parametr money
		try:
			money = int(sys.argv[2])
		except:
			ErrorArg()
			return
		
		# otevreni souboru
		try:
			file = open(filename, "r")
		except:
			ErrorDict()
			return
		
		# cteni souboru
		while True:
			line = file.readline()
			
			# konec souboru
			if (line == "" or line == "\n"):
				break
			else:
				try:
					if(notation==60):
						# prevod notace 12:30 na 12.5
						nums = line.split(":")
						num = float(nums[0]) + (float(nums[1]) / 60)
					elif(notation==10):
						# prevod notace na 12.5
						num = float(line)
					total += num
					if(num < minimum): minimum = num
					if(num > maximum): maximum = num
				except:
					ErrorFile()
					return
				count += 1
		
		file.close
		
		print ""
		print "Number of tasks:", count
		
		if(notation==60): print "Shortest task:", DecToSexadec(minimum)
		elif(notation==10): print "Shortest task:", round(minimum, 2)
		
		if(notation==60): print "Longest task:", DecToSexadec(maximum)
		elif(notation==10): print "Longest task:", round(maximum, 2)
		
		if(notation==60): print "Average time for task:", DecToSexadec(round(total / count, 2))
		elif(notation==10): print "Average time for task:", round(total / count, 2)
		
		print "Payment per hour:", money
		
		if(notation==60): print "Total hours:", DecToSexadec(round(total, 2))
		elif(notation==10): print "Total hours:", round(total, 2)
		
		print "Total payment:", round(total * money, 2)
		
		
	elif(len(sys.argv) == 2 and (sys.argv[1] == "-h" or sys.argv[1] == "--help")):
		Help()
		
	else:
		ErrorArg()



### MAIN #######################################################################

if (__name__=="__main__"):
	Payment()
