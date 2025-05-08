# Python-script-for-LAMMPS-dump-file-processing
  This program is designed to quickly extract information output by the dump command and can flexibly extract specified columns in the dump file.
The dump file output format in lammps is:

dump          1  pdos custom 10 dump.txt id type x y z vx vy vz 

dump_modify   1  sort id

<img width="347" alt="1746712437175" src="https://github.com/user-attachments/assets/388787bd-55cd-4af4-a89e-ffbc80e2011a" />

  In order to facilitate subsequent calculations, the dump file needs to be preprocessed to retain only pure data.

**deal.py:** The program skips the first 9 lines, reads the atomic data of each time step line by line, extracts and saves the required columns, and saves them to the specified output path.

**Need to be modified:** input and output file paths and specify the columns to be extracted.

**References and Acknowledgements**:https://github.com/Tingliangstu/Lammps_tools
