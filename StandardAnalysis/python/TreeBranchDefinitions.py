import FWCore.ParameterSet.Config as cms

from OSUT3Analysis.Configuration.cutUtilities import *

#######################################################
##### Set up the branches to be added to the tree #####
#######################################################

EventVariableBranches_names = [
    "isrPt",
    "lifetimeWeight",
    "cTau_1000024_0",
    "cTau_1000024_1",
    "isrWeight",
    "isrWeightUp",
    "isrWeightDown",
    "puScalingFactor",
    "puScalingFactorUp",
    "puScalingFactorDown",
    "trackScalingFactor",
    "metLegWeight",
    "trackLegWeight",
    "grandOrWeight",
    "grandOrWeightMCUp",
    "grandOrWeightMCDown",
    "grandOrWeightDataUp",
    "grandOrWeightDataDown",
    "L1ECALPrefiringWeight",
    "L1ECALPrefiringWeightUp",
    "L1ECALPrefiringWeightDown",
    "hasPrefiredJets",
    "numPVReco",
    "nJets",
    "nTracks",
    "nTracksInsideJets",
    "nTracksOutsideJets",
    "trackRho",

    "nGoodTPPairs",
    "nProbesPassingVeto",

    "nGoodSSTPPairs",
    "nSSProbesPassingVeto",

    "nGoodTagJetPairs",
    "nGoodTagPFCHPairs",
]

EventVariableBranches = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    branches = cms.VPSet ([cms.PSet(name = cms.string(x), inputVariables = cms.vstring(x)) for x in EventVariableBranches_names]),
)

for srcCTau in [1, 10, 100, 1000, 10000]:
    for i in range(2, 10):
        dst = float(0.1 * i * srcCTau)
        dstCTau = str(int(dst)) if dst > 1 else '0p' + str(int(10 * dst))
        thisName = "lifetimeWeight_1000024_" + str(srcCTau) + "cmTo" + dstCTau + "cm"
        EventVariableBranches.branches.append(
            cms.PSet(
                name = cms.string(thisName),
                inputVariables = cms.vstring(thisName),
            )
        )

MetShiftBranches_names = [
    "noMuPt",
    "noMuPt_JetResUp",
    "noMuPt_JetEnUp",
    "noMuPt_ElectronEnUp",
    "noMuPt_TauEnUp",
    "noMuPt_UnclusteredEnUp",
    "noMuPt_PhotonEnUp",
    "noMuPt_JetResDown",
    "noMuPt_JetEnDown",
    "noMuPt_ElectronEnDown",
    "noMuPt_TauEnDown",
    "noMuPt_UnclusteredEnDown",
    "noMuPt_PhotonEnDown",
]
MetShiftBranches = cms.PSet(
    inputCollection = cms.vstring("mets"),
    branches = cms.VPSet ([cms.PSet(name = cms.string(x), inputVariables = cms.vstring(x)) for x in MetShiftBranches_names]),
)

TrackDebugBranches_names = [
    "packedPixelBarrelHitPattern",
    "packedPixelEndcapHitPattern",
    
    "firstLayerWithValidHit",
    "lastLayerWithValidHit",
    
    "hasValidHitInPixelBarrelLayer1",
    "hasValidHitInPixelBarrelLayer2",
    "hasValidHitInPixelBarrelLayer3",
    "hasValidHitInPixelBarrelLayer4",

    "hasValidHitInPixelEndcapLayer1",
    "hasValidHitInPixelEndcapLayer2",
    "hasValidHitInPixelEndcapLayer3",
    
    "hitPattern_.pixelBarrelLayersNull",
    "hitPattern_.pixelEndcapLayersNull",

    "hitPattern_.numberOfValidPixelHits", 
    "hitPattern_.trackerLayersWithMeasurement",

    "bestTrackNumberOfValidHits",
    "bestTrackNumberOfValidPixelHits",
    "bestTrackNumberOfValidPixelBarrelHits",
    "bestTrackNumberOfValidPixelEndcapHits",
    "bestTrackMissingInnerHits",
    "bestTrackMissingMiddleHits",
    "bestTrackMissingOuterHits",

    "hitAndTOBDrop_bestTrackMissingOuterHits",

    "numberOfTrackerHits",
    "numberOfPixelHits",
    "numberOfStripHits",
    "numberOfPixelBarrelHits",
    "numberOfPixelEndcapHits",
    "numberOfStripTIBHits",
    "numberOfStripTIDHits",
    "numberOfStripTOBHits",
    "numberOfStripTECHits",

    "missingInnerHits",
    "missingMiddleHits",
    "missingOuterHits",

    "missingTrackerHits",
    "missingPixelHits",
    "missingStripHits",
    "missingPixelBarrelHits",
    "missingPixelEndcapHits",
    "missingStripTIBHits",
    "missingStripTIDHits",
    "missingStripTOBHits",
    "missingStripTECHits",

    "expectedTrackerHits",
    "expectedPixelHits",
    "expectedStripHits",
    "expectedPixelBarrelHits",
    "expectedPixelEndcapHits",
    "expectedStripTIBHits",
    "expectedStripTIDHits",
    "expectedStripTOBHits",
    "expectedStripTECHits",

    "expectedIncludeInactiveTrackerHits",
    "expectedIncludeInactivePixelHits",
    "expectedIncludeInactiveStripHits",
    "expectedIncludeInactivePixelBarrelHits",
    "expectedIncludeInactivePixelEndcapHits",
    "expectedIncludeInactiveStripTIBHits",
    "expectedIncludeInactiveStripTIDHits",
    "expectedIncludeInactiveStripTOBHits",
    "expectedIncludeInactiveStripTECHits",

    "trackerLayersNull",
    "pixelLayersNull",
    "stripLayersNull",
    "pixelBarrelLayersNull",
    "pixelEndcapLayersNull",
    "stripTIBLayersNull",
    "stripTIDLayersNull",
    "stripTOBLayersNull",
    "stripTECLayersNull",

    "numberOfBadHits",

    "numberOfLostInnerHits",
    "numberOfLostMiddleHits",
    "numberOfLostOuterHits",
    "numberOfLostHits",

    "pt",
    "eta",
    "phi",
    "normalizedChi2",
    "charge",
    "caloNewDRp5",
    "dRMinJet",

    "deltaRToClosestElectron",
    "deltaRToClosestVetoElectron",
    "deltaRToClosestLooseElectron",
    "deltaRToClosestMediumElectron",
    "deltaRToClosestTightElectron",
    "deltaRToClosestMuon",
    "deltaRToClosestLooseMuon",
    "deltaRToClosestMediumMuon",
    "deltaRToClosestTightMuon",
    "deltaRToClosestTau",
    "deltaRToClosestTauHad",

    "deltaRToClosestPFElectron",
    "deltaRToClosestPFMuon",
    "deltaRToClosestPFChHad",

    "pfElectronIsoDR03",
    "pfPUElectronIsoDR03",
    "pfMuonIsoDR03",
    "pfPUMuonIsoDR03",
    "pfHFIsoDR03",
    "pfPUHFIsoDR03",
    "pfLostTrackIsoDR03",
    "pfPULostTrackIsoDR03",
    "isoTrackIsoDR03",
    "pfChHadIsoDR03",
    "pfPUChHadIsoDR03",
    "pfNeutralHadIsoDR03",
    "pfPUNeutralHadIsoDR03",
    "pfPhotonIsoDR03",
    "pfPUPhotonIsoDR03",

    "caloNewNoPUDRp5",
    "caloNewNoPUDRp5Calo",
    "caloNewNoPUDRp5CentralCalo",
    "caloNewNoPUDRp3",
    "caloNewNoPUDRp3Calo",
    "caloNewNoPUDRp3CentralCalo",
    "caloNewNoPUDRp2",
    "caloNewNoPUDRp2Calo",
    "caloNewNoPUDRp2CentralCalo",
    "caloNewNoPUDRp1",
    "caloNewNoPUDRp1Calo",
    "caloNewNoPUDRp1CentralCalo",

    "trackIsoNoPUDRp5",
    "trackIsoNoPUDRp3",
    "trackIsoNoPUDRp2",
    "trackIsoNoPUDRp1",
]

from DisappTrks.StandardAnalysis.protoConfig_cfg import UseCandidateTracks
if not UseCandidateTracks:
    TrackDebugBranches_names.extend([
        "matchedCaloJetEmEnergy",
        "matchedCaloJetHadEnergy",
        "pfLepOverlap",
        "pfNeutralSum",
        "dz",
        "dxy",
        "dzError",
        "dxyError",
        "fromPV",
        "isHighPurityTrack",
        "isTightTrack",
        "isLooseTrack",
        "dEdxStrip",
        "dEdxPixel",
    ])


TrackDebugBranches = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    branches = cms.VPSet ([cms.PSet(name = cms.string(x), inputVariables = cms.vstring(x)) for x in TrackDebugBranches_names]),
)

IsolatedTrackDebugBranches = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    branches = cms.VPSet ([cms.PSet(name = cms.string("matchedCandidateTrack_" + x), inputVariables = cms.vstring("matchedCandidateTrack." + x)) for x in TrackDebugBranches_names]),
)

TrackEventvariablesDebugBranches = cms.PSet(
    inputCollection = cms.vstring("tracks", "eventvariables"),
    branches = cms.VPSet (
        cms.PSet(
            name = cms.string("trackD0WRTPV"),
            inputVariables = cms.vstring(trackD0WRTPV),
        ),
        cms.PSet(
            name = cms.string("trackDZWRTPV"),
            inputVariables = cms.vstring(trackDZWRTPV),
        ),
        cms.PSet(
            name = cms.string("trackDZWRTPV"),
            inputVariables = cms.vstring(trackDZWRTPV),
        ),
    )   
)
