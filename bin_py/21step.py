#!/usr/bin/env python

import warnings
import os, sys, getopt, time
import subprocess
import os, shutil
from argv import InputArgs

# Autorship information
__author__ = "Hüsamettin Deniz Özeren"
__copyright__ = "Copyright 2021"
__credits__ = ["Hüsamettin Deniz Özeren"]
__license__ = "GNU General Public License v3.0"
__maintainer__ = "Hüsamettin Deniz Özeren"
__email__ = "denizozeren614@gmail.com"


if __name__ == "__main__":
    PATH = os. getcwd()
    for i in range(1,2):
        print(i)
        os.chdir(PATH)
        step_dir = os.path.join(PATH, str(i))
        input_dir = os.path.join("/home/husamettin/Project/github/multigro/21step/inputs", str(i)+".mdp")
        print(input_dir)
        os.mkdir(step_dir)
        shutil.copy(input_dir, step_dir)
        os.chdir(step_dir)

        #os.system('gmx_mpi trjconv -f '+f+ '-s '+s+' -center -ur compact -pbc mol -o center_'+f)