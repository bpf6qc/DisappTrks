#!/usr/bin/env python

# Local options file to be used with makeDataCards.py
# Usage:
# > makeDatacards.py -l amsbLimitConfig.py -c test
#
# Copied from https://raw.github.com/DisplacedSUSY/DisplacedSUSY/master/LimitsCalculation/test/sampleLimitConfig.py

from DisappTrks.SignalMC.signalCrossSecs import *
from DisappTrks.StandardAnalysis.utilities import *
from DisappTrks.StandardAnalysis.IntegratedLuminosities import *
from amsbLimitConfigBkgds_2016BC import *    # Produced with ../scripts/makeANTables.py

##################################
### Event Selection Parameters ###
##################################

#name of histogram to integrate to get yields
integrateHistogramName = "metPt"

#########################
### Signal Parameters ###
#########################

# a separate datacard will be produced with each value of MASS,TAU
# named "datacard_AMSB_mGravMASSK_TAUns.txt"

samplesByGravitinoMass = False

#NOTE: These are the chargino masses in GeV
masses = ['100', '200', '300', '400', '500', '600', '700']

#chargino tau values in cm
lifetimes = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
             '20', '30', '40', '50', '60', '70', '80', '90', '100',
             '200', '300', '400', '500', '600', '700', '800', '900', '1000',
             '2000', '3000', '4000', '5000', '6000', '7000', '8000', '9000', '10000']

lumi = lumi["MET_2016BC"]
signalScaleFactor = 1.0

#condor directory in which to find signal root files
signal_condor_dir = dir["Andrew"] + '/2016_ICHEP/disappearingTracks_signal_weightedToBC/'

signal_suffix = '80X'

#name of event selection from which to take signal yields
signal_channel = 'DisTrkSelectionPlotter/Met Plots'

#######################
### Data Parameters ###
#######################

#this just sets the observed number of events equal to the total background expectation
run_blind_limits = False

data_dataset = "MET_2016_v3"

#condor directory in which to find data root file
data_condor_dir = dir["Andrew"] + '/2016_ICHEP/disappearingTracks/'

#name of event selection from which to take observed events
data_channel = 'DisTrkSelectionPlotter/Met Plots'

#############################
### Systematic Uncertainties ###
#############################

external_systematic_uncertainties = [
    # Use order of AN
    "isr_2016",
    "jec_2016",
    "jer_2016",
    "metVaryElectronEn_2016",
    "metVaryJetEn_2016",
    "metVaryJetRes_2016",
    "metVaryPhotonEn_2016",
    "metVaryTauEn_2016",
    "metVaryUnclusteredEn_2016",
    "pileup_2016BC",
    "trigger_metLegWeightData_2016BC",
    "trigger_metLegWeightMC_2016BC",
    "trigger_trackLegWeightData_2016BC",
    "trigger_trackLegWeightMC_2016BC",
]

#uncertainties on signal only (we can alter this if we need to)
# For now, use the largest value of the uncertainty range from Run 1
signal_systematic_uncertainties = {
    'lumi' :  {
        'value' : '1.062',
    },
    'NMissOut' : {
        'value' : '1.07',
    },
    'trkReco' :  {
        'value' : '1.017',
    },
    'Nmissin' :  {
        'value' : '1.028',
    },
    'Nmissmid' :  {
        'value' : '1.018',
    },
    'Ecalo' : {
        'value' : '1.00626555065492',
    },
}
