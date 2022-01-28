#!/usr/bin/env python

import numpy 
import matplotlib.pyplot as plt
import piecewise_regression

# Autorship information
__author__ = "Hüsamettin Deniz Özeren"
__copyright__ = "Copyright 2021"
__credits__ = ["Hüsamettin Deniz Özeren"]
__license__ = "GNU General Public License v3.0"
__maintainer__ = "Hüsamettin Deniz Özeren"
__email__ = "denizozeren614@gmail.com"





#x = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11, 12, 13, 14, 15], dtype=float)
#y = numpy.array([5, 7, 9, 11, 13, 15, 28.92, 42.81, 56.7, 70.59, 84.47, 98.36, 112.25, 126.14, 140.03])
class PVT:
    #def __init__(self, x, y):
    #    self.x = x
    #    self.y = y
        

    def fit (self, x, y):
        pw_fit = piecewise_regression.Fit(x, y, n_breakpoints=1)
        pw_fit.plot()
        plt.xlabel("Temperature (K)")
        plt.ylabel("Specific Volume ($cm^3$/g)")
        log = pw_fit.summary()
        print(log)
        plt.show()
        plt.close()
        return log

    def log (self, log):
        file_name = 'model_data.txt'
        log_file = open(file_name,'a+')
        log_file.write(log+"\n")
        log_file.close()
        return
    