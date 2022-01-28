#!/bin/bash
#author		     :Hüsamettin Deniz Özeren (https://github.com/hozeren)
#date            :2022-01-24
#notes           :Trajectory optimizer from gromacs to vmd
#==============================================================================
# set verbose level to info
__VERBOSE=10
folder=`pwd`             #directory where .gro, .mdp, etc.

#Input parameters
usage() 
{ 
    echo "Usage: $0 [-f <trajectory file>]"
    echo "  -f      trajectory file (ex. *.trr, *.xtc)"
    echo "  -b      Starting step for the trajectories"
    echo "Add *.tpr file in the same folder."
    exit 1
}

while getopts f:b flag
do
    case "${flag}" in
        f) xtc=${OPTARG};;
        b) b=${OPTARG};;
    esac
done

tpr=${xtc%".xtc"}

if [ -z "$xtc" ] || [ ! -f $folder/$tpr.tpr ]; then
   usage
   exit
fi

if [ -z "$b" ]; then
    b=0
fi

echo "Input parameters are shown below:"
echo "TRJ: $xtc";
echo "TPR: $tpr"".tpr"
echo "Starting Step: $b ps"

sleep 3
echo ""

gmx_mpi trjconv -s $tpr.tpr -f $xtc -center -ur compact -pbc mol -o center_$xtc