# MultiGRO
***Still in WIP STAGE***
***Transition from bash to python is ongoing, the expected final package will be finished within three months***

Bash shell scripts for GROMACS to run multiple simulations and their analysis at once.

<p align="center">
<img src="MultiGRO-logo.png"  alt="MultiGRO" width="70%">
</p>
<p align="center">

MultiGRO consists of two seperated components;

1. **21 step equilibration:** It is well known 21 step decompression equilibration method.
2. **PVT Curves for _T_<sub>g</sub> values:** A method to create PVT curves for glass transition temperature (_T_<sub>g</sub>).

## Directories

## Download

## Dependencies
* GROMACS 2021 with MPI is needed to be installed. The scripts needs to be modified for older versions since `-r` argument has been added for `grompp` module in 2021 version.

  ```bash
   # Add gromacs 'gmx_mpi' path:
   export PATH='*path_to_gromacs*/bin/':$PATH
  ```
## Usage
### 21 Step Equilibration
21 step equilibration is a well known method that is used for equilibration at the initial state of amorphous. `21step.sh` is located at `21step/` directory and starts a loop run which uses `21step/inputs/*.mdp` files as inputs.
 * Run structure:
  ```bash
  ./21step.sh -n number_cores -c initial.gro
  ```
  `-n`: number of cores (integer)\
  `-c`: initial .gro structure file\
    * Script needs topology (.top) and index file (.ndx) in the same folder.

### PVT Curves
Pressure-volume-temperature (PVT) curves are used to determine glass transition temperature (_T_<sub>g</sub>) of materials. `run_tg.sh` is located at `pvt_curves/` directory and starts a loop run from the specified starting temperature to specified ending temperature with an inverval of 25 K.  

 * Run structure:
  ```bash
  ./run_tg.sh -n number_cores -f user.mdp -c initial.gro -i starting_temp -m ending_temp
  ```
  `-n`: number of cores (integer)\
  `-f`: GROMACS .mdp inputfile\
  `-c`: initial .gro structure file\
  `-i`: Starting temperature of PVT (integer, kelvin)\
  `-m`: Ending Temperature of PVT (integer, kelvin)\
    * Script needs topology (.top) and index file (.ndx) in the same folder.
 * As an example, if simulation would be run from 700K to 150K with user.mdp and initial.gro using 12 cores:
  ```bash
  chmod a+x run_tg.sh
  ./run_tg.sh -n 12 -f user.mdp -c initial.gro -i 700 -m 150
  ```
 * Densities can be extracted using `denity.sh`, which is located at `pvt_curves/analysis/`:
  ```bash
  chmod a+x density.sh
  ./density.sh i starting_temp -m ending_temp -d density_code -b starting_step
  #example for run above
  ./density.sh -i 700 -m 150 -d 20 -b 4500
  ```
    * Output includes three columns; density, standard error and rmsd. 
  
  
