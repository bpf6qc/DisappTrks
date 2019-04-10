import sys
from optparse import OptionParser

from DisappTrks.SignalMC.signalCrossSecs import *
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *
from DisappTrks.StandardAnalysis.utilities import *

dirs = getUser ()

parser = OptionParser()
parser.add_option("-c", "--outputDir", dest="outputDir",
                  help="output directory")
parser.add_option("-s", "--suffix", dest="suffix", default="",
                  help="directory suffix, typically the date e.g. 2019Apr10")
parser.add_option("-R", "--runRooStatsCl95", action="store_true", dest="runRooStatsCl95", default=False,
                  help="create scripts to run RooStatsCl95")
parser.add_option("-g", "--gamma", action="store_true", dest="runSignalAsGamma", default=False,
                  help="treat signal with gamma function instead of log normal")
parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=False,
                  help="verbose output")
parser.add_option("-M", "--method", dest="method", default="Asymptotic",
                                    help="which method of combine to use: currently supported options are Asymptotic (default), MarkovChainMC and HybridNew")
parser.add_option("-i", "--iterations", dest="Niterations", default="10000",
                  help="how many points are proposed to fill a single Markov chain, default = 10k")
parser.add_option("-r", "--tries", dest="Ntries", default="10",
                  help="how many times the algorithm will run for observed limits, default = 10")
parser.add_option("-t", "--toys", dest="Ntoys", default="1",
                  help="how many toy MC to throw for expected limits, default = 1")
parser.add_option("-b", "--batchMode", action="store_true", dest="batchMode", default=False,
                  help="run on the condor queue")
parser.add_option("-q", "--quick", action="store_true", dest="quick", default=False,
                  help="run only a single sample, for testing")
parser.add_option("-n", "--noPicky", action="store_true", dest="noPicky", default=False,
                  help="do not use --picky in combine options")
parser.add_option("-p", "--paperMode", dest="paperMode", action='store_true', default=False,
                  help="paper mode as EXO-16-044")
parser.add_option("-o", "--saveObjects", dest="saveObjects",
                  help="objects to save in output root file")
parser.add_option("-e", "--era", dest="era", default="",
                  help="data-taking era for which to create cards")
parser.add_option("-l", "--limitType", dest="limitType", default="",
                  help="type of limit to use (which signal grid)")

(arguments, args) = parser.parse_args()

validEras = ["2015", 
             "2016BC", "2016DEFGH", 
             "2017_NLayers4", "2017_NLayers5", "2017_NLayers6plus",
             "20156",
             "2017_all",
             "run2"]

validLimitTypes = ["wino"]
