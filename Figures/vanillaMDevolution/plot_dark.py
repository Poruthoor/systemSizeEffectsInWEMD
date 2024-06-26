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
parser.add_argument('--cv',
                    default="FLC",
                    help='collective variable name : Should match with data/vanillaMD subfolders')
parser.add_argument('--xRange',
                    default="(0, 4)",
                    help='xRange as a tuple')
parser.add_argument('--yRange',
                    default="(0, 1)",
                    help='yRange as a tuple')
parser.add_argument('--yLabel',
                    default="Fraction of Lipids in Clusters (FLC)",
                    help='y Label')
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
MEDIUM_SIZE = 12
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
temp = [323, 423]
replica = [1,2,3,4]

# Create a figure and a set of subplots
fig, axs = plt.subplots(1, len(size), figsize=(18, 5), sharex=True, sharey=True)

# Plot bar plots in each subplot
for i in range(len(axs)):
    for j in range(len(temp)):
        for k in range(len(replica)):
            data = np.loadtxt("../data/vanillaMD/" + str(args.cv) + "/" + str(size[i])
                         + "/" + str(temp[j]) + "/" + str(replica[k]) + ".dat", dtype=float, comments="#")
            xdata =  np.arange(0, len(data), 1)
            axs[i].plot(xdata*.1, data, '-', linewidth=4, alpha=0.85,
                        label=str(temp[j]) + " - " + str(replica[k]))

    axs[i].set_title(str(size[i]))
    axs[i].set_ylim(tupY)
    axs[i].set_xlim(tupX)


fig.add_subplot(111, frameon=False)
# hide tick and tick label of the big axis
plt.tick_params(labelcolor='none', which='both', top=False, bottom=False,
left=False, right=False)
plt.xlabel(r'time ($\mu s$)') #,labelpad=20)
plt.ylabel(args.yLabel)

fig.tight_layout()

box = axs[i].get_position()
axs[i].legend(loc='upper center', ncol=8, handlelength=1, bbox_to_anchor=(-3.05,
                                                                          -0.2),
             frameon=False)
#  axs[i].legend(loc='upper center', , ncol=4,
              #  handlelength=1)
#  plt.legend(handlelength=4)


plt.savefig(args.suffix + ".pdf")
