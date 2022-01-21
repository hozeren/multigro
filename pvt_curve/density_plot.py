#!/usr/bin/env python

import numpy, scipy, matplotlib
#import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.optimize import differential_evolution
import warnings
import os, sys, getopt, time
from ..lib_py import regression

import os
WORK_DIR = os.getcwd()
THIS_FILE_DIR = os.path.dirname(os.path.abspath(__file__))
print('WORK_DIR', WORK_DIR)
print('THIS_FILE_DIR', THIS_FILE_DIR)

# Autorship information
__author__ = "Hüsamettin Deniz Özeren"
__copyright__ = "Copyright 2021"
__credits__ = ["Hüsamettin Deniz Özeren"]
__license__ = "GNU General Public License v3.0"
__maintainer__ = "Hüsamettin Deniz Özeren"
__email__ = "denizozeren614@gmail.com"
__special_thanks__ = "James Phillips, from Stackoverflow"

#Input arguments
def args_input():
  
    argv = sys.argv[1:]
  
    try:
        opts, args = getopt.getopt(argv, "i:m:d:b:")
      
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

i, m, d, b = args_input()

print('# ' + '=' * 39 + " INPUT PARAMETERS "+ '='*39)
print("Starting Density Analysis Run...")
os.chmod("density.sh", 0o777)
density_sh = "./density.sh"+" -i "+i+" -m "+m+" -d "+d+" -b "+b
print("Bash script starting with this command: "+density_sh)
os.system(density_sh)
print("Ending...")
print('# ' + '=' * 78)
time.sleep(3)

xData1 =[]
yData1 = []

with open("test_density.txt") as f:
    for i in range(1):
        f.readline()
    for line in f:
        cols = line.split()

        if len(cols) == 2:
            xData1.append(float(cols[0]))
            yData1.append(float(cols[1]))
    print('xData:', xData1)
    print('xData:', yData1)
xData = numpy.array(xData1) #putting x data in numpy array
yData = numpy.array(yData1) #putting y data in numpy array


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

# by default, differential_evolution completes by calling curve_fit() using parameter bounds
geneticParameters = generate_Initial_Parameters()

# call curve_fit without passing bounds from genetic algorithm
fittedParameters, pcov = curve_fit(func, xData, yData, geneticParameters)
print('Parameters:', fittedParameters)
print() #Emptty space

modelPredictions = func(xData, *fittedParameters) 

absError = modelPredictions - yData

SE = numpy.square(absError) # squared errors
MSE = numpy.mean(SE) # mean squared errors
RMSE = numpy.sqrt(MSE) # Root Mean Squared Error, RMSE
Rsquared = 1.0 - (numpy.var(absError) / numpy.var(yData))

print()
print('RMSE:', RMSE)
print('R-squared:', Rsquared)

print()


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

############################################################
# log the mo9del data
def log_model (xModel, yModel):
    file_name = 'model_data.txt'
    log_file = open(file_name,'a+')
    log_file.write(str(numpy.round(xModel,5))+"\t"+str(numpy.round(yModel,5))+"\n")
    log_file.close()
    return

graphWidth = 800
graphHeight = 600
xModel, yModel = ModelAndScatterPlot(graphWidth, graphHeight)
log_model(xModel, yModel)