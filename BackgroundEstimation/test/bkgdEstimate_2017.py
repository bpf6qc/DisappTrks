#!/usr/bin/env python

import math, os, sys
from DisappTrks.BackgroundEstimation.bkgdEstimate import LeptonBkgdEstimate
from DisappTrks.BackgroundEstimation.fakeEstimateTest import FakeTrackBkgdEstimate
from DisappTrks.StandardAnalysis.plotUtilities import *
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *
from ROOT import gROOT, TCanvas, TFile, TGraphErrors

gROOT.SetBatch () # I am Groot.

dirs = getUser()
canvas = TCanvas("c1", "c1",800,800)
setCanvasStyle(canvas)

background = "all"
if len (sys.argv) > 1:
    background = sys.argv[1]
background = background.upper ()

# '' will gives you Dataset_2017.root for the whole year
#runPeriods = ['B', 'C', 'D', 'E', 'F', 'G', 'H']
runPeriods = ['']

nEstFake = []
nEstElectron = []
nEstMuon = []
nEstTau = []

nEstFakeVsNHits = {}
nEstFakeVsNHitsZtoMuMu = {}

stdout = sys.stdout
nullout = open ("/dev/null", "w")

for runPeriod in runPeriods:

    nEstFakeVsNHits[runPeriod] = {}
    nEstFakeVsNHitsZtoMuMu[runPeriod] = {}

    if background == "FAKE" or background == "ALL":

        for minHits in range (3, 8):

            if minHits != 7:
                sys.stdout = nullout
            else:
                sys.stdout = stdout

            print "********************************************************************************"
            print "performing fake track background estimate in search region (2017", runPeriod, ")"
            print "--------------------------------------------------------------------------------"

            fout = TFile.Open ("fakeTrackBkgdEstimate_2017" + runPeriod + ".root", "recreate")

            fakeTrackBkgdEstimate = FakeTrackBkgdEstimate ()
            fakeTrackBkgdEstimate.addTFile (fout)
            fakeTrackBkgdEstimate.addTCanvas (canvas)
            fakeTrackBkgdEstimate.addLuminosityInInvPb (lumi["MET_2017" + runPeriod])
            fakeTrackBkgdEstimate.addMinHits (minHits)
            fakeTrackBkgdEstimate.addChannel  ("Basic3hits",            "DisTrkSelectionNoD0CutNHits3",        "MET_2017"  +  runPeriod,  dirs['fixme']+"2017_final_prompt/fakeTrackSystematic_d0Sideband_new_v2")
            fakeTrackBkgdEstimate.addChannel  ("DisTrkInvertD0",        "DisTrkSelectionSidebandD0Cut",        "MET_2017"  +  runPeriod,  dirs['fixme']+"2017_final_prompt/fakeTrackSystematic_d0Sideband_new_v2")
            fakeTrackBkgdEstimate.addChannel  ("DisTrkInvertD0NHits3",  "DisTrkSelectionSidebandD0CutNHits3",  "MET_2017"  +  runPeriod,  dirs['fixme']+"2017_final_prompt/fakeTrackSystematic_d0Sideband_new_v2")
            fakeTrackBkgdEstimate.addChannel  ("DisTrkInvertD0NHits4",  "DisTrkSelectionSidebandD0CutNHits4",  "MET_2017"  +  runPeriod,  dirs['fixme']+"2017_final_prompt/fakeTrackSystematic_d0Sideband_new_v2")
            fakeTrackBkgdEstimate.addChannel  ("DisTrkInvertD0NHits5",  "DisTrkSelectionSidebandD0CutNHits5",  "MET_2017"  +  runPeriod,  dirs['fixme']+"2017_final_prompt/fakeTrackSystematic_d0Sideband_new_v2")
            fakeTrackBkgdEstimate.addChannel  ("DisTrkInvertD0NHits6",  "DisTrkSelectionSidebandD0CutNHits6",  "MET_2017"  +  runPeriod,  dirs['fixme']+"2017_final_prompt/fakeTrackSystematic_d0Sideband_new_v2")
            fakeTrackBkgdEstimate.addChannel  ("Basic",                 "BasicSelection",                      "MET_2017"  +  runPeriod,  dirs['Brian']+"2017/fromRutgers/basicSelection")

            print "********************************************************************************"

            nEst = fakeTrackBkgdEstimate.printNest ()
            nEstFakeVsNHits[runPeriod][minHits] = nEst

            print "********************************************************************************"

            fout.Close ()

            print "\n\n"

            print "********************************************************************************"
            print "performing fake track background estimate in ZtoMuMu (2017", runPeriod, ")"
            print "--------------------------------------------------------------------------------"

            fout = TFile.Open ("zToMuMuEstimate_2017" + runPeriod + ".root", "recreate")

            zToMuMuEstimate = FakeTrackBkgdEstimate ()
            zToMuMuEstimate.addTFile (fout)
            zToMuMuEstimate.addTCanvas (canvas)
            zToMuMuEstimate.addLuminosityInInvPb (lumi["SingleMuon_2017" + runPeriod])
            zToMuMuEstimate.addMinHits (minHits)
            zToMuMuEstimate.addChannel  ("Basic3hits",            "ZtoMuMuDisTrkNoD0CutNHits3",        "SingleMu_2017"  +  runPeriod,  dirs['fixme']+"2017_final_prompt/fakeTrackBackground_d0Sideband_new")
            zToMuMuEstimate.addChannel  ("DisTrkInvertD0",        "ZtoMuMuDisTrkSidebandD0Cut",        "SingleMu_2017"  +  runPeriod,  dirs['fixme']+"2017_final_prompt/fakeTrackBackground_d0Sideband_new")
            zToMuMuEstimate.addChannel  ("DisTrkInvertD0NHits3",  "ZtoMuMuDisTrkSidebandD0CutNHits3",  "SingleMu_2017"  +  runPeriod,  dirs['fixme']+"2017_final_prompt/fakeTrackBackground_d0Sideband_new")
            zToMuMuEstimate.addChannel  ("DisTrkInvertD0NHits4",  "ZtoMuMuDisTrkSidebandD0CutNHits4",  "SingleMu_2017"  +  runPeriod,  dirs['fixme']+"2017_final_prompt/fakeTrackBackground_d0Sideband_new")
            zToMuMuEstimate.addChannel  ("DisTrkInvertD0NHits5",  "ZtoMuMuDisTrkSidebandD0CutNHits5",  "SingleMu_2017"  +  runPeriod,  dirs['fixme']+"2017_final_prompt/fakeTrackBackground_d0Sideband_new")
            zToMuMuEstimate.addChannel  ("DisTrkInvertD0NHits6",  "ZtoMuMuDisTrkSidebandD0CutNHits6",  "SingleMu_2017"  +  runPeriod,  dirs['fixme']+"2017_final_prompt/fakeTrackBackground_d0Sideband_new")
            zToMuMuEstimate.addChannel  ("Basic",                 "BasicSelection",                    "MET_2017"       +  runPeriod,  dirs['Brian']+"2017/fromRutgers/basicSelection")
            zToMuMuEstimate.addChannel  ("ZtoLL",                 "ZtoMuMu",                           "SingleMu_2017"  +  runPeriod,  dirs['Brian']+"2017/zToMuMu")

            print "********************************************************************************"

            nEst = zToMuMuEstimate.printNest ()
            nEstFakeVsNHitsZtoMuMu[runPeriod][minHits] = nEst
            if minHits == 7:
                nEstFake.append( nEst )

            print "********************************************************************************"

            fout.Close ()

            print "\n\n"

    if background == "ELECTRON" or background == "LEPTON" or background == "ALL":

        print "********************************************************************************"
        print "performing electron background estimate in search region (2017", runPeriod, ")"
        print "--------------------------------------------------------------------------------"

        fout = TFile.Open ("electronBkgdEstimate_2017" + runPeriod + ".root", "recreate")

        electronBkgdEstimate = LeptonBkgdEstimate ("electron")
        electronBkgdEstimate.addTFile (fout)
        electronBkgdEstimate.addTCanvas (canvas)
        electronBkgdEstimate.addPrescaleFactor (lumi["MET_2017" + runPeriod] / lumi["SingleElectron_2017" + runPeriod])

        # fixme
        # RAW/RECO missing for 1/5 events in C, 1/9 in E, and 2/4 events in F for ZtoEleDisTrk passing events
        electronTagProbeEffectiveLumi = lumi["SingleElectron_2017" + runPeriod]
        if "C" in runPeriod or runPeriod == "":
            electronTagProbeEffectiveLumi -= (1./5.) * lumi["SingleElectron_2017C"]
        if "E" in runPeriod or runPeriod == "":
            electronTagProbeEffectiveLumi -= (1./9.) * lumi["SingleElectron_2017E"]
        if "F" in runPeriod or runPeriod == "":
            electronTagProbeEffectiveLumi -= (2./4.) * lumi["SingleElectron_2017F"]
        electronBkgdEstimate.addTagProbePassScaleFactor (lumi["SingleElectron_2017" + runPeriod] / electronTagProbeEffectiveLumi)

        electronBkgdEstimate.addLuminosityInInvPb (lumi["MET_2017" + runPeriod])
        electronBkgdEstimate.addLuminosityLabel (str (round (lumi["SingleElectron_2017" + runPeriod] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
        electronBkgdEstimate.addPlotLabel ("SingleElectron 2017" + runPeriod)
        electronBkgdEstimate.addChannel  ("TagProbe",        "ZtoEleProbeTrk",              "SingleEle_2017"         +  runPeriod,  dirs['Brian']+"2017/fromLPC/electronBackgroundNoZCuts")
        electronBkgdEstimate.addChannel  ("TagProbePass",    "ZtoEleProbeTrk",              "SingleEle_rereco_2017"  +  runPeriod,  dirs['Brian']+"2017/fromLPC/electronBackgroundNoZCuts")
        electronBkgdEstimate.addChannel  ("TagProbePassSS",  "ZtoEleProbeTrkWithSSFilter",  "SingleEle_2017"         +  runPeriod,  dirs['Brian']+"2017/fromLPC/electronBackgroundNoZCuts")
        electronBkgdEstimate.addChannel  ("TagPt35",         "ElectronTagPt55",             "SingleEle_2017"         +  runPeriod,  dirs['Brian']+"2017/fromLPC/electronControlRegion")

        #electronBkgdEstimate.addChannel  ("TagPt35MetTrig",  "ElectronTagPt55MetTrig",  "SingleEle_2017"         +  runPeriod,  dirs['Brian']+"2017/fromLPC/electronControlRegion")

        electronBkgdEstimate.addUseHistogramsForPpassMetTriggers (True)
        electronBkgdEstimate.addRebinFactor (4)
        electronBkgdEstimate.addChannel  ("TagPt35MetTrig",    "ElectronTagPt55",  "SingleEle_2017"  +  runPeriod,  dirs['Brian']+"2017/fromLPC/electronControlRegion")
        electronBkgdEstimate.addChannel  ("TagPt35MetL1Trig",  "ElectronTagPt55",  "SingleEle_2017"  +  runPeriod,  dirs['Brian']+"2017/fromLPC/electronControlRegion")

        print "********************************************************************************"

        nEstElectron.append( electronBkgdEstimate.printNest () )

        print "********************************************************************************"

        fout.Close ()

        print "\n\n"

    if background == "MUON" or background == "LEPTON" or background == "ALL":

        print "********************************************************************************"
        print "performing muon background estimate in search region (2017", runPeriod, ")"
        print "--------------------------------------------------------------------------------"

        fout = TFile.Open ("muonBkgdEstimate_2017" + runPeriod + ".root", "recreate")

        muonBkgdEstimate = LeptonBkgdEstimate ("muon")
        muonBkgdEstimate.addTFile (fout)
        muonBkgdEstimate.addTCanvas (canvas)
        muonBkgdEstimate.addPrescaleFactor (lumi["MET_2017" + runPeriod] / lumi["SingleMuon_2017" + runPeriod])

        # fixme
        # RAW/RECO missing for no events in D for ZtoMuDisTrk passing events

        muonBkgdEstimate.addLuminosityInInvPb (lumi["MET_2017" + runPeriod])
        muonBkgdEstimate.addLuminosityLabel (str (round (lumi["SingleMuon_2017" + runPeriod] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
        muonBkgdEstimate.addPlotLabel ("SingleMuon 2017" + runPeriod)
        muonBkgdEstimate.addChannel  ("TagProbe",        "ZtoMuProbeTrk",              "SingleMu_2017"         +  runPeriod,  dirs['fixme']+"2017_final_prompt/stenson/muonBackground")
        muonBkgdEstimate.addChannel  ("TagProbePass",    "ZtoMuProbeTrk",              "SingleMu_rereco_2017"  +  runPeriod,  dirs['fixme']+"2017_final_prompt/stenson/muonBackground")
        muonBkgdEstimate.addChannel  ("TagProbePassSS",  "ZtoMuProbeTrkWithSSFilter",  "SingleMu_2017"         +  runPeriod,  dirs['fixme']+"2017_final_prompt/stenson/sameSign/skims/muonBackground")
        muonBkgdEstimate.addChannel  ("TagPt35",         "MuonTagPt55",                "SingleMu_2017"         +  runPeriod,  dirs['fixme']+"2017_final_prompt/muonBackground_nCtrl_new")

        #muonBkgdEstimate.addChannel  ("TagPt35MetTrig",  "MuonTagPt55MetTrig",  "SingleMu_2017"         +  runPeriod,  dirs['Andrew']+"2017_final_prompt/muonBackground_nCtrl_new")

        muonBkgdEstimate.addUseHistogramsForPpassMetTriggers (True)
        muonBkgdEstimate.addRebinFactor (4)
        muonBkgdEstimate.addChannel  ("TagPt35MetTrig",    "MuonTagPt55",  "SingleMu_2017"  +  runPeriod,  dirs['fixme']+"2017_final_prompt/muonBackground_passesMETTriggers_new")
        muonBkgdEstimate.addChannel  ("TagPt35MetL1Trig",  "MuonTagPt55",  "SingleMu_2017"  +  runPeriod,  dirs['fixme']+"2017_final_prompt/muonBackground_passesMETTriggers_SHINY")

        print "********************************************************************************"

        nEstMuon.append( muonBkgdEstimate.printNest () )

        print "********************************************************************************"

        fout.Close ()

        print "\n\n"

    if background == "TAU" or background == "LEPTON" or background == "ALL":

        print "********************************************************************************"
        print "performing tau background estimate in search region (2017", runPeriod, ")"
        print "--------------------------------------------------------------------------------"

        fout = TFile.Open ("tauBkgdEstimate_2017" + runPeriod + ".root", "recreate")

        tauBkgdEstimate = LeptonBkgdEstimate ("tau")
        tauBkgdEstimate.addTFile (fout)
        tauBkgdEstimate.addTCanvas (canvas)
        tauBkgdEstimate.addPrescaleFactor (lumi["MET_2017" + runPeriod] / lumi["HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_v*"]["Tau_2017" + runPeriod])

        # RAW/RECO missing for no ZtoTauToMuDisTrk passing events

        # fixme
        # RAW/RECO missing for SingleElectron_2017F passing ZtoTauToEleDisTrk events
        if runPeriod == "F":
            tauBkgdEstimate.addTagProbePass1ScaleFactor ( 0.0 )
        else:
            tauToEleTagProbeEffectiveLumi = lumi["SingleElectron_2017" + runPeriod]
            if "F" in runPeriod or runPeriod == "":
                tauToEleTagProbeEffectiveLumi -= lumi["SingleElectron_2017F"]

            tauBkgdEstimate.addTagProbePass1ScaleFactor ( lumi["SingleElectron_2017" + runPeriod] / tauToEleTagProbeEffectiveLumi )

        tauBkgdEstimate.addLuminosityInInvPb (lumi["MET_2017" + runPeriod])
        tauBkgdEstimate.addLuminosityLabel (str (round (lumi["HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_v*"]["Tau_2017" + runPeriod] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
        tauBkgdEstimate.addPlotLabel ("Tau 2017" + runPeriod)
        tauBkgdEstimate.addChannel  ("TagProbe",         "ZtoTauToMuProbeTrk",               "SingleMu_2017"          +  runPeriod,  dirs['fixme']+"2017_final_prompt/stenson/tauToMuonBackground")
        tauBkgdEstimate.addChannel  ("TagProbePass",     "ZtoTauToMuProbeTrk",               "SingleMu_rereco_2017"   +  runPeriod,  dirs['fixme']+"2017_final_prompt/stenson/tauToMuonBackground")
        tauBkgdEstimate.addChannel  ("TagProbePassSS",   "ZtoTauToMuProbeTrkWithSSFilter",   "SingleMu_2017"          +  runPeriod,  dirs['fixme']+"2017_final_prompt/stenson/sameSign/skims/tauToMuonBackground")
        tauBkgdEstimate.addChannel  ("TagProbe1",        "ZtoTauToEleProbeTrk",              "SingleEle_2017"         +  runPeriod,  dirs['fixme']+"2017_final_prompt/stenson/tauToElectronBackground")
        tauBkgdEstimate.addChannel  ("TagProbePass1",    "ZtoTauToEleProbeTrk",              "SingleEle_rereco_2017"  +  runPeriod,  dirs['fixme']+"2017_final_prompt/stenson/tauToElectronBackground")
        tauBkgdEstimate.addChannel  ("TagProbePassSS1",  "ZtoTauToEleProbeTrkWithSSFilter",  "SingleEle_2017"         +  runPeriod,  dirs['fixme']+"2017_final_prompt/stenson/sameSign/skims/tauToElectronBackground")
        tauBkgdEstimate.addChannel  ("TagPt35",          "TauTagPt55",                       "Tau_2017"               +  runPeriod,  dirs['fixme']+"2017_final_prompt/tauBackground_nCtrl_new")

        #tauBkgdEstimate.addChannel  ("TagPt35MetTrig",  "TauTagPt55MetTrig",       "Tau_2017"               +  runPeriod,  dirs['fixme']+"2017_final_prompt/tauBackground_nCtrl_new")
        #tauBkgdEstimate.addChannel  ("TrigEffDenom",    "ElectronTagPt55",         "SingleEle_2017"         +  runPeriod,  dirs['fixme']+"2017_final_prompt/electronBackground_nCtrl_new")
        #tauBkgdEstimate.addChannel  ("TrigEffNumer",    "ElectronTagPt55MetTrig",  "SingleEle_2017"         +  runPeriod,  dirs['fixme']+"2017_final_prompt/electronBackground_nCtrl_new")

        tauBkgdEstimate.addUseHistogramsForPpassMetTriggers (True)
        tauBkgdEstimate.addRebinFactor (8)
        tauBkgdEstimate.addChannel  ("TagPt35MetTrig",    "TauTagPt55",              "Tau_2017"               +  runPeriod,  dirs['fixme']+"2017_final_prompt/tauBackground_passesMETTriggers_new")
        tauBkgdEstimate.addChannel  ("TagPt35MetL1Trig",  "TauTagPt55",              "Tau_2017"               +  runPeriod,  dirs['fixme']+"2017_final_prompt/tauBackground_passesMETTriggers_SHINY")

        print "********************************************************************************"

        nEstTau.append ( tauBkgdEstimate.printNest () )

        print "********************************************************************************"

        fout.Close ()

        print "\n\n"

# fixme
# Redo the calculation of P_veto with the full 2015+2016 datasets so that the
# track pt dependence of P_veto can be plotted.

sys.stdout = nullout

if background == "ELECTRON" or background == "LEPTON" or background == "ALL":
    fout = TFile.Open ("electronBkgdEstimate.root", "recreate")
    electronBkgdEstimate = LeptonBkgdEstimate ("electron")
    electronBkgdEstimate.addTFile (fout)
    electronBkgdEstimate.addTCanvas (canvas)
    electronBkgdEstimate.addLuminosityLabel (str (round ((lumi["SingleElectron_2015"] + lumi["SingleElectron_2017"]) / 1000.0, 2)) + " fb^{-1} (13 TeV)")
    electronBkgdEstimate.addChannel  ("TagProbe",        "ZtoEleProbeTrk",              "SingleEle_2017"         +  runPeriod,  dirs['Brian']+"2017/fromLPC/electronBackgroundNoZCuts")
    electronBkgdEstimate.addChannel  ("TagProbePass",    "ZtoEleProbeTrk",              "SingleEle_rereco_2017"  +  runPeriod,  dirs['Brian']+"2017/fromLPC/electronBackgroundNoZCuts")
    electronBkgdEstimate.printPpassVetoTagProbe ()
    fout.Close ()

if background == "MUON" or background == "LEPTON" or background == "ALL":
    fout = TFile.Open ("muonBkgdEstimate.root", "recreate")
    muonBkgdEstimate = LeptonBkgdEstimate ("muon")
    muonBkgdEstimate.addTFile (fout)
    muonBkgdEstimate.addTCanvas (canvas)
    muonBkgdEstimate.addLuminosityLabel (str (round ((lumi["SingleMuon_2015"] + lumi["SingleMuon_2017"]) / 1000.0, 2)) + " fb^{-1} (13 TeV)")
    muonBkgdEstimate.addChannel  ("TagProbe",        "ZtoMuProbeTrk",              "SingleMu_2017"         +  runPeriod,  dirs['fixme']+"2017_final_prompt/stenson/muonBackground")
    muonBkgdEstimate.addChannel  ("TagProbePass",    "ZtoMuProbeTrk",              "SingleMu_rereco_2017"  +  runPeriod,  dirs['fixme']+"2017_final_prompt/stenson/muonBackground")
    muonBkgdEstimate.printPpassVetoTagProbe ()
    fout.Close ()

if background == "TAU" or background == "LEPTON" or background == "ALL":
    fout = TFile.Open ("tauBkgdEstimate.root", "recreate")
    tauBkgdEstimate = LeptonBkgdEstimate ("tau")
    tauBkgdEstimate.addTFile (fout)
    tauBkgdEstimate.addTCanvas (canvas)
    tauBkgdEstimate.addLuminosityLabel (str (round ((lumi["SingleMuon_2015"] + lumi["SingleMuon_2017"]) / 1000.0, 2)) + " fb^{-1} (13 TeV)")
    tauBkgdEstimate.addChannel  ("TagProbe",         "ZtoTauToMuProbeTrk",               "SingleMu_2017"          +  runPeriod,  dirs['fixme']+"2017_final_prompt/stenson/tauToMuonBackground")
    tauBkgdEstimate.addChannel  ("TagProbePass",     "ZtoTauToMuProbeTrk",               "SingleMu_rereco_2017"   +  runPeriod,  dirs['fixme']+"2017_final_prompt/stenson/tauToMuonBackground")
    tauBkgdEstimate.addChannel  ("TagProbe1",        "ZtoTauToEleProbeTrk",              "SingleEle_2017"         +  runPeriod,  dirs['fixme']+"2017_final_prompt/stenson/tauToElectronBackground")
    tauBkgdEstimate.addChannel  ("TagProbePass1",    "ZtoTauToEleProbeTrk",              "SingleEle_rereco_2017"  +  runPeriod,  dirs['fixme']+"2017_final_prompt/stenson/tauToElectronBackground")
    tauBkgdEstimate.printPpassVetoTagProbe ()
    fout.Close ()

sys.stdout = stdout

# print sums
if background == "ALL":
    nElectrons = {}
    nMuons = {}
    nTaus = {}
    nLeptons = {}
    nTotal = {}
    nFakes = {}
    for iRunPeriod in range(0,len(runPeriods)):
        print "********************************************************************************"
        nLeptons[runPeriods[iRunPeriod]] = nEstElectron[iRunPeriod] + nEstMuon[iRunPeriod] + nEstTau[iRunPeriod]
        nTotal[runPeriods[iRunPeriod]] = nLeptons[runPeriods[iRunPeriod]] + nEstFake[iRunPeriod]
        print "Total background from leptons (2017", runPeriods[iRunPeriod], "): ", nLeptons[runPeriods[iRunPeriod]]
        print "Total background from fake tracks (2017",runPeriods[iRunPeriod], "): ", nEstFake[iRunPeriod]
        print "********************************************************************************"
        print "Total background (2017", runPeriods[iRunPeriod], "): ", nTotal[runPeriods[iRunPeriod]]
        print "********************************************************************************"
        print "\n\n"

        nElectrons[runPeriods[iRunPeriod]] = nEstElectron[iRunPeriod]
        nMuons[runPeriods[iRunPeriod]] = nEstMuon[iRunPeriod]
        nTaus[runPeriods[iRunPeriod]] = nEstTau[iRunPeriod]
        nFakes[runPeriods[iRunPeriod]] = nEstFake[iRunPeriod]

    x = array ("d"); ex = array ("d")
    electron   =  array  ("d");  muon   =  array  ("d");  tau   =  array  ("d");  fake   =  array  ("d")
    eElectron  =  array  ("d");  eMuon  =  array  ("d");  eTau  =  array  ("d");  eFake  =  array  ("d")

    #runPeriodsToPlot = ["B", "C", "D", "E", "F", "G", "H"]
    runPeriodsToPlot = ["BC", "DEFGH"]
    i = 0.0

    for runPeriod in runPeriodsToPlot:
        x.append (i); ex.append (0.0); i += 1.0

        electron.append  ((nEstElectron[runPeriods.index  (runPeriod)]  /  lumi["MET_2017"  +  runPeriod]).centralValue ())
        muon.append      ((nEstMuon[runPeriods.index      (runPeriod)]  /  lumi["MET_2017"  +  runPeriod]).centralValue ())
        tau.append       ((nEstTau[runPeriods.index       (runPeriod)]  /  lumi["MET_2017"  +  runPeriod]).centralValue ())
        fake.append      ((nEstFake[runPeriods.index      (runPeriod)]  /  lumi["MET_2017"  +  runPeriod]).centralValue ())

        eElectron.append  ((nEstElectron[runPeriods.index  (runPeriod)]  /  lumi["MET_2017"  +  runPeriod]).maxUncertainty ())
        eMuon.append      ((nEstMuon[runPeriods.index      (runPeriod)]  /  lumi["MET_2017"  +  runPeriod]).maxUncertainty ())
        eTau.append       ((nEstTau[runPeriods.index       (runPeriod)]  /  lumi["MET_2017"  +  runPeriod]).maxUncertainty ())
        eFake.append      ((nEstFake[runPeriods.index      (runPeriod)]  /  lumi["MET_2017"  +  runPeriod]).maxUncertainty ())

    gElectron  =  TGraphErrors  (len  (x),  x,  electron,  ex,  eElectron)
    gMuon      =  TGraphErrors  (len  (x),  x,  muon,      ex,  eMuon)
    gTau       =  TGraphErrors  (len  (x),  x,  tau,       ex,  eTau)
    gFake      =  TGraphErrors  (len  (x),  x,  fake,      ex,  eFake)

    fout = TFile.Open ("backgroundCrossSections_2017.root", "recreate")
    fout.cd ()
    gElectron.Write ("electron")
    gMuon.Write ("muon")
    gTau.Write ("tau")
    gFake.Write ("fake")
    fout.Close ()