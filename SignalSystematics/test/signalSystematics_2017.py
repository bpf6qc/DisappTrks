#!/usr/bin/env python

import math
from DisappTrks.SignalSystematics.signalSystematics import *
from DisappTrks.StandardAnalysis.plotUtilities import *
from ROOT import TFile
import os
import re
import sys

dirs = getUser()
masses = [100, 200, 300, 400, 500, 600, 700, 800, 900]
lifetimes = [10, 100, 1000, 10000]
allTheLifetimes = ['0p2', '0p3', '0p4', '0p5', '0p6', '0p7', '0p8', '0p9', '1',
                   '2', '3', '4', '5', '6', '7', '8', '9', '10',
                   '20', '30', '40', '50', '60', '70', '80', '90', '100',
                   '200', '300', '400', '500', '600', '700', '800', '900', '1000',
                   '2000', '3000', '4000', '5000', '6000', '7000', '8000', '9000', '10000']
suffix = "94X"
extraSamples = getExtraSamples (suffix)

systematic = "all"
if len (sys.argv) > 1:
    systematic = sys.argv[1]
systematic = systematic.upper ()

nlayers = "NLayers4"
if len(sys.argv) > 2:
    nlayers = sys.argv[2]

if systematic == "PILEUP" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating pileup systematic (2017) " + nlayers
    print "--------------------------------------------------------------------------------"

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__pileup_2017_" + nlayers + ".txt", "w")

    pileupSystematic = PileupSystematic (masses, allTheLifetimes)
    pileupSystematic.addFout (fout)
    #pileupSystematic.addExtraSamples (extraSamples)
    pileupSystematic.addChannel  ("PileupCentral",  "disTrkSelectionSmearedJets" + nlayers,  suffix,  dirs['Brian']+"2017/signalAcceptance_full_v7")

    pileupSystematic.printSystematic ()

    print "********************************************************************************"

    fout.close ()


if systematic == "MET" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating met systematics (2017) " + nlayers
    print "--------------------------------------------------------------------------------"

    metVaryTypes = [
        'JetRes',
        'JetEn',
        'ElectronEn',
        'TauEn',
        'UnclusteredEn',
        'PhotonEn',
    ]

    metSystematic = MetSystematic (masses, allTheLifetimes)
    #metSystematic.addExtraSamples (extraSamples)
    metSystematic.addChannel ("central", "DisTrkNoMetSmearedJets" + nlayers, suffix, dirs['Brian']+"2017/signalAcceptance_full_v7_metSyst")
    metSystematic.addMetTypes (metVaryTypes)
    metSystematic.setMetCut (120.0)
    metSystematic.setFoutNames (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__metVary", "2017_" + nlayers + ".txt")
    metSystematic.printSystematic ()

    print "********************************************************************************"

    print "\n\n"

if systematic == "JEC" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating JEC systematic (2017) " + nlayers
    print "--------------------------------------------------------------------------------"

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__jec_2017_" + nlayers + ".txt", "w")

    jecSystematic = YieldSystematic (masses, allTheLifetimes)
    jecSystematic.addFout (fout)
    #jecSystematic.addExtraSamples (extraSamples)
    jecSystematic.addChannel  ("central",  "disTrkSelectionSmearedJets" + nlayers ,       suffix,  dirs['Brian']+"2017/signalAcceptance_full_v7")
    jecSystematic.addChannel  ("down",     "disTrkSelectionSmearedJetsJECUp" + nlayers,   suffix,  dirs['Brian']+"2017/signalAcceptance_full_v7_jecSyst")
    jecSystematic.addChannel  ("up",       "disTrkSelectionSmearedJetsJECDown" + nlayers, suffix,  dirs['Brian']+"2017/signalAcceptance_full_v7_jecSyst")
    jecSystematic.printSystematic ()

    print "********************************************************************************"

    fout.close ()

    print "\n\n"

if systematic == "JER" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating JER systematic (2017) " + nlayers
    print "--------------------------------------------------------------------------------"

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__jer_2017_" + nlayers + ".txt", "w")

    jerSystematic = YieldSystematic (masses, allTheLifetimes)
    jerSystematic.addFout (fout)
    #jerSystematic.addExtraSamples (extraSamples)
    jerSystematic.addChannel  ("central",  "disTrkSelectionSmearedJets" + nlayers ,       suffix,  dirs['Brian']+"2017/signalAcceptance_full_v7")
    jerSystematic.addChannel  ("down",     "disTrkSelectionSmearedJetsUp" + nlayers,   suffix,  dirs['Brian']+"2017/signalAcceptance_full_v7_jerSyst")
    jerSystematic.addChannel  ("up",       "disTrkSelectionSmearedJetsDown" + nlayers, suffix,  dirs['Brian']+"2017/signalAcceptance_full_v7_jerSyst")
    jerSystematic.printSystematic ()

    print "********************************************************************************"

    fout.close ()

    print "\n\n"

if systematic == "ISR" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating ISR systematic (2017) " + nlayers
    print "--------------------------------------------------------------------------------"

    fout = open(os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__isr_2017_" + nlayers + ".txt", "w")

    isrSystematic = YieldSystematic (masses, allTheLifetimes)
    isrSystematic.setIsWeightFluctuation (True)
    isrSystematic.addFout (fout)
    #isrSystematic.addExtraSamples (extraSamples)
    isrSystematic.addChannel ("central", "disTrkSelectionSmearedJets" + nlayers, suffix, dirs['Brian']+"2017l/signalAcceptance_full_v7")
    isrSystematic.printSystematic ()

    print "********************************************************************************"

    fout.close ()

    print "\n\n"


if systematic == "TRIGGER" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating trigger efficiency systematics (2017) " + nlayers
    print "--------------------------------------------------------------------------------"

    triggerFluctuations = [
        'grandOrWeightData',
        'grandOrWeightMC',
    ]

    triggerSystematic = TriggerSystematic (masses, allTheLifetimes)
    #triggerSystematic.addExtraSamples (extraSamples)
    triggerSystematic.addChannel ("central", "disTrkSelectionSmearedJets" + nlayers, suffix, dirs['Brian']+"2017/signalAcceptance_full_v7")
    triggerSystematic.addChannel ("down",    "disTrkSelectionSmearedJets" + nlayers, suffix, dirs['Brian']+"2017/signalAcceptance_full_v7")
    triggerSystematic.addChannel ("up",      "disTrkSelectionSmearedJets" + nlayers, suffix, dirs['Brian']+"2017/signalAcceptance_full_v7")
    triggerSystematic.addTriggerFluctuations (triggerFluctuations)
    triggerSystematic.setFoutNames (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__trigger_", "2017_" + nlayers + ".txt")
    triggerSystematic.printSystematic ()

    print "********************************************************************************\n\n"

    print "\n\n"


if systematic == "ECALO" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating ECalo systematic (2017)"
    print "--------------------------------------------------------------------------------"

    ecaloSystematic = ECaloSystematic ()
    ecaloSystematic.addChannel  ("Data",  "ZtoMuMuDisTrkNLayers4NoECaloCut",  "SingleMu_2017",  dirs['Andrew']+"2017/ecaloSystematic_atMost4Layers")
    ecaloSystematic.addChannel  ("MC",    "ZtoMuMuDisTrkNLayers4NoECaloCut",  "DYJetsToLL_50",       dirs['Andrew']+"2017/ecaloSystematic_atMost4Layers")

    print "********************************************************************************"

    ecaloSystematic.printSystematic ()

    print "********************************************************************************"

    print "\n\n"

if systematic == "HITS" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating hits systematic (2017)"
    print "--------------------------------------------------------------------------------"

    hitsSystematic_2017 = HitsSystematic ()
    hitsSystematic_2017.addChannel  ("Data",  "HitsSystematicsCtrlSelection",  "MET_2017",    dirs['Brian']+"2017/fromLPC/missingHitsCorrection_bkgdMC_scaledRight")
    hitsSystematic_2017.addChannel  ("MC",    "HitsSystematicsCtrlSelection",  "AllMC_scaled",  dirs['Brian']+"2017/fromLPC/missingHitsCorrection_bkgdMC")
    hitsSystematic_2017.addIntegrateHistogram ("Track Plots/trackNHitsMissingMiddleVsInner")
    print "--------------------------------------------------------------------------------"
    print "before correction to missing middle hits"
    hitsSystematic_2017.printSystematic ()
    hitsSystematic_2017.addIntegrateHistogram ("Track Plots/trackNHitsMissingMiddleCorrectedVsInner")
    print "--------------------------------------------------------------------------------"
    print "after correction to missing middle hits"
    hitsSystematic_2017.printSystematic ()

    print "********************************************************************************"

    print "\n\n"

if systematic == "MISSING_OUTER_HITS" or systematic == "ALL":

    print "********************************************************************************"
    print "evaluating missing outer hits systematic (2017)"
    print "--------------------------------------------------------------------------------"

    fout = open (os.environ["CMSSW_BASE"] + "/src/DisappTrks/SignalSystematics/data/systematic_values__nMissOut_2016BC.txt", "w")
    foutForPlot = TFile.Open ("nMissOutSystematic_2016BC.root", "recreate")

    missingOuterHitsSystematic_2016BC = MissingOuterHitsSystematic (masses, allTheLifetimes)
    #missingOuterHitsSystematic_2016BC = MissingOuterHitsSystematic (masses, allTheLifetimes)
    missingOuterHitsSystematic_2016BC.addFout (fout)
    missingOuterHitsSystematic_2016BC.addFoutForPlot (foutForPlot)
    missingOuterHitsSystematic_2016BC.addSignalSuffix ("_" + suffix)
    missingOuterHitsSystematic_2016BC.addIntegrateHistogram ("Track Plots/trackNHitsMissingOuterCorrected")
    missingOuterHitsSystematic_2016BC.addChannel  ("Data",    "MuonCtrlSelection",  "MET_2016BC",        dirs['Andrew']+"2016/hipAndTOBDrop")
    missingOuterHitsSystematic_2016BC.addChannel  ("MC",      "MuonCtrlSelection",  "Background_noQCD",  dirs['Andrew']+"2016/hitsSystematics_BC_new")
    missingOuterHitsSystematic_2016BC.addChannel  ("Signal",  "DisTrkNoNMissOut",   "",                  dirs['Andrew']+"2016_final_prompt/disTrkSelection_noNMissOutCut_BC")
    missingOuterHitsSystematic_2016BC.printSystematic ()

    print "********************************************************************************"

    fout.close ()
    foutForPlot.Close ()

    print "\n\n"
