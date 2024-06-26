import sys
import numpy as np
import argparse
import module
from pathlib import Path

############################# Data Input ######################################

# Parse command-line
parser = argparse.ArgumentParser()
parser.add_argument('--size',
                    help='Size of the system')
parser.add_argument('--outputFile',
                    default=False,
                    help='Output file is created instead of stdOut')
parser.add_argument('--dat_file',
                    help='Input pcoord vs probability file')
args = parser.parse_args()

###############################################################################

def avgVarFLC(fname):

    data, midpoints, prob = module.inputParser(args.dat_file)

    mean, std = module.weightedMeanAndStd(midpoints, prob)

    return(mean, std)

if __name__ == "__main__":
    fname = args.dat_file
    mean, std = avgVarFLC(fname)
    if args.outputFile :
        header = " ".join(sys.argv)
        hdr = header +  "\n# column 0: mean\n# coulmn1 : std"
        np.savetxt(str(args.size) + ".dat", np.c_[mean, std], delimiter="\t",
                   header=hdr)
    else:
        stem = Path(args.size).stem
        print(int(stem), mean, std)
