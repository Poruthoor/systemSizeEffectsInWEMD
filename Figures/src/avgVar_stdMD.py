import sys
import numpy as np
import argparse
import module

def avgVarFLC_stdMD(fname):

    data = np.loadtxt(fname, dtype=float, comments="#")

    # Only selecting frames 19 to 39 (2 us to 4 us)
    data = data[19:39]
    # prob = np.ones(np.shape(data))
    mean, std = module.weightedMeanAndStd(values=data, weights=None)

    return (mean, std)


if __name__ == "__main__":

    # Parse command-line
    parser = argparse.ArgumentParser()
    parser.add_argument("--replicaNum",
                        type=int,
                        help="Replica number of the system")
    parser.add_argument("--outputFileName",
                        default=None,
                        help="Output file suffix")
    parser.add_argument("--dat_file",
                        help="Input pcoord vs probability file")
    args = parser.parse_args()

    fname = args.dat_file
    mean, std = avgVarFLC_stdMD(fname)
    if args.outputFileName:
        header = " ".join(sys.argv)
        hdr = header + "\n# column 0: mean\n# coulmn1 : std"
        np.savetxt(
            str(args.outputFileName) + ".dat", np.c_[mean, std], delimiter="\t", header=hdr
        )
    else:
        print(args.replicaNum, mean, std)
