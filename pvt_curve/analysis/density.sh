#!/bin/bash
# Running GROMACS with input files to produce PVT curve for Tg Values
# Hüsamettin Deniz Özeren (https://github.com/hozeren)
# set verbose level to info
__VERBOSE=10

int=700        #first temperature
intmin=150        #last temperature
st_time=4500      #starting temperature in ps 
d_code=19         #density code (number when energy is run)
folder=`pwd`

while [ $int -gt $intmin ]
do
    if [ "$int" -eq 700 ] ; then
        cd $folder/$int
        echo $d_code | gmx_mpi energy -f $int.edr -b $st_time -o denisty_$int.xvg | awk -v OFS='\t' '/Energy/ {print $2, $3, $4} END {print $2, $3, $4}'| tee -a density.txt
        int=$(( int-25 ))

    else
        cd $folder/$int
        echo $d_code | gmx_mpi energy -f $int.edr -b $st_time -o denisty_$int.xvg | awk -v OFS='\t' 'END {print $2, $3, $4}'| tee -a density.txt
        int=$(( int-25 ))

    fi
done
#grep -oP '(?<=Density)[\d.]+' 