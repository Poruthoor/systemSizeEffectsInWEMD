#!/usr/bin/env bash

AuxHeaders00=("meanclusdppc_stdclusdppc"
              "meanclusdipc_stdclusdipc"
              "meancluschol_stdcluschol"
              "clusbydppc_meanclusdppc"
              "clusbydipc_meanclusdipc"
              "clusbychol_meancluschol"
              "clusbydppc_clucountdppc"
              "clusbydipc_clucountdipc"
              "clusbychol_clucountchol"
              "clucountdppc_meanclusdppc"
              "clucountdipc_meanclusdipc"
              "clucountchol_meancluschol"
              )

for aux in "${AuxHeaders00[@]}"
do
    mkdir -p ${aux}
    for size in 324 648 972 1944 3888 7776 10110 # 7776 10110
    do
        cp -prf ../../DIPC_DPPC_${size}_lipid_systems/WE_runs/Analysis/data/multi_west_aux/${aux}.pdf ${aux}/${size}.pdf
    done
done

