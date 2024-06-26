lipid=DPPC

python3 ../plot_meanclusdppc.py --suffix full --yRange "(0,0.3)" --xRange "(0,250)" --xLabel "Mean number of ${lipid} in ${lipid} clusters" --dat_files freeEnergyLandscapes/*.dat
python3 ../plot_meanclusdppc.py --suffix 324-972 --yRange "(0,0.3)" --xRange "(0,250)" --xLabel "Mean number of ${lipid} in ${lipid} clusters" --dat_files freeEnergyLandscapes/{324,648,972}.dat
python3 ../plot_meanclusdppc.py --suffix 1944-10100 --yRange "(0,0.3)" --xRange "(0,250)" --xLabel "Mean number of ${lipid} in ${lipid} clusters" --dat_files freeEnergyLandscapes/{1944,3888,7776,10110}.dat
