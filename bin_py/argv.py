#!/usr/bin/env python

import warnings
import os, sys, getopt, time


# Autorship information
__author__ = "Hüsamettin Deniz Özeren"
__copyright__ = "Copyright 2021"
__credits__ = ["Hüsamettin Deniz Özeren"]
__license__ = "GNU General Public License v3.0"
__maintainer__ = "Hüsamettin Deniz Özeren"
__email__ = "denizozeren614@gmail.com"

#Input arguments
class InputArgs:

    def __init__(self, argv):
        self.argv = argv

    def trjconv(self):
    
        try:
            opts, args = getopt.getopt(self.argv, "f:s:")
        
        except:
            print("Error with the arguments!")
    
        for opt, arg in opts:
            if opt in ['-f']:
                f = arg
            elif opt in ['-s']:
                s = arg
        return f, s

    def density(self):
    
        try:
            opts, args = getopt.getopt(self.argv, "i:m:d:b:")
        
        except:
            print("Error with the arguments!")
    
        for opt, arg in opts:
            if opt in ['-i']:
                i = arg
            elif opt in ['-m']:
                m = arg
            if opt in ['-d']:
                d = arg
            elif opt in ['-b']:
                b = arg
        return i, m, d, b 

    