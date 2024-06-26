import numpy as np
import argparse

def calculate_summary(fname):
    try:
        # Read data using numpy loadtxt
        data = np.loadtxt(fname,dtype=float)

        # Extract data
        replica_means = data[:, 1]
        replica_stdevs = data[:, 2]

        # Calculate overall mean
        overall_mean = np.mean(replica_means)

        # Calculate overall standard deviation (propagation of error)
        overall_stdev = np.sqrt(np.sum(np.square(replica_stdevs)) / len(replica_stdevs))

        return (overall_mean, overall_stdev)

    except FileNotFoundError:
        print("File not found.")


if __name__ == "__main__":

    # Parse command-line
    parser = argparse.ArgumentParser()
    parser.add_argument("--outputFileName",
                        default=None,
                        help="Output file suffix")
    parser.add_argument('--size',
                        default=None,
                        help='Size of the system')
    parser.add_argument("--dat_file",
                        help="Path to the data file")
    args = parser.parse_args()

    fname = args.dat_file
    mean, std = calculate_summary(fname)

    if args.outputFileName:
        header = " ".join(sys.argv)
        hdr = header + "\n# column 0: mean\n# coulmn1 : std"
        np.savetxt(
            str(args.outputFileName) + ".dat", np.c_[mean, std], delimiter="\t", header=hdr
        )
    else:
        print(int(args.size), mean, std)
