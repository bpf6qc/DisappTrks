#!/usr/bin/env python

import math
from DisappTrks.StandardAnalysis.bkgdEstimate import * 
from DisappTrks.StandardAnalysis.getUser import * 
from ROOT import TCanvas, TFile
import os 

metLumi       =  2590.0
electronLumi  =  2670.0
muonLumi      =  2670.0
tauLumi       =  225.17

dirs = getUser()
canvas = TCanvas("c1", "c1",800,800)
setCanvasStyle(canvas)

print "********************************************************************************"
print "performing fake track background estimate in disappearing track search region"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("fakeTrackBkgdEstimate.root", "recreate")

fakeTrackBkgdEstimate = FakeTrackBkgdEstimate ()
fakeTrackBkgdEstimate.addTFile (fout)
fakeTrackBkgdEstimate.addTCanvas (canvas)
fakeTrackBkgdEstimate.addPrescaleFactor (metLumi / muonLumi)
fakeTrackBkgdEstimate.addChannel  ("ZtoLL",        "ZtoMuMu",         "SingleMu_2015D",  dirs['Andrew']+"withFiducialCuts/zToMuMu")
fakeTrackBkgdEstimate.addChannel  ("ZtoLLdisTrk",  "ZtoMuMuDisTrk",   "SingleMu_2015D",  dirs['Andrew']+"withFiducialCuts/zToMuMuTrack")
fakeTrackBkgdEstimate.addChannel  ("Basic",        "BasicSelection",  "MET_2015D",       dirs['Andrew']+"withFiducialCuts/basicSelection")

print "********************************************************************************"

(nEstFake, nEstFakeError) = fakeTrackBkgdEstimate.printNest ()

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "performing electron background estimate in disappearing track search region"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("electronBkgdEstimate.root", "recreate")

electronBkgdEstimate = LeptonBkgdEstimate ("electron")
electronBkgdEstimate.addTFile (fout)
electronBkgdEstimate.addTCanvas (canvas)
electronBkgdEstimate.addPrescaleFactor (metLumi / electronLumi)
electronBkgdEstimate.addMetCut (100.0)
electronBkgdEstimate.addChannel  ("TagProbe",        "ZtoEleProbeTrkWithZCuts",  "SingleEle_2015D",  dirs['Andrew']+"withFiducialCuts/electronTagAndProbe_withMissingOuterHitsCut")
electronBkgdEstimate.addChannel  ("TagProbePass",    "ZtoEleDisTrk",             "SingleEle_2015D",  dirs['Andrew']+"withFiducialCuts/electronTagAndProbe_withMissingOuterHitsCut")
electronBkgdEstimate.addChannel  ("TagPt35",         "ElectronTagPt55",          "SingleEle_2015D",  dirs['Andrew']+"withFiducialCuts/electronBkgdForDisappearingTrackSelection")
electronBkgdEstimate.addChannel  ("TagPt35MetTrig",  "ElectronTagPt55MetTrig",   "SingleEle_2015D",  dirs['Andrew']+"withFiducialCuts/electronBkgdForDisappearingTrackSelection")

print "********************************************************************************"

(nEstElectron, nEstElectronError) = electronBkgdEstimate.printNest ()

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "performing muon background estimate in disappearing track search region"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("muonBkgdEstimate.root", "recreate")

muonBkgdEstimate = LeptonBkgdEstimate ("muon")
muonBkgdEstimate.addTFile (fout)
muonBkgdEstimate.addTCanvas (canvas)
muonBkgdEstimate.addPrescaleFactor (metLumi / muonLumi)
muonBkgdEstimate.addMetCut (100.0)
muonBkgdEstimate.addChannel  ("TagProbe",        "ZtoMuProbeTrkWithZCuts",  "SingleMu_2015D",  dirs['Andrew']+"withFiducialCuts/muonTagAndProbe_withMissingOuterHitsCut")
muonBkgdEstimate.addChannel  ("TagProbePass",    "ZtoMuDisTrk",             "SingleMu_2015D",  dirs['Andrew']+"withFiducialCuts/muonTagAndProbe_withMissingOuterHitsCut")
muonBkgdEstimate.addChannel  ("TagPt35",         "MuonTagPt55",             "SingleMu_2015D",  dirs['Andrew']+"withFiducialCuts/muonBkgdForDisappearingTrackSelection")
muonBkgdEstimate.addChannel  ("TagPt35MetTrig",  "MuonTagPt55MetTrig",      "SingleMu_2015D",  dirs['Andrew']+"withFiducialCuts/muonBkgdForDisappearingTrackSelection")

print "********************************************************************************"

(nEstMuon, nEstMuonError) = muonBkgdEstimate.printNest ()

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
print "performing tau background estimate in disappearing track search region"
print "--------------------------------------------------------------------------------"

fout = TFile.Open ("tauBkgdEstimate.root", "recreate")

tauBkgdEstimate = LeptonBkgdEstimate ("tau")
tauBkgdEstimate.addTFile (fout)
tauBkgdEstimate.addTCanvas (canvas)
tauBkgdEstimate.addPrescaleFactor (metLumi / tauLumi)
tauBkgdEstimate.addMetCut (100.0)
tauBkgdEstimate.addChannel  ("TagProbe",        "ZtoTauProbeTrkWithZCuts",  "SingleMu_2015D",  dirs['Andrew']+"withFiducialCuts/tauTagAndProbe")
tauBkgdEstimate.addChannel  ("TagProbePass",    "ZtoTauDisTrk",             "SingleMu_2015D",  dirs['Andrew']+"withFiducialCuts/tauTagAndProbe")
tauBkgdEstimate.addChannel  ("TagPt35",         "TauTagPt55",             "Tau_2015D",       dirs['Andrew']+"withFiducialCuts/tauBkgdForDisappearingTrackSelection")
tauBkgdEstimate.addChannel  ("TagPt35MetTrig",  "TauTagPt55MetTrig",      "Tau_2015D",       dirs['Andrew']+"withFiducialCuts/tauBkgdForDisappearingTrackSelection")

print "********************************************************************************"

(nEstTau, nEstTauError) = tauBkgdEstimate.printNest ()

print "********************************************************************************"

fout.Close ()

print "\n\n"

print "********************************************************************************"
nEst = nEstElectron + nEstMuon + nEstTau
nEstError = math.hypot (math.hypot (nEstElectronError, nEstMuonError), nEstTauError)
print "total background from leptons: " + str (nEst) + " +- " + str (nEstError)
print "********************************************************************************"

print "\n\n"

print "********************************************************************************"
nEst += nEstFake
nEstError = math.hypot (nEstError, nEstFakeError)
print "total background: " + str (nEst) + " +- " + str (nEstError)
print "********************************************************************************"