import sys
import numpy as np
import argparse
import module
from scipy.signal import find_peaks, peak_prominences

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

def peakInfo(fname, temp, Slice=True):
    '''
    '''

    if Slice:
        data = module.sliceDataIn2sigmaRange(fname)
    else:
        data, midpoints, prob = module.inputParser(fname)

    kBT_factor = module.kBT_to_kcal_per_mol(float(args.temp))
    delGsignal= kBT_factor*data[:, 2]

    peaks, _ = find_peaks(delGsignal)

    peakFLCs = data[:, 0][peaks]

    peakValue = delGsignal[peaks]

    prominences = peak_prominences(delGsignal, peaks)[0]

    return (peakFLCs, peakValue, prominences)

if __name__ == "__main__":
    fname = args.dat_file
    temp = args.temp
    peakFLCs, peakValue, prominences = peakInfo(fname, temp)

    header = " ".join(sys.argv)
    hdr = header +  "\n# column 0: peaks\n# coulmn1 : peak Height\n# column 2: peak prominences"
    np.savetxt(str(args.size) + ".dat", np.c_[peakFLCs, peakValue, prominences], delimiter="\t",
               header=hdr)
