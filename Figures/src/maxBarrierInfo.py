import sys
import numpy as np
import argparse
import module

############################# Data Input ######################################

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

###############################################################################

def maxBarrierInfo(fname, temp, Slice=True):
    '''
    Returns FLC with max peak  and peak Height

    by default the full data is sliced betweeen +/- std of <FLC>
    fname should contain the probability info not the delG
    temp in Kelvin
    '''

    if Slice:
        data = module.sliceDataIn2sigmaRange(fname)
    else:
        data, midpoints, prob = module.inputParser(fname)

    # Finding the array with max delG
    minArray = data[data[:, 1] == np.min(data[:,1])]

    maxBarrierFLC = minArray[:, 0]
    #  minProb = minArray[:, 1]
    kBT_factor = module.kBT_to_kcal_per_mol(float(args.temp))
    # Free energy corresponding to min prob
    maxBarrierHeight = kBT_factor*minArray[:, 2]

    return (maxBarrierFLC, maxBarrierHeight)

if __name__ == "__main__":
    fname = args.dat_file
    temp = args.temp
    barrierFLC, barrierHeight = maxBarrierInfo(fname, temp)
    print(int(args.size), float(barrierFLC), float(barrierHeight))
