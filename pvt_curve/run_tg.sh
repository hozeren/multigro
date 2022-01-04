#!/bin/bash
# Running GROMACS with input files to produce PVT curve for Tg Values
# Hüsamettin Deniz Özeren (https://github.com/hozeren)
# set verbose level to info
__VERBOSE=10

init=21               #initial .gro
np=12                 #number of cores to use with mpirun
folder=`pwd`          #directory where .gro, .mdp, etc.
input=pvt             #name of the input file .mdp

int=700               #first temperature
intmin=150            #last temperature

while [ $int -gt $intmin ]
do
    pint=$(( int+25 ))

    cd $folder
    mkdir $int
    cp topol.top $int/

     
    if  [ "$int" -eq 700 ] ; then
        cp $init.gro $int/
        cp $input.mdp $folder/$int/$int.mdp 
        cd $int
        #sed -i '39d' $int.mdp
        sed -i '/^ref_t.*/d' $int.mdp
        sed -i "/^tau_t.*/a ref_t\t\t\= $int" $int.mdp  

        gmx_mpi grompp -f npt$int.mdp -o $int.tpr -c $init.gro -r $init.gro -p topol.top -n index.ndx
        mpirun -np $np gmx_mpi mdrun -v -deffnm $int
        int=$(( int-25 ))
    else
        cp $folder/$pint/$pint.gro $folder/$int/$pint.gro
        cp ${input}.mdp $folder/$int/$int.mdp 
        cd $int
        sed -i '/^ref_t.*/d' $int.mdp
        sed -i "/^tau_t.*/a ref_t\t\t\= $int" $int.mdp 

        gmx_mpi grompp -f npt$int.mdp -o $int.tpr -c $pint.gro -r $init.gro -p topol.top -n index.ndx
        mpirun -np $np gmx_mpi mdrun -v -deffnm $int
        int=$(( int-25 ))
    fi
done