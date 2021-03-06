from DisappTrks.ToyModels.config_cfg import *
from DisappTrks.StandardAnalysis.customize import *

if not os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    print "Please use a CMSSW_9_4_X release..."
    sys.exit (0)

process = customize (process, 
					 "2017", 
					 applyPUReweighting = True, 
					 applyISRReweighting = False, 
					 applyTriggerReweighting = False, 
					 applyMissingHitsCorrections = False, 
					 runMETFilters = False)

moveVariableProducer(process, "ParticleGunMuonVarProducer", "MuonGunSkim")

# When using these channels for calculating a new weight in MC, use the following customization instead:
# ZtoMuMuISRStudy, ZtoMuMuISRStudyJet30
# hitsSystematicsCtrlSelection, muonCtrlSelection
# process = customize (process, "2017", applyPUReweighting = True, applyISRReweighting = False, applyTriggerReweighting = False, applyMissingHitsCorrections = False, runMETFilters = False)
