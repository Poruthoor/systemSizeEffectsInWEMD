#!/usr/bin/env bash

# # Removing previous data and plots
# rm -rf *.dat
# rm -rf *.pdf

# rm -rf freeEnergyLandscapes*
# mkdir -p freeEnergyLandscapes
# mkdir -p freeEnergyLandscapes_offset

# # Generating data for the plots from the data files
# bash prob2kcalPerMol.sh

# # Ploting  the data
# python3 plot.py --suffix full --dat_files freeEnergyLandscapes/*.dat
# python3 plot.py --suffix 324-972 --dat_files freeEnergyLandscapes/{324,648,972}.dat
# python3 plot.py --suffix 1944-10100 --dat_files freeEnergyLandscapes/{1944,3888,7776,10110}.dat

# cd freeEnergyLandscapes_offset/
# python3 ../offset.py ../freeEnergyLandscapes/324.dat 0
# python3 ../offset.py ../freeEnergyLandscapes/648.dat 0.75
# python3 ../offset.py ../freeEnergyLandscapes/972.dat 1.5
# python3 ../offset.py ../freeEnergyLandscapes/1944.dat 2.25
# python3 ../offset.py ../freeEnergyLandscapes/3888.dat 3
# python3 ../offset.py ../freeEnergyLandscapes/7776.dat 3.75
# python3 ../offset.py ../freeEnergyLandscapes/10110.dat 4.5

# cd ../

# python3 plot.py --suffix full_offset --yRange "(0, 9)" --dat_files freeEnergyLandscapes_offset/*.dat

python3 plot_dark.py --suffix 324 --dat_files freeEnergyLandscapes/324.dat
python3 plot_dark.py --suffix 648 --dat_files freeEnergyLandscapes/648.dat
python3 plot_dark.py --suffix 972 --dat_files freeEnergyLandscapes/972.dat
python3 plot_dark.py --suffix 1944 --dat_files freeEnergyLandscapes/1944.dat
python3 plot_dark.py --suffix 3888 --dat_files freeEnergyLandscapes/3888.dat
python3 plot_dark.py --suffix 7776 --dat_files freeEnergyLandscapes/7776.dat
python3 plot_dark.py --suffix 10110 --dat_files freeEnergyLandscapes/10110.dat
