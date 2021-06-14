#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime
import sys
import os

filename  = 'countdown.txt'

full_path = os.path.realpath(__file__)
path, thisfile = os.path.split(full_path)
ff = open(path+"/"+filename,"w")

ff.close()
