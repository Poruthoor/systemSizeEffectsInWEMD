#!/usr/bin/env bash

# Removing previous data and plots
rm -rf *.dat
rm -rf *.pdf

# Generating data for the plots from the data files
for lipid in dppc dipc chol
do
    for temp in 323 423
    do
        for size in 324 648 972 1944 3888 7776 10110
        do
            for replica in 1 2 3 4
            do
                mkdir -p ${lipid}/${size}/
                python3 ../src/avgVar_stdMD.py --replicaNum ${replica} --dat_file ../data/vanillaMD/meanclus_${lipid}/${size}/${temp}/${replica}.dat >> ${lipid}/${size}/${temp}.dat
            done
            python3 ../src/summarizeReplicas.py  --size ${size} --dat_file ${lipid}/${size}/${temp}.dat >> ${lipid}_${temp}.dat
        done
    done
done

# Ploting the data
python3 plot2.py --suffix "lipid_meanSize"  --dat_file *.dat
