#!/usr/bin/env python

import warnings
import os, sys, getopt, time
import subprocess
import os, shutil
from argv import InputArgs
import sh

# Autorship information
__author__ = "Hüsamettin Deniz Özeren"
__copyright__ = "Copyright 2021"
__credits__ = ["Hüsamettin Deniz Özeren"]
__license__ = "GNU General Public License v3.0"
__maintainer__ = "Hüsamettin Deniz Özeren"
__email__ = "denizozeren614@gmail.com"



if __name__ == "__main__":
    PATH = os. getcwd()
    args = InputArgs(sys.argv[1:])
    n, f, c, i, m = args.pvt_run()
  
    print('# ' + '=' * 39 + " INPUT PARAMETERS "+ '='*39)
    print('')
    print('Cores                 : '+n)
    print('Input .MDP            : '+f)
    print('Input .GRO            : '+c)
    print('Starting Temperature  : '+i+' K')
    print('Ending Temperature    : '+m+' K')
    print('')
    print('# ' + '='*96)
    time.sleep(3)
    print('')
    print("Starting Density Analysis Run...")
    print("")
    time.sleep(1)

    for i in range(int(i), int(m)-25, -25):
        os.chdir(PATH)
        step_dir = os.path.join(PATH, str(i))
        mdp_dir = os.path.join(PATH, str(f))
        gro_dir = os.path.join(PATH, str(f))
        if os.path.exists(step_dir) == True:
            shutil.rmtree(step_dir)
        
        os.mkdir(step_dir)
        shutil.copy(mdp_dir, step_dir)
        os.chdir(step_dir)
        os.rename(str(f), str(i)+".mdp")
        sh.sed('-i', '/^ref_t.*/d', str(i)+".mdp")
        sh.sed('-i', '/^tau_t.*/a ref_t\t\t\= '+str(i), str(i)+".mdp")
