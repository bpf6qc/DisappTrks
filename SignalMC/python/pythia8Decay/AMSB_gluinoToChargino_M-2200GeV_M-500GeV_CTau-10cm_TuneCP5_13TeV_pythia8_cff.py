COM_ENERGY = 13000.
MGLU = 2200  # GeV
MCHI = 500  # GeV
CTAU = 100  # mm
CROSS_SECTION = 0.000356 # pb
SLHA_TABLE="""
#  ISAJET SUSY parameters in SUSY Les Houches Accord 2 format
#  Created by ISALHA 2.0 Last revision: C. Balazs 21 Apr 2009
Block SPINFO   # Program information
     1   ISASUGRA from ISAJET          # Spectrum Calculator
     2   7.80   29-OCT-2009 12:50:36   # Version number
Block MODSEL   # Model selection
     1     3   # Minimal anomaly mediated (AMSB) model
Block SMINPUTS   # Standard Model inputs
     1     1.27836266E+02   # alpha_em^(-1)
     2     1.16570000E-05   # G_Fermi
     3     1.17200002E-01   # alpha_s(M_Z)
     4     9.11699982E+01   # m_{Z}(pole)
     5     4.19999981E+00   # m_{b}(m_{b})
     6     1.73070007E+02   # m_{top}(pole)
     7     1.77699995E+00   # m_{tau}(pole)
Block MINPAR   # SUSY breaking input parameters
     1     1.50000000E+03   # m_0
     2     1.74430000E+05   # m_{3/2}
     3     5.00000000E+00   # tan(beta)
     4     1.00000000E+00   # sign(mu)
Block EXTPAR   # Non-universal SUSY breaking parameters
     0     1.12737372E+16   # Input scale
Block MASS   # Scalar and gaugino mass spectrum
#  PDG code   mass                 particle
        24     8.04229965E+01   #  W^+
        25     1.15511902E+02   #  h^0
        35     3.18671997E+03   #  H^0
        36     3.16565356E+03   #  A^0
        37     3.17845288E+03   #  H^+
   1000001     3.56121729E+03   #  dnl
   1000002     3.56034009E+03   #  upl
   1000003     3.56121729E+03   #  stl
   1000004     3.56034033E+03   #  chl
   1000005     3.10211743E+03   #  b1
   1000006     2.56294897E+03   #  t1
   1000011     1.32959814E+03   #  el-
   1000012     1.32121753E+03   #  nuel
   1000013     1.32959814E+03   #  mul-
   1000014     1.32121753E+03   #  numl
   1000015     1.28115686E+03   #  tau1
   1000016     1.31567761E+03   #  nutl
   1000021     %.9g   #  glss
   1000022     4.99829254E+02   #  z1ss
   1000023     1.60168201E+03   #  z2ss
   1000024     5.00002502E+02   #  w1ss
   1000025    -2.81133667E+03   #  z3ss
   1000035     2.81305249E+03   #  z4ss
   1000037     2.81642407E+03   #  w2ss
   2000001     3.61366235E+03   #  dnr
   2000002     3.58297388E+03   #  upr
   2000003     3.61366235E+03   #  str
   2000004     3.58297412E+03   #  chr
   2000005     3.58649536E+03   #  b2
   2000006     3.13307568E+03   #  t2
   2000011     1.28796350E+03   #  er-
   2000013     1.28796350E+03   #  mur-
   2000015     1.32356653E+03   #  tau2
Block ALPHA   # Effective Higgs mixing parameter
         -1.97843567E-01   # alpha
Block STOPMIX   # stop mixing matrix
  1  1     1.02065332E-01   # O_{11}
  1  2    -9.94777679E-01   # O_{12}
  2  1     9.94777679E-01   # O_{21}
  2  2     1.02065332E-01   # O_{22}
Block SBOTMIX   # sbottom mixing matrix
  1  1     9.99975383E-01   # O_{11}
  1  2     7.02077523E-03   # O_{12}
  2  1    -7.02077523E-03   # O_{21}
  2  2     9.99975383E-01   # O_{22}
Block STAUMIX   # stau mixing matrix
  1  1     2.05478176E-01   # O_{11}
  1  2     9.78661716E-01   # O_{12}
  2  1    -9.78661716E-01   # O_{21}
  2  2     2.05478176E-01   # O_{22}
Block NMIX   # neutralino mixing matrix
  1  1    -1.00043009E-03   #
  1  2     9.99558985E-01   #
  1  3    -2.82598697E-02   #
  1  4     9.08957701E-03   #
  2  1     9.99603391E-01   #
  2  2     1.80333573E-03   #
  2  3     2.33832896E-02   #
  2  4    -1.55895352E-02   #
  3  1     5.53086400E-03   #
  3  2    -1.35487262E-02   #
  3  3    -7.06874847E-01   #
  3  4    -7.07187414E-01   #
  4  1     2.75947675E-02   #
  4  2    -2.63707135E-02   #
  4  3    -7.06387043E-01   #
  4  4     7.06796229E-01   #
Block UMIX   # chargino U mixing matrix
  1  1    -9.99171793E-01   # U_{11}
  1  2     4.06901948E-02   # U_{12}
  2  1    -4.06901948E-02   # U_{21}
  2  2    -9.99171793E-01   # U_{22}
Block VMIX   # chargino V mixing matrix
  1  1    -9.99882162E-01   # V_{11}
  1  2     1.53514510E-02   # V_{12}
  2  1    -1.53514510E-02   # V_{21}
  2  2    -9.99882162E-01   # V_{22}
Block GAUGE Q=  2.70318530E+03   #
     1     3.57524961E-01   # g`
     2     6.52378559E-01   # g_2
     3     1.21927977E+00   # g_3
Block YU Q=  2.70318530E+03   #
  3  3     8.46211851E-01   # y_t
Block YD Q=  2.70318530E+03   #
  3  3     6.63219020E-02   # y_b
Block YE Q=  2.70318530E+03   #
  3  3     5.15569262E-02   # y_tau
Block HMIX Q=  2.70318530E+03   # Higgs mixing parameters
     1     2.81156128E+03   # mu(Q)
     2     5.00000000E+00   # tan(beta)(M_GUT)
     3     2.51505371E+02   # Higgs vev at Q
     4     1.00213620E+07   # m_A^2(Q)
Block MSOFT Q=  2.70318530E+03   # DRbar SUSY breaking parameters
     1     1.62324744E+03   # M_1(Q)
     2     4.73120422E+02   # M_2(Q)
     3    -3.27709692E+03   # M_3(Q)
    31     1.32059900E+03   # MeL(Q)
    32     1.32059900E+03   # MmuL(Q)
    33     1.31518896E+03   # MtauL(Q)
    34     1.28408386E+03   # MeR(Q)
    35     1.28408386E+03   # MmuR(Q)
    36     1.27127039E+03   # MtauR(Q)
    41     3.39131226E+03   # MqL1(Q)
    42     3.39131226E+03   # MqL2(Q)
    43     2.96472168E+03   # MqL3(Q)
    44     3.41352490E+03   # MuR(Q)
    45     3.41352490E+03   # McR(Q)
    46     2.46472070E+03   # MtR(Q)
    47     3.44374805E+03   # MdR(Q)
    48     3.44374805E+03   # MsR(Q)
    49     3.45781030E+03   # MbR(Q)
Block AU Q=  2.70318530E+03   #
  1  1     2.80809619E+03   # A_u
  2  2     2.80809619E+03   # A_c
  3  3     2.80809619E+03   # A_t
Block AD Q=  2.70318530E+03   #
  1  1     6.67355664E+03   # A_d
  2  2     6.67355664E+03   # A_s
  3  3     6.67355664E+03   # A_b
Block AE Q=  2.70318530E+03   #
  1  1     1.82787415E+03   # A_e
  2  2     1.82787415E+03   # A_mu
  3  3     1.82787415E+03   # A_tau
#
#
#
#                             =================
#                             |The decay table|
#                             =================
#
#         PDG            Width
DECAY   1000021     5.50675438E+00 # gluino decay
#  BR              NDA  ID1  ID2  ID3
   2.50000000E-01  3    1    -1   1000022
   2.50000000E-01  3    2    -2   1000022
   2.50000000E-01  3    1    -2   1000024
   2.50000000E-01  3    -1   2    -1000024
#
#         PDG            Width
DECAY   1000024     %.9g # chargino decay
#
""" % (MGLU, (1.97326979e-13 / CTAU))

import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(-1),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    SLHATableForPythia8 = cms.string('%s' % SLHA_TABLE),
    comEnergy = cms.double(COM_ENERGY),
    crossSection = cms.untracked.double(CROSS_SECTION),
    maxEventsToPrint = cms.untracked.int32(0),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        processParameters = cms.vstring(
            'SUSY:all = off',
            'SUSY:gg2gluinogluino = on',
            'SUSY:qqbar2gluinogluino = on',
            '1000024:isResonance = false',
            '1000024:oneChannel = 1 1.0 100 1000022 211',
            '1000024:tau0 = %.1f' % CTAU,
            'ParticleDecays:tau0Max = %.1f' % (CTAU * 10),
       ),
        parameterSets = cms.vstring(
            'pythia8CommonSettings',
            'pythia8CP5Settings',
            'processParameters')
    ),
    # The following parameters are required by Exotica_HSCP_SIM_cfi:
    slhaFile = cms.untracked.string(''),   # value not used
    processFile = cms.untracked.string('SimG4Core/CustomPhysics/data/RhadronProcessList.txt'),
    useregge = cms.bool(False),
    hscpFlavor = cms.untracked.string('stau'),
    massPoint = cms.untracked.int32(MCHI),  # value not used
    particleFile = cms.untracked.string('Configuration/GenProduction/python/ThirteenTeV/DisappTrksAMSBCascade/test/geant4_AMSB_chargino_%sGeV_ctau%scm.slha' % (MCHI, CTAU/10))
)

ProductionFilterSequence = cms.Sequence(generator)
