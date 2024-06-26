import sys
import numpy as np
import argparse
import module
import maxBarrierInfo as mbi


def deldelG(fname, temp, cutoff):

    kBT_factor = module.kBT_to_kcal_per_mol(temp)
    data, midpoints, prob = module.inputParser(fname)

    midShape = np.shape(midpoints)
    probRatio = np.zeros(midShape)
    normhist = prob/np.sum(prob)

    sortedHist = 0

    for i in range(midShape[0]):
        if (float(cutoff) <= midpoints[i]):
            sortedHist += normhist[i]

    # Final state = Separated , Initial State = Mixed
    probRatio =  sortedHist/(1-sortedHist)
    loghist = -(np.log(probRatio))

    deldelG = kBT_factor*loghist
    return (deldelG)

if __name__ == "__main__":

# Parse command-line
    parser = argparse.ArgumentParser()
    parser.add_argument('--size',
                        help='Size of the system')
    parser.add_argument('--temp',
                        default=323,
                        help='Temperature in Kelvin')
    parser.add_argument('--dat_file',
                        help='Input pcoord vs probability file')
    args = parser.parse_args()

    fname = args.dat_file
    temp = args.temp
    barrierFLC, barrierHeight = mbi.maxBarrierInfo(fname, temp)
    ddG = deldelG(fname, temp, barrierFLC)
    print(int(args.size), float(ddG))
