#!/usr/bin/env bash

# Removing previous data and plots
rm -rf ddG.dat

# Generating data for the plots from source data files
for size in 324 648 972 1944 3888 7776 10110 # 324 648 972 
do
    python3 ../src/ddG.py  --size ${size} --dat_file ../data/FLC/${size}.dat >> ddG.dat
    python3 ../src/maxBarrierInfo.py  --size ${size} --dat_file ../data/FLC/${size}.dat >> maxBarrierInfo.dat
done

# Ploting the data
python3 plot2.py --suffix "ddG"  --dat_file ddG.dat
# python3 plot2.py --suffix "ddG_log" --xlog True --dat_file ddG.dat
