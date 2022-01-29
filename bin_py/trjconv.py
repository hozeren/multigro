#!/usr/bin/env python

import warnings
import os, sys, getopt, time
import subprocess
import os
from argv import InputArgs

# Autorship information
__author__ = "Hüsamettin Deniz Özeren"
__copyright__ = "Copyright 2021"
__credits__ = ["Hüsamettin Deniz Özeren"]
__license__ = "GNU General Public License v3.0"
__maintainer__ = "Hüsamettin Deniz Özeren"
__email__ = "denizozeren614@gmail.com"


if __name__ == "__main__":
 
    args = InputArgs(sys.argv[1:])
    f,s = args.trjconv()
    
    
    print('# ' + '=' * 39 + " INPUT PARAMETERS "+ '='*39)
    print('TRJ      : '+f)
    print('TPR/GRO  : '+s)
    time.sleep(3)
    print('')
    print("Starting Density Analysis Run...")
    print("")
    time.sleep(1)
    os.system('gmx_mpi trjconv -f '+f+ '-s '+s+' -center -ur compact -pbc mol -o center_'+f)

    print("Ending...")
    print('# ' + '='*78)

