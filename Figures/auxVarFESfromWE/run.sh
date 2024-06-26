#! /bin/bash
#SBATCH -p debug
#SBATCH -t 01:00:00
#SBATCH -c 1
#SBATCH -J run
#SBATCH -o run_o
#SBATCH -e run_e

CURRENT=$PWD

for lipid in dppc dipc chol
do
    for aux in clucount 
    do
        mkdir -p ${aux}${lipid}

        cd ${aux}${lipid}/

        # Removing previous data and plots
        rm -rf *.dat
        rm -rf *.pdf

        rm -rf freeEnergyLandscapes
        mkdir -p freeEnergyLandscapes

        # Generating data for the plots from the data files
        bash ../prob2kcalPerMol.sh ${aux}${lipid}

        # Ploting  the data
        python3 ../plot.py --suffix full --xRange "(0,50)" --xLabel "Cluster counts" --dat_files freeEnergyLandscapes/*.dat
        python3 ../plot.py --suffix 324-972 --xRange "(0,50)" --xLabel "Cluster counts" --dat_files freeEnergyLandscapes/{324,648,972}.dat
        python3 ../plot.py --suffix 1944-10100 --xRange "(0,50)" --xLabel "Cluster counts" --dat_files freeEnergyLandscapes/{1944,3888,7776,10110}.dat

        cd $CURRENT
    done
done

for lipid in dppc dipc chol
do
    for aux in coreby clusby 
    do
        mkdir -p ${aux}${lipid}

        cd ${aux}${lipid}/

        # Removing previous data and plots
        rm -rf *.dat
        rm -rf *.pdf

        rm -rf freeEnergyLandscapes
        mkdir -p freeEnergyLandscapes

        # Generating data for the plots from the data files
        bash ../prob2kcalPerMol.sh ${aux}${lipid}

        # Ploting  the data
        python3 ../plot.py --suffix full --xLabel "FLC(${lipid})" --dat_files freeEnergyLandscapes/*.dat
        python3 ../plot.py --suffix 324-972 --xLabel "FLC(${lipid})" --dat_files freeEnergyLandscapes/{324,648,972}.dat
        python3 ../plot.py --suffix 1944-10100 --xLabel "FLC(${lipid})" --dat_files freeEnergyLandscapes/{1944,3888,7776,10110}.dat

        cd $CURRENT
    done
done

for lipid in dppc dipc chol
do
    for aux in meanclus meancore 
    do
        mkdir -p ${aux}${lipid}

        cd ${aux}${lipid}/

        # Removing previous data and plots
        rm -rf *.dat
        rm -rf *.pdf

        rm -rf freeEnergyLandscapes
        mkdir -p freeEnergyLandscapes

        # Generating data for the plots from the data files
        bash ../prob2kcalPerMol.sh ${aux}${lipid}

        # Ploting  the data
        python3 ../plot.py --suffix full --yRange "(0,6)" --xRange "(0,250)" --xLabel "Mean number of ${lipid} in ${lipid} clusters" --dat_files freeEnergyLandscapes/*.dat
        python3 ../plot.py --suffix 324-972 --yRange "(0,6)" --xRange "(0,250)" --xLabel "Mean number of ${lipid} in ${lipid} clusters" --dat_files freeEnergyLandscapes/{324,648,972}.dat
        python3 ../plot.py --suffix 1944-10100 --yRange "(0,6)" --xRange "(0,250)" --xLabel "Mean number of ${lipid} in ${lipid} clusters" --dat_files freeEnergyLandscapes/{1944,3888,7776,10110}.dat

        cd $CURRENT
    done
done

for lipid in dppc dipc chol
do
    for aux in stdclus stdcore
    do
        mkdir -p ${aux}${lipid}

        cd ${aux}${lipid}/

        # Removing previous data and plots
        rm -rf *.dat
        rm -rf *.pdf

        rm -rf freeEnergyLandscapes
        mkdir -p freeEnergyLandscapes

        # Generating data for the plots from the data files
        bash ../prob2kcalPerMol.sh ${aux}${lipid}

        # Ploting  the data
        python3 ../plot.py --suffix full --yRange "(0,6)" --xRange "(0,250)" --xLabel "std in number of ${lipid} in ${lipid} clusters" --dat_files freeEnergyLandscapes/*.dat
        python3 ../plot.py --suffix 324-972 --yRange "(0,6)" --xRange "(0,250)" --xLabel "std in number of ${lipid} in ${lipid} clusters" --dat_files freeEnergyLandscapes/{324,648,972}.dat
        python3 ../plot.py --suffix 1944-10100 --yRange "(0,6)" --xRange "(0,250)" --xLabel "std in number of ${lipid} in ${lipid} clusters" --dat_files freeEnergyLandscapes/{1944,3888,7776,10110}.dat

        cd $CURRENT
    done
done

for lipid in dppc dipc chol
do
    for aux in sc
    do
        mkdir -p ${aux}${lipid}

        cd ${aux}${lipid}/

        # Removing previous data and plots
        rm -rf *.dat
        rm -rf *.pdf

        rm -rf freeEnergyLandscapes
        mkdir -p freeEnergyLandscapes

        # Generating data for the plots from the data files
        bash ../prob2kcalPerMol.sh ${aux}${lipid}

        # Ploting  the data
        python3 ../plot.py --suffix full --xRange "(-1,1)" --xLabel "silhouette coefficient of ${lipid} clusters" --dat_files freeEnergyLandscapes/*.dat
        python3 ../plot.py --suffix 324-972 --xRange "(-1,1)" --xLabel "silhouette coefficient of ${lipid} clusters" --dat_files freeEnergyLandscapes/{324,648,972}.dat
        python3 ../plot.py --suffix 1944-10100 --xRange "(-1,1)" --xLabel "silhouette coefficient of ${lipid} clusters"  --dat_files freeEnergyLandscapes/{1944,3888,7776,10110}.dat

        cd $CURRENT
    done
done
