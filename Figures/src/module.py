import numpy as np
import math
from scipy import constants

def inputParser(fname):
    data = np.loadtxt(fname, dtype=float, comments="#")
    return (data, data[:, 0], data[:, 1])

def weightedMeanAndStd(values, weights):
    mean = np.average(values, weights=weights)
    var = np.average(((values-mean)*(values-mean)), weights=weights)
    return (mean, math.sqrt(var))

def kBT_to_kcal_per_mol(temperature):

    '''
    Output kBT value in corresponding kcal/mol units for given temperaturein Kelvin.
    '''

    kB  = constants.value('Boltzmann constant')
    Na  = constants.value('Avogadro constant')
    T   = temperature
    eJules = kB*T
    eKcal  = eJules/(1000*(constants.calorie))
    eKcal_per_mol  = eKcal*Na
    return (eKcal_per_mol)
    #  eJules_per_mol  = eJules*Na
    #  return (eJules_per_mol)

def sliceDataIn2sigmaRange(fname):

    data, midpoints, prob = inputParser(fname)
    mean, std = weightedMeanAndStd(midpoints, prob)

    # Slciing the data betweem mean +/- std along FLC
    sub = data[data[:, 0] >= (mean-std)]
    subset = sub[sub[:, 0] <= (mean+std)]
    return (subset)
