#!/bin/bash

#modify with T1=temperature == $T1

gmx_mpi grompp -f nvt.mdp -c npt_new.gro -p topol.top -o nvt70.tpr
mpirun -np 48 gmx_mpi mdrun -dds 0.9 -v -deffnm nvt70


gmx_mpi grompp -f npt.mdp -c nvt70.gro -p topol.top -o npt67.tpr
mpirun -np 48 gmx_mpi mdrun -dds 0.9 -v -deffnm npt67


echo "Starting run PVT at 675K..."
mkdir 675K
cp topol.top npt67.gro npt675K.mdp 675K/
cd 675K
gmx_mpi grompp -f npt675K.mdp -c npt67.gro -p topol.top -o 675K.tpr
mpirun -np 48 gmx_mpi mdrun -dds 0.9 -v -deffnm 675K


echo "Starting run PVT at 650K..."
cd ..
mkdir 650K
cp /pfs/nobackup/home/o/ozeren/xinfeng/GLU30_w/tg/675K/675K.gro 650K/
cp topol.top npt650K.mdp 650K/
cd 650K
gmx_mpi grompp -f npt650K.mdp -c 675K.gro -p topol.top -o 650K.tpr
mpirun -np 48 gmx_mpi mdrun -dds 0.9 -v -deffnm 650K


echo "Starting run PVT at 625K..."
cd ..
mkdir 625K
cp /pfs/nobackup/home/o/ozeren/xinfeng/GLU30_w/tg/650K/650K.gro 625K/
cp topol.top npt625K.mdp 625K/
cd 625K
gmx_mpi grompp -f npt625K.mdp -c 650K.gro -p topol.top -o 625K.tpr
mpirun -np 48 gmx_mpi mdrun -dds 0.9 -v -deffnm 625K


echo "Starting run PVT at 600K..."
cd ..
mkdir 600K
cp /pfs/nobackup/home/o/ozeren/xinfeng/GLU30_w/tg/625K/625K.gro 600K/
cp topol.top npt600K.mdp 600K/
cd 600K
gmx_mpi grompp -f npt600K.mdp -c 625K.gro -p topol.top -o 600K.tpr
mpirun -np 48 gmx_mpi mdrun -dds 0.9 -v -deffnm 600K

echo "Starting run PVT at 575K..."
cd ..
mkdir 575K
cp /pfs/nobackup/home/o/ozeren/xinfeng/GLU30_w/tg/600K/600K.gro 575K/
cp topol.top npt575K.mdp 575K/
cd 575K
gmx_mpi grompp -f npt575K.mdp -c 600K.gro -p topol.top -o 575K.tpr
mpirun -np 48 gmx_mpi mdrun -dds 0.9 -v -deffnm 575K

echo "Starting run PVT at 550K..."
cd ..
mkdir 550K
cp /pfs/nobackup/home/o/ozeren/xinfeng/GLU30_w/tg/575K/575K.gro 550K/
cp topol.top npt550K.mdp 550K/
cd 550K
gmx_mpi grompp -f npt550K.mdp -c 575K.gro -p topol.top -o 550K.tpr
mpirun -np 48 gmx_mpi mdrun -dds 0.9 -v -deffnm 550K

echo "Starting run PVT at 525K..."
cd ..
mkdir 525K
cp /pfs/nobackup/home/o/ozeren/xinfeng/GLU30_w/tg/550K/550K.gro 525K/
cp topol.top npt525K.mdp 525K/
cd 525K
gmx_mpi grompp -f npt525K.mdp -c 550K.gro -p topol.top -o 525K.tpr
mpirun -np 48 gmx_mpi mdrun -dds 0.9 -v -deffnm 525K

echo "Starting run PVT at 500K..."
cd ..
mkdir 500K
cp /pfs/nobackup/home/o/ozeren/xinfeng/GLU30_w/tg/525K/525K.gro 500K/
cp topol.top npt500K.mdp 500K/
cd 500K
gmx_mpi grompp -f npt500K.mdp -c 525K.gro -p topol.top -o 500K.tpr
mpirun -np 48 gmx_mpi mdrun -dds 0.9 -v -deffnm 500K

echo "Starting run PVT at 475K..."
cd ..
mkdir 475K
cp /pfs/nobackup/home/o/ozeren/xinfeng/GLU30_w/tg/500K/500K.gro 475K/
cp topol.top npt475K.mdp 475K/
cd 475K
gmx_mpi grompp -f npt475K.mdp -c 500K.gro -p topol.top -o 475K.tpr
mpirun -np 48 gmx_mpi mdrun -dds 0.9 -v -deffnm 475K

echo "Starting run PVT at 450K..."
cd ..
mkdir 450K
cp /pfs/nobackup/home/o/ozeren/xinfeng/GLU30_w/tg/475K/475K.gro 450K/
cp topol.top npt450K.mdp 450K/
cd 450K
gmx_mpi grompp -f npt450K.mdp -c 475K.gro -p topol.top -o 450K.tpr
mpirun -np 48 gmx_mpi mdrun -dds 0.9 -v -deffnm 450K

echo "Starting run PVT at 425K..."
cd ..
mkdir 425K
cp /pfs/nobackup/home/o/ozeren/xinfeng/GLU30_w/tg/450K/450K.gro 425K/
cp topol.top npt425K.mdp 425K/
cd 425K
gmx_mpi grompp -f npt425K.mdp -c 450K.gro -p topol.top -o 425K.tpr
mpirun -np 48 gmx_mpi mdrun -dds 0.9 -v -deffnm 425K

echo "Starting run PVT at 400K..."
cd ..
mkdir 400K
cp /pfs/nobackup/home/o/ozeren/xinfeng/GLU30_w/tg/425K/425K.gro 400K/
cp topol.top npt400K.mdp 400K/
cd 400K
gmx_mpi grompp -f npt400K.mdp -c 425K.gro -p topol.top -o 400K.tpr
mpirun -np 48 gmx_mpi mdrun -dds 0.9 -v -deffnm 400K

echo "Starting run PVT at 375K..."
cd ..
mkdir 375K
cp /pfs/nobackup/home/o/ozeren/xinfeng/GLU30_w/tg/400K/400K.gro 375K/
cp topol.top npt375K.mdp 375K/
cd 375K
gmx_mpi grompp -f npt375K.mdp -c 400K.gro -p topol.top -o 375K.tpr
mpirun -np 48 gmx_mpi mdrun -dds 0.9 -v -deffnm 375K

echo "Starting run PVT at 350K..."
cd ..
mkdir 350K
cp /pfs/nobackup/home/o/ozeren/xinfeng/GLU30_w/tg/375K/375K.gro 350K/
cp topol.top npt350K.mdp 350K/
cd 350K
gmx_mpi grompp -f npt350K.mdp -c 375K.gro -p topol.top -o 350K.tpr
mpirun -np 48 gmx_mpi mdrun -dds 0.9 -v -deffnm 350K

echo "Starting run PVT at 325K..."
cd ..
mkdir 325K
cp /pfs/nobackup/home/o/ozeren/xinfeng/GLU30_w/tg/350K/350K.gro 325K/
cp topol.top npt325K.mdp 325K/
cd 325K
gmx_mpi grompp -f npt325K.mdp -c 350K.gro -p topol.top -o 325K.tpr
mpirun -np 48 gmx_mpi mdrun -dds 0.9 -v -deffnm 325K

echo "Starting run PVT at 300K..."
cd ..
mkdir 300K
cp /pfs/nobackup/home/o/ozeren/xinfeng/GLU30_w/tg/325K/325K.gro 300K/
cp topol.top npt300K.mdp 300K/
cd 300K
gmx_mpi grompp -f npt300K.mdp -c 325K.gro -p topol.top -o 300K.tpr
mpirun -np 48 gmx_mpi mdrun -dds 0.9 -v -deffnm 300K

echo "Starting run PVT at 275K..."
cd ..
mkdir 275K
cp /pfs/nobackup/home/o/ozeren/xinfeng/GLU30_w/tg/300K/300K.gro 275K/
cp topol.top npt275K.mdp 275K/
cd 275K
gmx_mpi grompp -f npt275K.mdp -c 300K.gro -p topol.top -o 275K.tpr
mpirun -np 48 gmx_mpi mdrun -dds 0.9 -v -deffnm 275K

echo "Starting run PVT at 250K..."
cd ..
mkdir 250K
cp /pfs/nobackup/home/o/ozeren/xinfeng/GLU30_w/tg/275K/275K.gro 250K/
cp topol.top npt250K.mdp 250K/
cd 250K
gmx_mpi grompp -f npt250K.mdp -c 275K.gro -p topol.top -o 250K.tpr
mpirun -np 48 gmx_mpi mdrun -dds 0.9 -v -deffnm 250K

echo "Starting run PVT at 225K..."
cd ..
mkdir 225K
cp /pfs/nobackup/home/o/ozeren/xinfeng/GLU30_w/tg/250K/250K.gro 225K/
cp topol.top npt225K.mdp 225K/
cd 225K
gmx_mpi grompp -f npt225K.mdp -c 250K.gro -p topol.top -o 225K.tpr
mpirun -np 48 gmx_mpi mdrun -dds 0.9 -v -deffnm 225K

echo "Starting run PVT at 200K..."
cd ..
mkdir 200K
cp /pfs/nobackup/home/o/ozeren/xinfeng/GLU30_w/tg/225K/225K.gro 200K/
cp topol.top npt200K.mdp 200K/
cd 200K
gmx_mpi grompp -f npt200K.mdp -c 225K.gro -p topol.top -o 200K.tpr
mpirun -np 48 gmx_mpi mdrun -dds 0.9 -v -deffnm 200K

echo "Starting run PVT at 175K..."
cd ..
mkdir 175K
cp /pfs/nobackup/home/o/ozeren/xinfeng/GLU30_w/tg/200K/200K.gro 175K/
cp topol.top npt175K.mdp 175K/
cd 175K
gmx_mpi grompp -f npt175K.mdp -c 200K.gro -p topol.top -o 175K.tpr
mpirun -np 48 gmx_mpi mdrun -dds 0.9 -v -deffnm 175K

echo "Starting run PVT at 150K..."
cd ..
mkdir 150K
cp /pfs/nobackup/home/o/ozeren/xinfeng/GLU30_w/tg/175K/175K.gro 150K/
cp topol.top npt150K.mdp 150K/
cd 150K
gmx_mpi grompp -f npt150K.mdp -c 175K.gro -p topol.top -o 150K.tpr
mpirun -np 48 gmx_mpi mdrun -dds 0.9 -v -deffnm 150K

echo "PVT job complete."






