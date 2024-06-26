#!/usr/bin/env bash

# Removing previous data and plots
rm -rf *.dat
rm -rf *.pdf

rm -rf rollingStd
rm -rf peakInfo
rm -rf avgVarFLC
mkdir -p rollingStd
mkdir -p peakInfo
mkdir -p avgVarFLC

# Generating data for the plots from the data files
for size in 324 648 972 1944 3888 7776 10110
do
    python3 ../src/runningStdDelG.py  --size rollingStd/${size} --dat_file ../data/FLC/${size}.dat
    python3 ../src/peaksHeights.py  --size peakInfo/${size} --dat_file ../data/FLC/${size}.dat
    python3 ../src/avgVarFLC.py  --size avgVarFLC/${size} --outputFile True --dat_file ../data/FLC/${size}.dat
done

# # Ploting the data
python3 plot.py --suffix full
# python3 plot_dark.py --suffix full_dark

# python3 plot.py --suffix full --dat_files rollingStd/*.dat
# python3 plot.py --suffix 324-1944 --dat_files rollingStd/{324,648,972,1944}.dat
# python3 plot.py --suffix 3888-10100 --dat_files rollingStd/{3888,7776,10110}.dat
