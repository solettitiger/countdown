#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime
import sys
import subprocess
import os
from playsound import playsound


# ******************************************************************
# Definitionen
# ******************************************************************
filename  = 'countdown.txt'
audiofile = 'ringing.mp3'
settimer  = 'add.py'
stoptimer = 'stop.py'
overlay   = 'overlay.py'
title = "⏰"
zeit = ""
command = ""
path = ""
diff = 0

# ******************************************************************
# Funktionen
# ******************************************************************
def readdata():
	global title, zeit, command, path
	full_path = os.path.realpath(__file__)
	path, thisfile = os.path.split(full_path)
	ff = open(path+"/countdown/"+filename,"r")
	ll = ff.readlines()
	if(len(ll) == 3):
		title   = ll[0].strip()
		zeit    = ll[1].strip()
		command = ll[2].strip()
	ff.close()

def gettimediff():
	global zeit
	now = datetime.datetime.now()
	day = datetime.datetime(now.year, now.month, now.day)
	endtime = datetime.datetime.strptime(now.strftime("%Y-%m-%d ") + zeit, "%Y-%m-%d %H:%M")
	diff = int((endtime-now).seconds/60)
	if(diff < 0):
		diff = diff + 1440
	
	if(diff < 1 and diff >= -1):
		runDone()
	else:
		zeit = convertTime(diff)

def runDone():
	global zeit
	# Command ausführen
	if(command != ""):
		cmdlist = command.split()
		subprocess.Popen(cmdlist, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
	# Overlay anzeigen
	subprocess.Popen([path+"/countdown/"+overlay, beautifyTimestring(zeit), title], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
	zeit = ""
	# Sound abspielen
	playsound(path+"/countdown/"+audiofile)
	# Countdown beenden - dauert die Zeit von Argos
	stopCountdown()

def stopCountdown():
	ff = open(path+"/countdown/"+filename,"w")
	ff.close()

def convertTime(minutes):
	hours = int(minutes/60)
	minutes = minutes - hours*60
	str_hours = "0" + str(hours)
	str_minutes = "0" + str(minutes)
	return (str_hours[-2:] + ":" + str_minutes[-2:])

def beautifyTimestring(timestring):
	times = timestring.split(":")
	str_hours = "0" + times[0]
	str_minutes = "0" + times[1]
	return (str_hours[-2:] + ":" + str_minutes[-2:])


# ******************************************************************
# Main
# ******************************************************************
def main():
	readdata()
	if(zeit != ""):
		gettimediff()
	print (title + " " + zeit)
	print ("---")
	print ("Set Timer | bash='"+ path+"/countdown/"+settimer +"' terminal=false")
	print ("Stopp Timer | bash='"+ path+"/countdown/"+stoptimer +"' terminal=false")

if __name__ == "__main__":
	main()
