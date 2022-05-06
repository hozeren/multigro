#!/usr/bin/env python

import warnings
import os, sys, getopt, time
import subprocess
import shutil
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
    args = InputArgs(sys.argv[1:])
    n, f = args.twentyone_step()

    print('# ' + '=' * 39 + " INPUT PARAMETERS " + '=' * 39)
    print('TRJ      : ' + n)
    print('TPR/GRO  : ' + f)
    print('')
    print('# ' + '=' * 96)
    time.sleep(3)
    print('')
    print("Starting Density Analysis Run...")
    print("")
    time.sleep(1)

    for i in range(1, 2):
        print(i)
        os.chdir(PATH)
        step_dir = os.path.join(PATH, str(i))
        input_dir = os.path.join("/home/husamettin/Project/github/multigro/21step/inputs", str(i) + ".mdp")
        if os.path.exists(step_dir) == True:
            shutil.rmtree(step_dir)

        os.mkdir(step_dir)
        shutil.copy(input_dir, step_dir)
        os.chdir(step_dir)

        os.system('gmx_mpi grompp -f ' + str(i) + '.mdp' + ' -o ' + str(i) + '.tpr' + ' -c ' + f+'.gro' + ' -r '+f+'.gro'+' -p topol.top -n index.ndx')
        os.system('mpirun -np ' + str(n) + ' gmx_mpi mdrun -v -deffnm ' + str(i))

        print("Ending...")
        print('# ' + '=' * 78)