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

    for temp in range(int(i), int(m)-25, -25):
        os.chdir(PATH)
        step_dir = os.path.join(PATH, str(temp))
        mdp_dir = os.path.join(PATH, str(f))
        gro_dir = os.path.join(PATH, str(f))
        if os.path.exists(step_dir) == True:
            shutil.rmtree(step_dir)
        
        os.mkdir(step_dir)
        shutil.copy(mdp_dir, step_dir)
        os.chdir(step_dir)
        os.rename(str(f), str(temp)+".mdp")
        sh.sed('-i', '/^ref_t.*/d', str(temp)+".mdp")
        sh.sed('-i', '/^tau_t.*/a ref_t\t\t\= '+str(temp), str(temp)+".mdp")

        #PVT run of i step
        if temp==int(i): #first step
            print("First step started")
            os.system('gmx_mpi grompp -f '+str(f)+' -o '+str(temp)+'.tpr'+' -c '+c+' -r '+c+' -p topol.top -n index.ndx')
            os.system('mpirun -np '+str(n)+' gmx_mpi mdrun -v -deffnm '+str(temp))
            new_gro=os.path.join(step_dir, str(temp)+".gro")
        else:
            p=int(temp)-25
            new_gro=os.path.join(step_dir, str(p)+".gro")
            os.system('gmx_mpi grompp -f '+str(temp)+".gro"+' -o '+str(temp)+'.tpr'+' -c '+str(p)+'.gro'+' -t '+str(p)+'.cpt'+' -p topol.top -n index.ndx')
            os.system('mpirun -np '+str(n)+' gmx_mpi mdrun -v -deffnm '+str(temp))
