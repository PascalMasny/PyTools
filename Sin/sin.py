#!/usr/bin/python3

#Imports
from oct2py import Oct2Py
oc = Oct2Py()

#Path to directory
oc.addpath('/home/masnyp/octave/sin')

#Print plot inj ASCII
list = oc.asdf("sincurve.csv", True)

