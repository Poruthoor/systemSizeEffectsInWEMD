#!/usr/bin/env bash

# Removing previous data and plots
rm -rf *.dat
rm -rf *.pdf

# Generating data for the plots from the data files
for temp in 323 423
do
    for size in 324 648 972 1944 3888 7776 10110
    do
        for replica in 1 2 3 4
        do
            mkdir -p ${size}/
            python3 ../src/avgVar_stdMD.py --replicaNum ${replica} --dat_file ../data/vanillaMD/FLC/${size}/${temp}/${replica}.dat >> ${size}/${temp}.dat 
        done
        python3 ../src/summarizeReplicas.py  --size ${size} --dat_file ${size}/${temp}.dat >> ${temp}.dat
    done
done

# Ploting the data
python3 plot2.py --suffix "systemFLC"  --dat_file *.dat
