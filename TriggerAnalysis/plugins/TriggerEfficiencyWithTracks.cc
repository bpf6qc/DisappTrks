#include "CommonTools/Utils/interface/TFileDirectory.h"

#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/PatCandidates/interface/Electron.h"

#include "DisappTrks/TriggerAnalysis/plugins/TriggerEfficiencyWithTracks.h"

TriggerEfficiencyWithTracks::TriggerEfficiencyWithTracks (const edm::ParameterSet &cfg) :
  mets_ (cfg.getParameter<edm::InputTag> ("mets")),
  caloMets_ (cfg.getParameter<edm::InputTag> ("caloMets")),
  tracks_ (cfg.getParameter<edm::InputTag> ("tracks")),
  triggerBits_ (cfg.getParameter<edm::InputTag> ("triggerBits")),
  triggerObjs_ (cfg.getParameter<edm::InputTag> ("triggerObjs")),
  vertices_ (cfg.getParameter<edm::InputTag> ("vertices")),
  genParticles_ (cfg.getParameter<edm::InputTag> ("genParticles")),
  metTriggersList_ ({
    {"hltMETClean75"},
    {"HLT_PFMET120_PFMHT120_IDLoose_v"},
    {"HLT_PFMETNoMu120_NoiseCleaned_PFMHTNoMu120_IDTight_v"},
    {"HLT_PFMET170_NoiseCleaned_v"},
    {"hltMETClean75", "HLT_PFMET120_PFMHT120_IDLoose_v"},
    {"hltMETClean75", "HLT_PFMETNoMu120_NoiseCleaned_PFMHTNoMu120_IDTight_v"},
    {"hltMETClean75", "HLT_PFMET170_NoiseCleaned_v"},
    {"hltMETClean75", "HLT_PFMET120_PFMHT120_IDLoose_v", "HLT_PFMETNoMu120_NoiseCleaned_PFMHTNoMu120_IDTight_v"}
  }),
  metTriggerNames_ ({})
{
  TH1::SetDefaultSumw2 ();
  TFileDirectory MuMETNoMETNoTrigger_metDir = fs_->mkdir ("MuMETNoMETNoTriggerPlotter/Met Plots"),
                 MuMETNoMETNoTrigger_muonDir = fs_->mkdir ("MuMETNoMETNoTriggerPlotter/Muon Plots");
  map<string, TFileDirectory> MuMETNoMET_metDir,
                              MuMETNoMET_muonDir,
                              MuMETNoMuonPt_metDir,
                              MuMETNoMuonPt_muonDir,
                              MuMETNoMuonPtNoTrigger_metDir,
                              MuMETNoMuonPtNoTrigger_muonDir;
  vector<double> bins;
  logSpace (1000, 0.0, 3.0, bins);

  oneDHists_["NoTrigger"];
  twoDHists_["NoTrigger"];

  oneDHists_.at ("NoTrigger")["MuMETNoMETNoTrigger_metDir/metPt"] = MuMETNoMETNoTrigger_metDir.make<TH1D> ("metPt", ";E_{T}^{miss} [GeV]", bins.size () - 1, bins.data ());
  oneDHists_.at ("NoTrigger")["MuMETNoMETNoTrigger_metDir/metPhi"] = MuMETNoMETNoTrigger_metDir.make<TH1D> ("metPhi", ";E_{T}^{miss} #phi", 1000, -3.2, 3.2);
  oneDHists_.at ("NoTrigger")["MuMETNoMETNoTrigger_metDir/caloMetPt"] = MuMETNoMETNoTrigger_metDir.make<TH1D> ("caloMetPt", ";calo E_{T}^{miss} [GeV]", bins.size () - 1, bins.data ());
  oneDHists_.at ("NoTrigger")["MuMETNoMETNoTrigger_metDir/caloMetPhi"] = MuMETNoMETNoTrigger_metDir.make<TH1D> ("caloMetPhi", ";calo E_{T}^{miss} #phi", 1000, -3.2, 3.2);
  oneDHists_.at ("NoTrigger")["MuMETNoMETNoTrigger_muonDir/muonPt"] = MuMETNoMETNoTrigger_muonDir.make<TH1D> ("muonPt", ";muon p_{T} [GeV]", bins.size () - 1, bins.data ());
  oneDHists_.at ("NoTrigger")["MuMETNoMETNoTrigger_muonDir/muonPhi"] = MuMETNoMETNoTrigger_muonDir.make<TH1D> ("muonPhi", ";muon #phi", 1000, -3.2, 3.2);
  oneDHists_.at ("NoTrigger")["MuMETNoMETNoTrigger_muonDir/muonEta"] = MuMETNoMETNoTrigger_muonDir.make<TH1D> ("muonEta", ";muon #eta", 1000, -5.0, 5.0);

  twoDHists_.at ("NoTrigger")["MuMETNoMETNoTrigger_metDir/caloMetVsPFMET"] = MuMETNoMETNoTrigger_metDir.make<TH2D> ("caloMetVsPFMET", ";PF E_{T}^{miss} [GeV];calo E_{T}^{miss} [GeV]", bins.size () - 1, bins.data (), bins.size () - 1, bins.data ());

  for (const auto &metTriggers : metTriggersList_)
    {
      string metTriggerName = "";
      for (auto metTrigger = metTriggers.cbegin (); metTrigger != metTriggers.cend (); metTrigger++)
        {
          metTriggerName += *metTrigger;
          if (metTrigger + 1 != metTriggers.cend ())
            metTriggerName += " OR ";
        }
      metTriggerNames_.push_back (metTriggerName);

      MuMETNoMET_metDir[metTriggerName] = fs_->mkdir ("MuMETNoMETPlotter/" + metTriggerName + "/Met Plots"),
      MuMETNoMET_muonDir[metTriggerName] = fs_->mkdir ("MuMETNoMETPlotter/" + metTriggerName + "/Muon Plots"),
      MuMETNoMuonPt_metDir[metTriggerName] = fs_->mkdir ("MuMETNoMuonPtPlotter/" + metTriggerName + "/Met Plots"),
      MuMETNoMuonPt_muonDir[metTriggerName] = fs_->mkdir ("MuMETNoMuonPtPlotter/" + metTriggerName + "/Muon Plots");
      MuMETNoMuonPtNoTrigger_metDir[metTriggerName] = fs_->mkdir ("MuMETNoMuonPtNoTriggerPlotter/" + metTriggerName + "/Met Plots");
      MuMETNoMuonPtNoTrigger_muonDir[metTriggerName] = fs_->mkdir ("MuMETNoMuonPtNoTriggerPlotter/" + metTriggerName + "/Muon Plots");

      oneDHists_[metTriggerName];
      twoDHists_[metTriggerName];

      oneDHists_.at (metTriggerName)["MuMETNoMET_metDir/metPt"] = MuMETNoMET_metDir.at (metTriggerName).make<TH1D> ("metPt", ";E_{T}^{miss} [GeV]", bins.size () - 1, bins.data ());
      oneDHists_.at (metTriggerName)["MuMETNoMET_metDir/metPhi"] = MuMETNoMET_metDir.at (metTriggerName).make<TH1D> ("metPhi", ";E_{T}^{miss} #phi", 1000, -3.2, 3.2);
      oneDHists_.at (metTriggerName)["MuMETNoMET_metDir/caloMetPt"] = MuMETNoMET_metDir.at (metTriggerName).make<TH1D> ("caloMetPt", ";calo E_{T}^{miss} [GeV]", bins.size () - 1, bins.data ());
      oneDHists_.at (metTriggerName)["MuMETNoMET_metDir/caloMetPhi"] = MuMETNoMET_metDir.at (metTriggerName).make<TH1D> ("caloMetPhi", ";calo E_{T}^{miss} #phi", 1000, -3.2, 3.2);
      oneDHists_.at (metTriggerName)["MuMETNoMET_muonDir/muonPt"] = MuMETNoMET_muonDir.at (metTriggerName).make<TH1D> ("muonPt", ";muon p_{T} [GeV]", bins.size () - 1, bins.data ());
      oneDHists_.at (metTriggerName)["MuMETNoMET_muonDir/muonPhi"] = MuMETNoMET_muonDir.at (metTriggerName).make<TH1D> ("muonPhi", ";muon #phi", 1000, -3.2, 3.2);
      oneDHists_.at (metTriggerName)["MuMETNoMET_muonDir/muonEta"] = MuMETNoMET_muonDir.at (metTriggerName).make<TH1D> ("muonEta", ";muon #eta", 1000, -5.0, 5.0);

      twoDHists_.at (metTriggerName)["MuMETNoMET_metDir/caloMetVsPFMET"] = MuMETNoMET_metDir.at (metTriggerName).make<TH2D> ("caloMetVsPFMET", ";PF E_{T}^{miss} [GeV];calo E_{T}^{miss} [GeV]", bins.size () - 1, bins.data (), bins.size () - 1, bins.data ());

      oneDHists_.at (metTriggerName)["MuMETNoMuonPt_metDir/metPt"] = MuMETNoMuonPt_metDir.at (metTriggerName).make<TH1D> ("metPt", ";E_{T}^{miss} [GeV]", bins.size () - 1, bins.data ());
      oneDHists_.at (metTriggerName)["MuMETNoMuonPt_metDir/metPhi"] = MuMETNoMuonPt_metDir.at (metTriggerName).make<TH1D> ("metPhi", ";E_{T}^{miss} #phi", 1000, -3.2, 3.2);
      oneDHists_.at (metTriggerName)["MuMETNoMuonPt_metDir/caloMetPt"] = MuMETNoMuonPt_metDir.at (metTriggerName).make<TH1D> ("caloMetPt", ";calo E_{T}^{miss} [GeV]", bins.size () - 1, bins.data ());
      oneDHists_.at (metTriggerName)["MuMETNoMuonPt_metDir/caloMetPhi"] = MuMETNoMuonPt_metDir.at (metTriggerName).make<TH1D> ("caloMetPhi", ";calo E_{T}^{miss} #phi", 1000, -3.2, 3.2);
      oneDHists_.at (metTriggerName)["MuMETNoMuonPt_muonDir/muonPt"] = MuMETNoMuonPt_muonDir.at (metTriggerName).make<TH1D> ("muonPt", ";muon p_{T} [GeV]", bins.size () - 1, bins.data ());
      oneDHists_.at (metTriggerName)["MuMETNoMuonPt_muonDir/muonPhi"] = MuMETNoMuonPt_muonDir.at (metTriggerName).make<TH1D> ("muonPhi", ";muon #phi", 1000, -3.2, 3.2);
      oneDHists_.at (metTriggerName)["MuMETNoMuonPt_muonDir/muonEta"] = MuMETNoMuonPt_muonDir.at (metTriggerName).make<TH1D> ("muonEta", ";muon #eta", 1000, -5.0, 5.0);

      twoDHists_.at (metTriggerName)["MuMETNoMuonPt_metDir/caloMetVsPFMET"] = MuMETNoMuonPt_metDir.at (metTriggerName).make<TH2D> ("caloMetVsPFMET", ";PF E_{T}^{miss} [GeV];calo E_{T}^{miss} [GeV]", bins.size () - 1, bins.data (), bins.size () - 1, bins.data ());

      oneDHists_.at (metTriggerName)["MuMETNoMuonPtNoTrigger_metDir/metPt"] = MuMETNoMuonPtNoTrigger_metDir.at (metTriggerName).make<TH1D> ("metPt", ";E_{T}^{miss} [GeV]", bins.size () - 1, bins.data ());
      oneDHists_.at (metTriggerName)["MuMETNoMuonPtNoTrigger_metDir/metPhi"] = MuMETNoMuonPtNoTrigger_metDir.at (metTriggerName).make<TH1D> ("metPhi", ";E_{T}^{miss} #phi", 1000, -3.2, 3.2);
      oneDHists_.at (metTriggerName)["MuMETNoMuonPtNoTrigger_metDir/caloMetPt"] = MuMETNoMuonPtNoTrigger_metDir.at (metTriggerName).make<TH1D> ("caloMetPt", ";calo E_{T}^{miss} [GeV]", bins.size () - 1, bins.data ());
      oneDHists_.at (metTriggerName)["MuMETNoMuonPtNoTrigger_metDir/caloMetPhi"] = MuMETNoMuonPtNoTrigger_metDir.at (metTriggerName).make<TH1D> ("caloMetPhi", ";calo E_{T}^{miss} #phi", 1000, -3.2, 3.2);
      oneDHists_.at (metTriggerName)["MuMETNoMuonPtNoTrigger_muonDir/muonPt"] = MuMETNoMuonPtNoTrigger_muonDir.at (metTriggerName).make<TH1D> ("muonPt", ";muon p_{T} [GeV]", bins.size () - 1, bins.data ());
      oneDHists_.at (metTriggerName)["MuMETNoMuonPtNoTrigger_muonDir/muonPhi"] = MuMETNoMuonPtNoTrigger_muonDir.at (metTriggerName).make<TH1D> ("muonPhi", ";muon #phi", 1000, -3.2, 3.2);
      oneDHists_.at (metTriggerName)["MuMETNoMuonPtNoTrigger_muonDir/muonEta"] = MuMETNoMuonPtNoTrigger_muonDir.at (metTriggerName).make<TH1D> ("muonEta", ";muon #eta", 1000, -5.0, 5.0);

      twoDHists_.at (metTriggerName)["MuMETNoMuonPtNoTrigger_metDir/caloMetVsPFMET"] = MuMETNoMuonPtNoTrigger_metDir.at (metTriggerName).make<TH2D> ("caloMetVsPFMET", ";PF E_{T}^{miss} [GeV];calo E_{T}^{miss} [GeV]", bins.size () - 1, bins.data (), bins.size () - 1, bins.data ());
    }
}

TriggerEfficiencyWithTracks::~TriggerEfficiencyWithTracks ()
{
}

void
TriggerEfficiencyWithTracks::analyze (const edm::Event &event, const edm::EventSetup &setup)
{
  edm::Handle<vector<pat::MET> > mets;
  event.getByLabel (mets_, mets);
  edm::Handle<vector<reco::CaloMET> > caloMets;
  event.getByLabel (caloMets_, caloMets);
  edm::Handle<vector<reco::Track> > tracks;
  event.getByLabel (tracks_, tracks);
  edm::Handle<edm::TriggerResults> triggerBits;
  event.getByLabel (triggerBits_, triggerBits);
  edm::Handle<vector<pat::TriggerObjectStandAlone> > triggerObjs;
  event.getByLabel (triggerObjs_, triggerObjs);
  edm::Handle<vector<reco::Vertex> > vertices;
  event.getByLabel (vertices_, vertices);
  edm::Handle<vector<reco::GenParticle> > genParticles;
  event.getByLabel (genParticles_, genParticles);

  const edm::TriggerNames &triggerNames = event.triggerNames (*triggerBits);
  const reco::Vertex &pv = vertices->at (0);

  //////////////////////////////////////////////////////////////////////////////
  // MuMETNoMETNoTrigger channel
  //////////////////////////////////////////////////////////////////////////////
  fillHistograms (*mets, *caloMets, *tracks, "MuMETNoMETNoTrigger");
  //////////////////////////////////////////////////////////////////////////////

  for (unsigned i = 0; i < metTriggersList_.size (); i++)
    {
      bool passesMETTriggers = false;
      for (const auto &metTrigger : metTriggersList_.at (i))
        {
          passesMETTriggers = passesMETTriggers || (metTrigger.find ("HLT") == 0 ? passesTrigger (triggerNames, *triggerBits, metTrigger) : passesTriggerFilter (triggerNames, *triggerObjs, metTrigger));
          if (passesMETTriggers)
            break;
        }

      //////////////////////////////////////////////////////////////////////////////
      // MuMETNoMET channel
      //////////////////////////////////////////////////////////////////////////////
      if (passesMETTriggers)
        fillHistograms (*mets, *caloMets, *tracks, "MuMETNoMET", metTriggerNames_.at (i));
      //////////////////////////////////////////////////////////////////////////////

      //////////////////////////////////////////////////////////////////////////////
      // MuMETNoMuonPtNoTrigger channel
      //////////////////////////////////////////////////////////////////////////////
      vector<const reco::Track *> selectedTracks;
      selectedTracks.clear ();
      for (const auto &track : *tracks)
        {
          if (fabs (track.eta ()) > 2.5)
            continue;
          if (track.normalizedChi2 () > 10.0)
            continue;
          if (fabs (track.dxy (pv.position ())) > 0.2)
            continue;
          if (fabs (track.dz (pv.position ())) > 0.5)
            continue;
          if (track.hitPattern ().numberOfValidPixelHits () == 0)
            continue;
          if (track.hitPattern ().trackerLayersWithMeasurement () <= 5)
            continue;
          if (track.hitPattern ().trackerLayersWithoutMeasurement (reco::HitPattern::MISSING_INNER_HITS) > 0)
            continue;
          if (track.hitPattern ().trackerLayersWithoutMeasurement (reco::HitPattern::TRACK_HITS) > 0)
            continue;
          if (!genMatched (track, *genParticles, 1000024, 3, 0.1))
            continue;
          if (trackIsolation (track, *tracks, 0.3, 1.0e-12) / track.pt () > 0.01)
            continue;
          selectedTracks.push_back (&track);
        }
      sort (selectedTracks.begin (), selectedTracks.end (), [](const reco::Track *a, const reco::Track *b) -> bool { return (a->pt () > b->pt ()); });
      if (selectedTracks.size () == 1 && passesMETTriggers)
        fillHistograms (*mets, *caloMets, *selectedTracks.at (0), "MuMETNoMuonPtNoTrigger", metTriggerNames_.at (i));
      //////////////////////////////////////////////////////////////////////////////

      //////////////////////////////////////////////////////////////////////////////
      // MuMETNoMuonPt channel
      //////////////////////////////////////////////////////////////////////////////
      if (selectedTracks.size () == 1 && passesMETTriggers && passesTrigger (triggerNames, *triggerBits, "HLT_MET75_IsoTrk50_v"))
        fillHistograms (*mets, *caloMets, *selectedTracks.at (0), "MuMETNoMuonPt", metTriggerNames_.at (i));
      //////////////////////////////////////////////////////////////////////////////
    }
}

void
TriggerEfficiencyWithTracks::logSpace (const unsigned n, const double a, const double b, vector<double> &bins) const
{
  double step = (b - a) / ((double) n);

  bins.clear ();
  for (double i = a; i < b + 0.5 * step; i += step)
    bins.push_back (pow (10.0, i));
}

void
TriggerEfficiencyWithTracks::linSpace (const unsigned n, const double a, const double b, vector<double> &bins) const
{
  double step = (b - a) / ((double) n);

  bins.clear ();
  for (double i = a; i < b + 0.5 * step; i += step)
    bins.push_back (i);
}

void
TriggerEfficiencyWithTracks::fillHistograms (const vector<pat::MET> &mets, const vector<reco::CaloMET> &caloMets, const vector<reco::Track> &tracks, const string &channel, const string &trigger) const
{
  for (const auto &met : mets)
    {
      oneDHists_.at (trigger).at (channel + "_metDir/metPt")->Fill (met.pt ());
      oneDHists_.at (trigger).at (channel + "_metDir/metPhi")->Fill (met.phi ());

      for (const auto &caloMet : caloMets)
        twoDHists_.at (trigger).at (channel + "_metDir/caloMetVsPFMET")->Fill (met.pt (), caloMet.pt ());
    }
  for (const auto &caloMet : caloMets)
    {
      oneDHists_.at (trigger).at (channel + "_metDir/caloMetPt")->Fill (caloMet.pt ());
      oneDHists_.at (trigger).at (channel + "_metDir/caloMetPhi")->Fill (caloMet.phi ());
    }
  for (const auto &track : tracks)
    {
      oneDHists_.at (trigger).at (channel + "_muonDir/muonPt")->Fill (track.pt ());
      oneDHists_.at (trigger).at (channel + "_muonDir/muonPhi")->Fill (track.phi ());
      oneDHists_.at (trigger).at (channel + "_muonDir/muonEta")->Fill (track.eta ());
    }
}

void
TriggerEfficiencyWithTracks::fillHistograms (const vector<pat::MET> &mets, const vector<reco::CaloMET> &caloMets, const reco::Track &track, const string &channel, const string &trigger) const
{
  for (const auto &met : mets)
    {
      oneDHists_.at (trigger).at (channel + "_metDir/metPt")->Fill (met.pt ());
      oneDHists_.at (trigger).at (channel + "_metDir/metPhi")->Fill (met.phi ());

      for (const auto &caloMet : caloMets)
        twoDHists_.at (trigger).at (channel + "_metDir/caloMetVsPFMET")->Fill (met.pt (), caloMet.pt ());
    }
  for (const auto &caloMet : caloMets)
    {
      oneDHists_.at (trigger).at (channel + "_metDir/caloMetPt")->Fill (caloMet.pt ());
      oneDHists_.at (trigger).at (channel + "_metDir/caloMetPhi")->Fill (caloMet.phi ());
    }
  oneDHists_.at (trigger).at (channel + "_muonDir/muonPt")->Fill (track.pt ());
  oneDHists_.at (trigger).at (channel + "_muonDir/muonPhi")->Fill (track.phi ());
  oneDHists_.at (trigger).at (channel + "_muonDir/muonEta")->Fill (track.eta ());
}

bool
TriggerEfficiencyWithTracks::passesTriggerFilter (const edm::TriggerNames &triggerNames, const vector<pat::TriggerObjectStandAlone> &triggerObjs, const string &filter) const
{
  for (auto triggerObj : triggerObjs)
    {
      triggerObj.unpackPathNames (triggerNames);
      for (const auto &filterLabel : triggerObj.filterLabels ())
        {
          if (filterLabel == filter)
            return true;
        }
    }
  return false;
}

bool
TriggerEfficiencyWithTracks::passesTrigger (const edm::TriggerNames &triggerNames, const edm::TriggerResults &triggerBits, const string &path) const
{
  for (unsigned i = 0; i < triggerNames.size (); i++)
    {
      string name = triggerNames.triggerName (i);
      bool pass = triggerBits.accept (i);
      if (name.find (path) == 0)
        return pass;
    }
  return false;
}

double
TriggerEfficiencyWithTracks::trackIsolation (const reco::Track &track, const vector<reco::Track> &tracks, const double outerDeltaR, const double innerDeltaR) const
{
  double sumPt = 0.0;

  for (const auto &t : tracks)
    {
      double dR = deltaR (track, t);
      if (dR < outerDeltaR && dR > innerDeltaR)
        sumPt += t.pt ();
    }

  return sumPt;
}

bool
TriggerEfficiencyWithTracks::genMatched (const reco::Track &track, const vector<reco::GenParticle> &genParticles, const int pdgId, const int status, const double maxDeltaR) const
{
  for (const auto &genParticle : genParticles)
    {
      if (abs (genParticle.pdgId ()) != abs (pdgId))
        continue;
      if (genParticle.status () != status)
        break;
      if (deltaR (track, genParticle) > maxDeltaR)
        continue;
      return true;
    }
  return false;
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(TriggerEfficiencyWithTracks);
