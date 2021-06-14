#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
import datetime
import sys
import os

# ******************************************************************
# Definitionen
# ******************************************************************
filename  = 'countdown.txt'
title = "Add Countdown"
zeit = ""
command = ""
path = ""

# ******************************************************************
# Klassen
# ******************************************************************
class App(tk.Frame):
	def __init__(self, parent):
		super().__init__(parent)
		now = datetime.datetime.now()
		tm_hour   = now.hour
		tm_minute = now.minute
		
		self.hourstr=tk.StringVar(self,tm_hour)
		self.hour = tk.Spinbox(self,from_=00,to=23,format="%02.0f",wrap=True,textvariable=self.hourstr,width=2,state="readonly")
		self.minstr=tk.StringVar(self,tm_minute)
		self.minstr.trace("w",self.trace_var)
		self.last_value = ""
		self.min = tk.Spinbox(self,from_=00,to=59,format="%02.0f",wrap=True,textvariable=self.minstr,width=2,state="readonly")
		self.hour.grid()
		self.min.grid(row=0,column=1)
	
	def trace_var(self,*args):
		if self.last_value == "59" and self.minstr.get() == "0":
			self.hourstr.set(int(self.hourstr.get())+1 if self.hourstr.get() !="23" else 0)
		self.last_value = self.minstr.get()


class Form(tk.Frame):
	def __init__(self, parent):
		super().__init__(parent)
		self.lbl_title = tk.Label(self, text="Bezeichnung: ")
		self.inp_title = tk.Entry(self, width=40)
		self.lbl_time = tk.Label(self, text="Countdown bis: ")
		self.inp_time = App(self)
		self.lbl_command = tk.Label(self, text="Shell-Command: ")
		self.inp_command = tk.Entry(self, width=40)
		self.btn_set = tk.Button(self, text="Set Countdown", command=self.setCountdown)
		
		self.lbl_title.grid(row=0, column=0, sticky="e")
		self.inp_title.grid(row=0, column=1, sticky="w")
		self.lbl_time.grid(row=1, column=0, sticky="e")
		self.inp_time.grid(row=1, column=1, sticky="w")
		self.lbl_command.grid(row=2, column=0, sticky="e")
		self.inp_command.grid(row=2, column=1, sticky="w")
		self.btn_set.grid(row=3,column=1, sticky="e")
		
		self.inp_title.focus_set()
	
	def setCountdown(self,*args):
		if(self.inp_title.get() == ""):
			print("Geben Sie bitte ein Bezeichnung an")
		else:
			self.write2File()
			self.quit()
	
	def write2File(self,*args):
		full_path = os.path.realpath(__file__)
		path, thisfile = os.path.split(full_path)
		ff = open(path+"/"+filename,"w")
		ff.write(self.inp_title.get()+"\n")
		ff.write(self.inp_time.hourstr.get()+":"+self.inp_time.minstr.get()+"\n")
		if(self.inp_command.get() == ""):
			ff.write("\n")
		else:
			ff.write(self.inp_command.get())
		ff.close()


# ******************************************************************
# Main
# ******************************************************************
window = tk.Tk()
window.title(title)
window.resizable(width=False, height=False)

Form(window).pack(padx=10, pady=10)
window.mainloop()

