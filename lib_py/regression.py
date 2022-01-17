#!/usr/bin/env python

import numpy, scipy, matplotlib
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.optimize import differential_evolution
import warnings
import os, sys, getopt, time

# Autorship information
__author__ = "Hüsamettin Deniz Özeren"
__copyright__ = "Copyright 2021"
__credits__ = ["Hüsamettin Deniz Özeren"]
__license__ = "GNU General Public License v3.0"
__maintainer__ = "Hüsamettin Deniz Özeren"
__email__ = "denizozeren614@gmail.com"
__special_thanks__ = "James Phillips, from Stackoverflow"

#Function for pairwise regression
def func(xArray, breakpoint, slopeA, offsetA, slopeB, offsetB):
    returnArray = []
    for x in xArray:
        if x < breakpoint:
            returnArray.append(slopeA * x + offsetA)
        else:
            returnArray.append(slopeB * x + offsetB)
    return returnArray


# function for genetic algorithm to minimize (sum of squared error)
def sumOfSquaredError(parameterTuple):
    warnings.filterwarnings("ignore") # do not print warnings by genetic algorithm
    val = func(xData, *parameterTuple)
    return numpy.sum((yData - val) ** 2.0)


def generate_Initial_Parameters():
    # min and max used for bounds
    maxX = max(xData)
    minX = min(xData)
    maxY = max(yData)
    minY = min(yData)
    slope = 10.0 * (maxY - minY) / (maxX - minX) # times 10 for safety margin

    parameterBounds = []
    parameterBounds.append([minX, maxX]) # search bounds for breakpoint
    parameterBounds.append([-slope, slope]) # search bounds for slopeA
    parameterBounds.append([minY, maxY]) # search bounds for offsetA
    parameterBounds.append([-slope, slope]) # search bounds for slopeB
    parameterBounds.append([minY, maxY]) # search bounds for offsetB


    result = differential_evolution(sumOfSquaredError, parameterBounds, seed=3)
    return result.x

    ##########################################################
# graphics output section
def ModelAndScatterPlot(graphWidth, graphHeight):
    f = plt.figure(figsize=(graphWidth/100.0, graphHeight/100.0), dpi=100)
    axes = f.add_subplot(111)

    # first the raw data as a scatter plot
    axes.plot(xData, yData,  '.', color='red')

    # create data for the fitted equation plot
    xModel = numpy.linspace(min(xData), max(xData))
    yModel = func(xModel, *fittedParameters)

    # now the model as a line plot
    axes.plot(xModel, yModel, color='black')

    axes.set_xlabel('Temperature (K)') # X axis data label
    axes.set_ylabel('Density (kg/mL)') # Y axis data label
    axes.tick_params(axis ='both', direction = 'in')

    plt.show()
    plt.close('all') # clean up after using pyplot
    return xModel, yModel    