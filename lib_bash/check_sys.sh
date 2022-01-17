#!/bin/bash
# Running GROMACS with input files to produce PVT curve for Tg Values
# Hüsamettin Deniz Özeren (https://github.com/hozeren)
# set verbose level to info
__VERBOSE=10

check_cmd() {
    if [[ ! $(command -v "$1") ]]; then
        echo "It seems like you have $1! Nice work!";
        sleep 2
    else    
        echo "Go and Install $1!!! Then come back anytime.";
        sleep 2
        exit 1
    fi
}

# check commands
check_cmd mpirun
check_cmd gmx_mpi