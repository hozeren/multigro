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
    echo "Usage: $0 [-n <Number of cores>] [-c <.GRO file>]"
    echo "  -f      trajectory file (ex. *.trr, *.xtc)"
    echo "  -c      initial .gro structure file"
    echo "  -b      Starting step for the trajectories"
    echo "Add *.tpr file in the same folder."
    exit 1
}

while getopts f:c:b: flag
do
#[[ ${OPTARG} == -* ]] && { echo "Missing argument for -${flag}" ; exit 1 ; }
    case "${flag}" in
        n) xtc=${OPTARG};;
        c) init=${OPTARG%".gro"};;
        b) b=${OPTARG%".gro"};;
    esac
done

if [ -z "$xtc" ] || [ -z "$init" ] || [ ! -f $folder/topol.tpr ]; then
   usage
   exit
fi

if [ -z "$b" ]; then
    b=0
fi

echo "Input parameters are shown below:"
echo "TRJ: $xtc";
echo ".GRO: $init.gro";
tpr=${xtc%".xtc"}
sleep 2
echo ""

gmx_mpi trjconv -s $tpr.tpr -f $xtc -center -ur compact -pbc mol -o center_$xtc