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

def rollingStd(data, window_size):
    rolling_std = np.zeros_like(data)
    for i in range(len(data) - window_size + 1):
        rolling_std[i + window_size - 1] = np.std(data[i:i + window_size])
    return (rolling_std)

def rollingStdCentered(data, window_size):
    std_values = np.zeros_like(data, dtype=float)
    half_window = window_size // 2

    for i in range(len(data)):
        start_idx = max(0, i - half_window)
        end_idx = min(len(data), i + half_window + 1)
        std_values[i]  = np.std(data[start_idx:end_idx])
    return std_values

def movingStd(fname, temp, windowSize=5, Slice=True):
    '''
    '''

    if Slice:
        data = module.sliceDataIn2sigmaRange(fname)
    else:
        data, midpoints, prob = module.inputParser(fname)

    kBT_factor = module.kBT_to_kcal_per_mol(float(args.temp))
    delGsignal= kBT_factor*data[:, 2]

    #  # Only using 50% of bins in the data at max
    #  maxWindows = int(np.round(len(delGsignal)*0.5))

    #  windowSizeArray = np.zeros((maxWindows, len(delGsignal)))
    #  stdArray = np.zeros((maxWindows, len(delGsignal)))

    #  # Calculate the moving standard deviation over mulitple window sizes
    #  for i in range(maxWindows):
        #  windowSizeArray[i] = i+1
        #  stdArray[i] = rollingStd(delGsignal, i+1)

    #  return (windowSizeArray, stdArray)

    return(data[:, 0], rollingStdCentered(delGsignal, windowSize))

if __name__ == "__main__":
    fname = args.dat_file
    temp = args.temp
    midpoints, rollingStd = movingStd(fname, temp)

    header = " ".join(sys.argv)
    hdr = header +  "\n# column 0: midpoints\n# coulmn1 : std"
    np.savetxt(str(args.size) + ".dat", np.c_[midpoints, rollingStd], delimiter="\t",
               header=hdr)
