# MultiGRO
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
GROMACS 2021 multicore version needs to be installed. It needs to be modified for older versions since `-r` argument has been added for `grompp` module in 2021 version.

  ```bash
   # Add gromacs 'gmx_mpi' path:
   export PATH='*path_to_gromacs*/bin/':$PATH
  ```
## Usage
### PVT Curves
Pressure-volume-temperature (PVT) curves are used to determine glass transition temperature (_T_<sub>g</sub>)) of materials. `run_tg.sh` is located at `pvt_curves/` directory and starts a loop run from the specified starting temperature to specified ending temperature with an inverval of 25 K.  

  Structure:\
  ```bash
  ./run_tg.sh -n number_cores -f user.mdp -c initial.gro -i starting_temp -m ending_temp
  ```
  `-n`: number of cores (integer)\
  `-f`: GROMACS .mdp inputfile\
  `-c`: initial .gro structure file\
  `-i`: Starting temperature of PVT (integer, kelvin)\
  `-m`: Ending Temperature of PVT (integer, kelvin)\
  As an example, if simulation would be run from 700K to 150K with user.mdp and initial.gro using 12 cores:\
  ```bash
  chmod a+x run_tg.sh
  ./run_tg.sh -n 12 -f user.mdp -c initial.gro -i 700 -m 150
  ```
  
  
