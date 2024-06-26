#!/usr/bin/env bash

rm -rf *.pdf

python3 plot.py --suffix fractionOfLipidsInClusters --cv FLC

# for aux in coreby 
# do
    # for lipid in dppc dipc chol
    # do
        # python3 plot.py --suffix ${aux}_${lipid} --cv ${aux}_${lipid} --yLabel "Fraction of ${lipid} in ${lipid} cores"
    # done
# done

for aux in clusby 
do
    for lipid in dppc dipc chol
    do
        python3 plot.py --suffix fractionOF${lipid}IN${lipid}Clusters --cv ${aux}_${lipid} --yLabel "Fraction of ${lipid} in ${lipid} clusters"
    done
done

for aux in clustcount
do
    for lipid in dppc dipc chol
    do
        python3 plot.py --suffix ${lipid}ClusterCount --cv ${aux}_${lipid} --yRange "(0, 50)" --yLabel "Number of ${lipid} cluster"
    done
done

for aux in meanclus
do
    for lipid in dppc dipc chol
    do
        python3 plot.py --suffix mean${lipid}IN${lipid}Clusters --cv ${aux}_${lipid} --yRange "(0, 250)" --yLabel "Mean ${lipid} in ${lipid} clusters"
        python3 plot_norm.py --suffix mean${lipid}IN${lipid}Clusters  --cv ${aux}_${lipid} --lipid ${lipid} --yRange "(0, 0.5)" --yLabel "Mean ${lipid} in ${lipid} clusters (In fraction of total ${lipid})"
    done
done

# for aux in meancore
# do
    # for lipid in dppc dipc chol
    # do
        # python3 plot.py --suffix ${aux}_${lipid} --cv ${aux}_${lipid} --yRange "(0, 250)" --yLabel "Mean ${lipid} in ${lipid} cores"
        # python3 plot_norm.py --suffix ${aux}_${lipid} --cv ${aux}_${lipid} --lipid ${lipid} --yRange "(0, 0.5)" --yLabel "Mean ${lipid} in ${lipid} cores (In fraction of total ${lipid})"
    # done
# done

for aux in stdclus
do
    for lipid in dppc dipc chol
    do
        python3 plot.py --suffix stdOF${lipid}IN${lipid}Clusters --cv ${aux}_${lipid} --yRange "(0, 250)" --yLabel "std dev of  ${lipid} in ${lipid} clusters" 
        python3 plot_norm.py --suffix stdOF${lipid}IN${lipid}Clusters --cv ${aux}_${lipid} --lipid ${lipid} --yRange "(0, 0.5)" --yLabel "std dev of ${lipid} in ${lipid} clusters (In fraction of total ${lipid})"
    done
done

# for aux in stdcore
# do
    # for lipid in dppc dipc chol
    # do
        # python3 plot.py --suffix ${aux}_${lipid} --cv ${aux}_${lipid} --yRange "(0, 250)" --yLabel "std dev of  ${lipid} in ${lipid} cores" 
        # python3 plot_norm.py --suffix ${aux}_${lipid} --cv ${aux}_${lipid} --lipid ${lipid} --yRange "(0, 0.5)" --yLabel "std dev of ${lipid} in ${lipid} cores (In fraction of total ${lipid})"
    # done
# done

# for aux in sc
# do
    # for lipid in dppc dipc chol
    # do
        # python3 plot.py --suffix ${aux}_${lipid} --cv ${aux}_${lipid} --yRange "(-1, 1)" --yLabel "silhouette coefficient"
    # done
# done
