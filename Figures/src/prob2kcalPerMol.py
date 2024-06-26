import argparse
import module
import sys
import numpy as np

############################# Data Input ######################################

# Parse command-line
parser = argparse.ArgumentParser()
parser.add_argument('--suffix',
                    help=' Output file suffix')
parser.add_argument('--temp',
                    default=323,
                    help='Temperature in Kelvin')
parser.add_argument('--dat_file',
                    help='Input pcoord vs probability file')
args = parser.parse_args()

###############################################################################

if __name__ == "__main__":

    fname = args.dat_file
    temp = args.temp

    kBT_factor = module.kBT_to_kcal_per_mol(temp)
    data = module.inputParser(fname)[0]
    midpoints = data[:,0]
    enehists = data[:,2]
    plothist = kBT_factor*enehists

    header = " ".join(sys.argv)
    hdr = header +  "\n# column 0: midpoint of bin\n# column 1: delG of the bin in kcal per mol"
    np.savetxt(str(args.suffix) + ".dat", np.c_[midpoints, plothist], delimiter="\t",
               header=hdr)
