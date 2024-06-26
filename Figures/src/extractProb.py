import argparse
import module
import sys
import numpy as np

############################# Data Input ######################################

# Parse command-line
parser = argparse.ArgumentParser()
parser.add_argument('--suffix',
                    help=' Output file suffix')
parser.add_argument('--dat_file',
                    help='Input pcoord vs probability file')
args = parser.parse_args()

###############################################################################

if __name__ == "__main__":

    fname = args.dat_file

    data = module.inputParser(fname)[0]
    midpoints = data[:,0]
    prob = data[:,1]
    totalProb = np.sum(prob)
    normProb = prob/totalProb

    header = " ".join(sys.argv)
    hdr = header +  "\n# column 0: midpoint of bin\n# column 1: Normalized probability"
    np.savetxt(str(args.suffix) + ".dat", np.c_[midpoints, normProb], delimiter="\t",
               header=hdr)
