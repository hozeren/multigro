#!/bin/bash
# Running GROMACS with input files to produce PVT curve for Tg Values
# Hüsamettin Deniz Özeren (https://github.com/hozeren)
# set verbose level to info
__VERBOSE=10

#init=.gro               #initial .gro
#np=12                   #number of cores to use with mpirun
#input=.mdp              #name of the input file .mdp
folder=`pwd`             #directory where .gro, .mdp, etc.

#Input parameters
while getopts n:f:c: flag
do
    case "${flag}" in
        n) np=${OPTARG};;
        f) input=${OPTARG%".mdp"};;
        c) init=${OPTARG%".gro"};;
    esac
done
echo "Input parameters are shown below:"
echo "Cores: $np cores";
echo ".MDP: $input.mdp";
echo ".GRO: $init.gro";

sleep 2
echo "Simulations are starting... Sit tight."
sleep 3

int=1
intmax=21
#Simulation Loop
while [ $int -gt $intmax ]
do
    pint=$(( int+25 ))

     
    if  [ "$int" -eq 1 ] ; then
        cp $init.gro $int/
        cp $input.mdp $folder/$int/$int.mdp 
        cd $int

        gmx_mpi grompp -f npt$int.mdp -o $int.tpr -c $init.gro -r $init.gro -p topol.top -n index.ndx
        mpirun -np $np gmx_mpi mdrun -v -deffnm $int
        int=$(( int+1 ))
    else
        cp $folder/$pint/$pint.gro $folder/$int/$pint.gro
        cp ${input}.mdp $folder/$int/$int.mdp 
        cd $int
        sed -i '/^ref_t.*/d' $int.mdp
        sed -i "/^tau_t.*/a ref_t\t\t\= $int" $int.mdp 

        gmx_mpi grompp -f npt$int.mdp -o $int.tpr -c $pint.gro -r $init.gro -p topol.top -n index.ndx
        mpirun -np $np gmx_mpi mdrun -v -deffnm $int
        int=$(( int+1 ))
    fi
done