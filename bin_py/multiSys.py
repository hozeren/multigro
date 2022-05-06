#!/usr/bin/env python

# import pandas as pd
import sys
from time import sleep
import subprocess
import re
from .analysis import *

# pip install pandas

# Autorship information
__author__ = "Hüsamettin Deniz Özeren"
__copyright__ = "Copyright 2021"
__credits__ = ["Hüsamettin Deniz Özeren"]
__license__ = "GNU General Public License v3.0"
__maintainer__ = "Hüsamettin Deniz Özeren"
__email__ = "denizozeren614@gmail.com"


class multiSys:
    def __init__(self, mdpfilePath):
        self.mdpfilePath = mdpfilePath

    def mdp_unbias(self):
        with open(self.mdpfilePath, "r+") as mdpFile:
            content = mdpFile.read()
            content = re.sub('continuation\t\t= yes', 'continuation\t\t= no', content) # noqa
            content = re.sub('gen_vel\t\t= no', 'gen_vel\t\t= yes', content)
            content = re.sub('gen_seed.*\n|gen_temp.*\n', '', content, flags=re.M) # noqa
            content = re.sub(r"(gen_vel.*$)", r"\1\ngen_temp\t\t= 310", content, flags=re.MULTILINE) # noqa #add temperature variable here
            content = re.sub(r"(gen_temp.*$)", r"\1\ngen_seed\t\t= -1", content, flags=re.MULTILINE) # noqa
            mdpFile.seek(0)
            mdpFile.write(content)
            mdpFile.truncate()

    def mdp_bias(self):
        with open(self.mdpfilePath, "r+") as mdpFile:
            content = mdpFile.read()
            content = re.sub('continuation\t\t= no', 'continuation\t\t= yes', content) # noqa
            content = re.sub('gen_seed.*\n|gen_temp.*\n', '', content, flags=re.M) # noqa
            content = re.sub('gen_vel\t\t= yes', 'gen_vel\t\t= no', content)
            mdpFile.seek(0)
            mdpFile.write(content)
            mdpFile.truncate()

    def distance(self, istep, dt, rdist):
        distance = subprocess.run(['gmx_mpi',
                                   'distance',
                                   '-f', istep + '.trr',
                                   '-s', istep + '.tpr',
                                   '-oav', 'distance.xvg',
                                   '-dt', str(dt),
                                   '-select', rdist])
        error = distance.returncode
        if error != 0:
            sys.exit()

        SlopeObject = slope_5p()
        y1, slope, slope_intercept = SlopeObject.distance_slope()
        SlopeObject.log_slope(y1, slope, slope_intercept)
        return y1, slope

    def create_folder(self, mdp, init_gro, topol, index, maxwarn):
        pass

    def prepare_init(self, mdp, istep, init_gro, topol, index, maxwarn):
        prepare_init = subprocess.run(['gmx_mpi',
                                       'grompp',
                                       '-f', mdp + '.mdp',
                                       '-o', istep + '.tpr',
                                       '-c', init_gro + '.gro',
                                       '-r', init_gro + '.gro',
                                       '-p', topol + '.top',
                                       '-n', index + '.ndx',
                                       '-maxwarn', str(maxwarn)])
        error = prepare_init.returncode
        print(error)
        if error != 0:
            sys.exit()

    def prepare(self, mdp, istep, pstep, topol, index, maxwarn):
        prepare = subprocess.run(['gmx_mpi',
                                  'grompp',
                                  '-f', mdp + '.mdp',
                                  '-o', istep + '.tpr',
                                  '-c', pstep + '.gro',
                                  '-t', pstep + '.cpt',
                                  '-p', topol + '.top',
                                  '-n', index + '.ndx',
                                  '-maxwarn', str(maxwarn)])
        error = prepare.returncode
        print(error)
        if error != 0:
            sys.exit()

    def run(self, ntmpi, ntomp, dds, dlb, istep, gpu):
        if gpu == 0:
            pinoffset = 0

        elif gpu == 1:
            pinoffset = 12
        run = subprocess.run(['mpirun',
                              '-np', str(ntmpi),
                              'gmx_mpi',
                              'mdrun',
                              '-v',
                              '-ntomp', str(ntomp),
                              '-gpu_id', str(gpu),
                              '-pin on',
                              '-pinoffset', str(pinoffset),
                              '-pinstride 1',
                              '-dds', str(dds),
                              '-dlb', dlb,
                              '-deffnm', istep])
        error = run.returncode
        print(error)
        if error != 0:
            sys.exit()

    def clean_backups(self):
        print('\nCleaning the backups...\n')
        sleep(3)
        subprocess.run(['rm -f \#*\#'], shell=True) # noqa

    def stuckfixer(self, line_number, ps_time, nr, fixer):
        # reading last last 5, 8, 10 lines to change simulation time if fixer = True in input.py
        distance = []
        if exists("log_slope.txt") and fixer is True and nr > 10:
            with open("log_slope.txt") as f:
                for line in (f.readlines()[-int(line_number):]):
                    cols = line.split()
                    distance.append(float(cols[0]))
            deviation_d = np.std(distance)
            if deviation_d < 0.03:
                with open(self.mdpfilePath, "r+") as mdpFile:
                    content = mdpFile.read()
                    content = re.sub('nsteps.*\n', '', content, flags=re.M) # noqa
                    content = re.sub(r"(dt.*$)", r"\1\nnsteps                  = "+str(ps_time), content, flags=re.MULTILINE) # noqa
                    mdpFile.seek(0)
                    mdpFile.write(content)
                    mdpFile.truncate()
            else:
                with open(self.mdpfilePath, "r+") as mdpFile:
                    content = mdpFile.read()
                    content = re.sub('nsteps.*\n', '', content, flags=re.M) # noqa
                    content = re.sub(r"(dt.*$)", r"\1\nnsteps                  = 300000", content, flags=re.MULTILINE) # noqa
                    mdpFile.seek(0)
                    mdpFile.write(content)
                    mdpFile.truncate()

    def stage(self, distance, rdist1, rdist2):
        if mean(distance) < 0.5:
            rdist = rdist2
            file_name = 'log_slope.txt'
            log_file = open(file_name, 'a+')
            log_file.write("----- Stage 2 has started... -----")
            log_file.close()
        else:
            rdist = rdist1
        return rdist
