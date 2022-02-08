#!/bin/bash
# Running GROMACS with input files to produce PVT curve for Tg Values
# Hüsamettin Deniz Özeren (https://github.com/hozeren)
# set verbose level to info
__VERBOSE=10

#init=.gro               #initial .gro
#np=12                   #number of cores to use with mpirun
folder=`pwd`             #directory where .gro, .mdp, etc.

if [ ! -f $folder/topol.top ] || [ ! -f $folder/index.ndx ]; then
    echo "topol.top AND/OR index.ndx is missing on the path!"
    exit
fi

#Input parameters
usage() 
{ 
    echo "Usage: $0 [-n <Number of cores>] [-c <.GRO file>]"
    echo "  -n      number of cores (integer)"
    echo "  -c      initial .gro structure file"
    exit 1
}
while getopts n:c: flag
do
#[[ ${OPTARG} == -* ]] && { echo "Missing argument for -${flag}" ; exit 1 ; }
    case "${flag}" in
        n) np=${OPTARG};;
        c) init=${OPTARG%".gro"};;
    esac
done

if [ -z "$np" ] || [ -z "$init" ]; then
   usage
   exit
fi

echo "Input parameters are shown below:"
echo "Cores: $np cores";
echo ".GRO: $init.gro";
sleep 2
echo ""
echo "Minimization is starting... "
echo ""
sleep 2

cp $folder/inputs/min.mdp $folder/min.mdp

gmx_mpi grompp -f min.mdp -o min.tpr -c $init.gro -r $init.gro -p topol.top -n index.ndx
mpirun -np $np gmx_mpi mdrun -v -deffnm min

echo "21 step simulations are starting... Sit tight."
sleep 3

int=1
intmax=21
minit=min

#Simulation Loop
while [ $int -le $intmax ]
do
    pint=$(( int-1 ))
    echo ""
    echo "Step $int started..."
    echo ""
    sleep 3
    cd $folder
    mkdir $int
    cp topol.top $int/
    cp index.ndx $int/
     
    if  [ "$int" -eq 1 ] ; then
        cp $minit.gro $int/
        cp $folder/inputs/$int.mdp $folder/$int/$int.mdp 
        cd $int

        gmx_mpi grompp -f $int.mdp -o $int.tpr -c $minit.gro -r $minit.gro -p topol.top -n index.ndx
        mpirun -np $np gmx_mpi mdrun -v -deffnm $int
        int=$(( int+1 ))
    else
        cp $folder/$pint/$pint.gro $folder/$int/$pint.gro
        cp $folder/inputs/$int.mdp $folder/$int/$int.mdp
        cd $int

        gmx_mpi grompp -f $int.mdp -o $int.tpr -c $pint.gro -r $pint.gro -p topol.top -n index.ndx
        mpirun -np $np gmx_mpi mdrun -v -deffnm $int
        int=$(( int+1 ))
    fi
done