#!/usr/bin/env bash

for size in 324 648 972 1944 3888 # 7776 10110
do
    cp -prf ../../../DIPC_DPPC_${size}_lipid_systems/WE_runs/Analysis/data/multi_west/average_991-1000.dat ${size}.dat
    # cp -prf ../../../DIPC_DPPC_${size}_lipid_systems/WE_runs/Analysis/data/multi_west/average_491-500.dat ${size}.dat
done


cp -prf ../../../DIPC_DPPC_7776_lipid_systems/WE_runs/Analysis/data/multi_west/average_591-600.dat 7776.dat
cp -prf ../../../DIPC_DPPC_10110_lipid_systems/WE_runs/Analysis/data/multi_west/average_491-500.dat 10110.dat
