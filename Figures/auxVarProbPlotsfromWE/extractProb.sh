#!/usr/bin/env bash

for size in 324 648 972 1944 3888 7776 10110
do
    python3 ../../src/extractProb.py  --suffix freeEnergyLandscapes/${size} --dat_file ../../data/auxCoords/${1}/${size}.dat 
done
