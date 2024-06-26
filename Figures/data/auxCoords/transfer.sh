#!/usr/bin/env bash

for lipid in dppc dipc chol
do
    for aux in clucount coreby clusby meanclus stdclus meancore stdcore sc
    do
        mkdir -p ${aux}${lipid}
        for size in 324 648 972 1944 3888 7776 10110
        do
            cp -prf ../../../DIPC_DPPC_${size}_lipid_systems/WE_runs/Analysis/data/multi_west_aux/${aux}${lipid}_average_1-9.dat ${aux}${lipid}/${size}.dat
        done
    done
done

