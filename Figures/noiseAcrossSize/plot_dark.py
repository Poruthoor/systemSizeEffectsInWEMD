import sys
import numpy as np
import argparse
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from ast import literal_eval

############################# Data Input ######################################

# Parse command-line
parser = argparse.ArgumentParser()
parser.add_argument('--suffix',
                    default="foo",
                    help='File name suffix')
parser.add_argument('--xRange',
                    default="(0, 1)",
                    help='xRange as a tuple')
parser.add_argument('--yRange',
                    default="(0, 4)",
                    help='yRange as a tuple')
parser.add_argument('--xLabel',
                    default="Fraction of Lipids in Clusters (FLC)",
                    help='X axis label')
args = parser.parse_args()

###############################################################################

# Evaluating xRange
try:
    tupX = literal_eval(args.xRange)
except (SyntaxError, ValueError):
    print("%s -> Invalid tuple format given" % args.xRange)

# Evaluating yRange
try:
    tupY = literal_eval(args.yRange)
except (SyntaxError, ValueError):
    print("%s -> Invalid tuple format given" % args.yRange)

# #  ############################# Plot parameters #################################

#  plt.rcParams.update({'font.size': 14})
plt.style.use('dark_background')

SMALL_SIZE = 18
MEDIUM_SIZE = 14
BIGGER_SIZE = 18

plt.rc('font', size=MEDIUM_SIZE)         # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)    # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)   # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

#  ################################ Ploting #######################################

size = [324, 648, 972, 1944, 3888, 7776, 10110]

# Create a figure and a set of subplots
fig, axs = plt.subplots(1, 7, figsize=(18, 5), sharex=True, sharey=True)

# Plot bar plots in each subplot
for i in range(len(axs)):
    felData = np.loadtxt("../freeEnergyLandscapesFromWE/freeEnergyLandscapes/" + str(size[i])
                         + ".dat", dtype=float, comments="#")
    peakData = np.loadtxt("peakInfo/" + str(size[i]) + ".dat", dtype=float, comments="#")
    rollingData = np.loadtxt("rollingStd/" + str(size[i]) + ".dat", dtype=float, comments="#")
    avgVarData = np.loadtxt("avgVarFLC/" + str(size[i]) + ".dat", dtype=float, comments="#")

    sigmaMax = np.max(rollingData[:, 1])
    twoSigma = 2*sigmaMax

    axs[i].plot(felData[:, 0], felData[:, 1], '-', linewidth=4, alpha=0.8,
                label="Free energy curve")
    axs[i].plot(rollingData[:, 0], rollingData[:, 1], '-', linewidth=4,
                label=r'$Rolling\ \sigma$')
    #  axs[i].scatter(peakData[:, 0], peakData[:, 1], c='black')
    axs[i].axhspan(0, twoSigma, alpha=0.3, color='orange', label=r'$2\sigma (\Delta G)$')
    axs[i].axvline([avgVarData[0]], ls='--', color="green", linewidth=4,
                   label="Mean FLC")
    axs[i].axvspan(avgVarData[0]-avgVarData[1], avgVarData[0]+avgVarData[1],
                   alpha=0.3, color='seagreen', label=r'$FLC\pm\sigma (FLC)$')
    axs[i].set_title(str(size[i]))
    axs[i].set_ylim([0, 2])
    axs[i].set_xlim([0.2, 0.8])


fig.add_subplot(111, frameon=False)
# hide tick and tick label of the big axis
plt.tick_params(labelcolor='none', which='both', top=False, bottom=False,
left=False, right=False)
ylabel = r'$\Delta G\ (kcal/mol)$'
plt.xlabel(str(args.xLabel),labelpad=20)
plt.ylabel(ylabel,labelpad=20)

fig.tight_layout()
box = axs[i].get_position()
axs[i].legend(loc='upper center', ncol=5, handlelength=1,
              bbox_to_anchor=(-3.55, -0.30),
             frameon=False)


plt.savefig(args.suffix + ".pdf")
