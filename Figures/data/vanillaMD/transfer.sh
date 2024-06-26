#!/usr/bin/env bash

for size in 324 648 972 1944 3888 7776 10110
do
    for temp in 323 423
    do
        for replica in 1 2 3 4
        do
            mkdir -p FLC/${size}/${temp}/
            cp -prf ../../../DIPC_DPPC_${size}_lipid_systems/production_runs/0${replica}/${temp}K/visual/pcoord_refine.dat FLC/${size}/${temp}/${replica}.dat
        done
    done
done

for aux in clustcount coreby clusby meancore meanclus stdcore stdclus sc
do
    for lipid in dppc dipc chol
    do
        for size in 324 648 972 1944 3888 7776 10110
        do
            for temp in 323 423
            do
                for replica in 1 2 3 4
                do
                    mkdir -p ${aux}_${lipid}/${size}/${temp}/
                    cp -prf ../../../DIPC_DPPC_${size}_lipid_systems/production_runs/0${replica}/${temp}K/visual/${aux}_${lipid}.dat ${aux}_${lipid}/${size}/${temp}/${replica}.dat
                done
            done
        done
    done
done
