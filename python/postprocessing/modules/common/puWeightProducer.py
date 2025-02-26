from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
import ROOT
import os
import numpy as np
ROOT.PyConfig.IgnoreCommandLineOptions = True


class puWeightProducer(Module):
    def __init__(self,
                 myfile,
                 targetfile,
                 myhist="pileup",
                 targethist="pileup",
                 name="puWeight",
                 norm=True,
                 verbose=False,
                 nvtx_var="Pileup_nTrueInt",
                 doSysVar=True
     ):
        print(targetfile,targethist)
        self.targeth = self.loadHisto(targetfile, targethist)
        if doSysVar:
            self.targeth_plus = self.loadHisto(targetfile,
                                               targethist + "_plus")
            self.targeth_minus = self.loadHisto(targetfile,
                                                targethist + "_minus")
        self.fixLargeWeights = True  # temporary fix
        if myfile != "auto":
            self.autoPU = False
            self.myh = self.loadHisto(myfile, myhist)
        else:
            self.fixLargeWeights = False  # AR: it seems to crash with it, to be deugged
            self.autoPU = True
            ROOT.gROOT.cd()
            self.myh = self.targeth.Clone("autoPU")
            self.myh.Reset()
        self.name = name
        self.norm = norm
        self.verbose = verbose
        self.nvtxVar = nvtx_var
        self.doSysVar = doSysVar

        # Try to load module via python dictionaries
        try:
            ROOT.gSystem.Load("libPhysicsToolsNanoAODTools")
            dummy = ROOT.WeightCalculatorFromHistogram
        # Load it via ROOT ACLIC. NB: this creates the object file in the
        # CMSSW directory, causing problems if many jobs are working from the
        # same CMSSW directory
        except Exception as e:
            print("Could not load module via python, trying via ROOT" + str(e))
            if "/WeightCalculatorFromHistogram_cc.so" not in ROOT.gSystem.GetLibraries(
            ):
                print("Load C++ Worker")
                ROOT.gROOT.ProcessLine(
                    ".L %s/src/PhysicsTools/NanoAODTools/src/WeightCalculatorFromHistogram.cc++"
                    % os.environ['CMSSW_BASE'])
            dummy = ROOT.WeightCalculatorFromHistogram

    def loadHisto(self, filename, hname):
        tf = ROOT.TFile.Open(filename)
        hist = tf.Get(hname)
        #hist.SetDirectory(None)
        hist.SetDirectory(0)
        tf.Close()
        return hist

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        if self.autoPU:
            self.myh.Reset()
            print("Computing PU profile for this file")
            ROOT.gROOT.cd()
            inputFile.Get("Events").Project("autoPU",
                                            self.nvtxVar)  # doitfrom inputFile
            if outputFile:
                outputFile.cd()
                self.myh.Write()
        self._worker = ROOT.WeightCalculatorFromHistogram(
            self.myh, self.targeth, self.norm, self.fixLargeWeights,
            self.verbose)
        self.out = wrappedOutputTree
        self.out.branch(self.name, "F")
        if self.doSysVar:
            self._worker_plus = ROOT.WeightCalculatorFromHistogram(
                self.myh, self.targeth_plus, self.norm, self.fixLargeWeights,
                self.verbose)
            self._worker_minus = ROOT.WeightCalculatorFromHistogram(
                self.myh, self.targeth_minus, self.norm, self.fixLargeWeights,
                self.verbose)
            self.out.branch(self.name + "Up", "F")
            self.out.branch(self.name + "Down", "F")

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        if hasattr(event, self.nvtxVar):
            nvtx = int(getattr(event, self.nvtxVar))
            weight = self._worker.getWeight(
                nvtx) if nvtx < self.myh.GetNbinsX() else 1
            if self.doSysVar:
                weight_plus = self._worker_plus.getWeight(
                    nvtx) if nvtx < self.myh.GetNbinsX() else 1
                weight_minus = self._worker_minus.getWeight(
                    nvtx) if nvtx < self.myh.GetNbinsX() else 1
        else:
            weight = 1
        self.out.fillBranch(self.name, weight)
        if self.doSysVar:
            self.out.fillBranch(self.name + "Up", weight_plus)
            self.out.fillBranch(self.name + "Down", weight_minus)
        return True


class puWeightProducer3Files(Module): # used when 3 files provided for data up and down
    def __init__(self,
                 myfile,
                 targetfile,
                 myhist="pileup",
                 targethist="pileup",
                 name="puWeight",
                 norm=True,
                 verbose=False,
                 nvtx_var="Pileup_nTrueInt",
                 doSysVar=True,
                 varfile_up="",
                 varfile_dn="",
     ):
        self.targeth = self.loadHisto(targetfile, targethist)
        if doSysVar:
            if varfile_up=="":
                self.targeth_plus = self.loadHisto(targetfile,
                                                   targethist + "_plus")
            else:
                self.targeth_plus = self.loadHisto(varfile_up,
                                                   targethist)
            if varfile_dn=="":
                self.targeth_minus = self.loadHisto(targetfile,
                                                    targethist + "_minus")
            else:
                self.targeth_minus = self.loadHisto(varfile_dn,
                                                   targethist)
        self.fixLargeWeights = True  # temporary fix
        if myfile != "auto":
            self.autoPU = False
            self.myh = self.loadHisto(myfile, myhist)
        else:
            self.fixLargeWeights = False  # AR: it seems to crash with it, to be deugged
            self.autoPU = True
            ROOT.gROOT.cd()
            self.myh = self.targeth.Clone("autoPU")
            self.myh.Reset()
        self.name = name
        self.norm = norm
        self.verbose = verbose
        self.nvtxVar = nvtx_var
        self.doSysVar = doSysVar

        # Try to load module via python dictionaries
        try:
            ROOT.gSystem.Load("libPhysicsToolsNanoAODTools")
            dummy = ROOT.WeightCalculatorFromHistogram
        # Load it via ROOT ACLIC. NB: this creates the object file in the
        # CMSSW directory, causing problems if many jobs are working from the
        # same CMSSW directory
        except Exception as e:
            print("Could not load module via python, trying via ROOT" + str(e))
            if "/WeightCalculatorFromHistogram_cc.so" not in ROOT.gSystem.GetLibraries(
            ):
                print("Load C++ Worker")
                ROOT.gROOT.ProcessLine(
                    ".L %s/src/PhysicsTools/NanoAODTools/src/WeightCalculatorFromHistogram.cc++"
                    % os.environ['CMSSW_BASE'])
            dummy = ROOT.WeightCalculatorFromHistogram
    def loadHisto(self, filename, hname):
        tf = ROOT.TFile.Open(filename)
        hist = tf.Get(hname)
        hist.SetDirectory(0)
        tf.Close()
        return hist

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        if self.autoPU:
            self.myh.Reset()
            print("Computing PU profile for this file")
            ROOT.gROOT.cd()
            inputFile.Get("Events").Project("autoPU",
                                            self.nvtxVar)  # doitfrom inputFile
            if outputFile:
                outputFile.cd()
                self.myh.Write()
        self._worker = ROOT.WeightCalculatorFromHistogram(
            self.myh, self.targeth, self.norm, self.fixLargeWeights,
            self.verbose)
        self.out = wrappedOutputTree
        self.out.branch(self.name, "F")
        if self.doSysVar:
            self._worker_plus = ROOT.WeightCalculatorFromHistogram(
                self.myh, self.targeth_plus, self.norm, self.fixLargeWeights,
                self.verbose)
            self._worker_minus = ROOT.WeightCalculatorFromHistogram(
                self.myh, self.targeth_minus, self.norm, self.fixLargeWeights,
                self.verbose)
            self.out.branch(self.name + "Up", "F")
            self.out.branch(self.name + "Down", "F")
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        if hasattr(event, self.nvtxVar):
            nvtx = int(getattr(event, self.nvtxVar))
            weight = self._worker.getWeight(
                nvtx) if nvtx < self.myh.GetNbinsX() else 1
            if self.doSysVar:
                weight_plus = self._worker_plus.getWeight(
                    nvtx) if nvtx < self.myh.GetNbinsX() else 1
                weight_minus = self._worker_minus.getWeight(
                    nvtx) if nvtx < self.myh.GetNbinsX() else 1
        else:
            weight = 1
        self.out.fillBranch(self.name, weight)
        if self.doSysVar:
            self.out.fillBranch(self.name + "Up", weight_plus)
            self.out.fillBranch(self.name + "Down", weight_minus)
        return True


# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

pufile_mc2016APV = "%s/src/PhysicsTools/NanoAODTools/python/postprocessing/data/pileup/pileup_profile_Summer16.root" % os.environ[
    'CMSSW_BASE']
pufile_data2016APV = "%s/src/PhysicsTools/NanoAODTools/python/postprocessing/data/pileup/PileupData_GoldenJSON_Full2016.root" % os.environ[
    'CMSSW_BASE']
puWeight_2016APV = lambda: puWeightProducer(pufile_mc2016,
                                         pufile_data2016,
                                         "pu_mc",
                                         "pileup",
                                         verbose=False,
                                         doSysVar=True)
puAutoWeight_2016APV = lambda: puWeightProducer(
    "auto", pufile_data2016, "pu_mc", "pileup", verbose=False)


pufile_mc2016 = "%s/src/PhysicsTools/NanoAODTools/python/postprocessing/data/pileup/pileup_profile_Summer16.root" % os.environ[
    'CMSSW_BASE']
pufile_data2016 = "%s/src/PhysicsTools/NanoAODTools/python/postprocessing/data/pileup/PileupData_GoldenJSON_Full2016.root" % os.environ[
    'CMSSW_BASE']
puWeight_2016 = lambda: puWeightProducer(pufile_mc2016,
                                         pufile_data2016,
                                         "pu_mc",
                                         "pileup",
                                         verbose=False,
                                         doSysVar=True)
puAutoWeight_2016 = lambda: puWeightProducer(
    "auto", pufile_data2016, "pu_mc", "pileup", verbose=False)

pufile_data2017 = "%s/src/PhysicsTools/NanoAODTools/python/postprocessing/data/pileup/PileupHistogram-goldenJSON-13tev-2017-99bins_withVar.root" % os.environ[
    'CMSSW_BASE']
pufile_mc2017 = "%s/src/PhysicsTools/NanoAODTools/python/postprocessing/data/pileup/mcPileup2017.root" % os.environ[
    'CMSSW_BASE']
puWeight_2017 = lambda: puWeightProducer(pufile_mc2017,
                                         pufile_data2017,
                                         "pu_mc",
                                         "pileup",
                                         verbose=False,
                                         doSysVar=True)
puAutoWeight_2017 = lambda: puWeightProducer(
    "auto", pufile_data2017, "pu_mc", "pileup", verbose=False)

pufile_data2018 = "%s/src/PhysicsTools/NanoAODTools/python/postprocessing/data/pileup/PileupHistogram-goldenJSON-13tev-2018-100bins_withVar.root" % os.environ[
    'CMSSW_BASE']
pufile_mc2018 = "%s/src/PhysicsTools/NanoAODTools/python/postprocessing/data/pileup/mcPileup2018.root" % os.environ[
    'CMSSW_BASE']
puWeight_2018 = lambda: puWeightProducer(pufile_mc2018,
                                         pufile_data2018,
                                         "pu_mc",
                                         "pileup",
                                         verbose=False,
                                         doSysVar=True)
puAutoWeight_2018 = lambda: puWeightProducer(
    "auto", pufile_data2018, "pu_mc", "pileup", verbose=False)

# Ultra legacy

# 2016APV

pufile_dataUL2016APV = "%s/src/PhysicsTools/NanoAODTools/python/postprocessing/data/pileup/PileupHistogram-UL2016-100bins_withVar.root" % os.environ[
    'CMSSW_BASE']
pufile_mcUL2016APV = "%s/src/PhysicsTools/NanoAODTools/python/postprocessing/data/pileup/mcPileupUL2016.root" % os.environ[
    'CMSSW_BASE']
puWeight_UL2016APV = lambda: puWeightProducer(pufile_mcUL2016,
                                           pufile_dataUL2016,
                                           "pu_mc",
                                           "pileup",
                                           verbose=False,
                                           doSysVar=True)
puAutoWeight_UL2016APV = lambda: puWeightProducer(
    "auto", pufile_dataUL2016APV, "pu_mc", "pileup", verbose=False)


# 2016
pufile_dataUL2016 = "%s/src/PhysicsTools/NanoAODTools/python/postprocessing/data/pileup/PileupHistogram-UL2016-100bins_withVar.root" % os.environ[
    'CMSSW_BASE']
pufile_mcUL2016 = "%s/src/PhysicsTools/NanoAODTools/python/postprocessing/data/pileup/mcPileupUL2016.root" % os.environ[
    'CMSSW_BASE']
puWeight_UL2016 = lambda: puWeightProducer(pufile_mcUL2016,
                                           pufile_dataUL2016,
                                           "pu_mc",
                                           "pileup",
                                           verbose=False,
                                           doSysVar=True)
puAutoWeight_UL2016 = lambda: puWeightProducer(
    "auto", pufile_dataUL2016, "pu_mc", "pileup", verbose=False)

# 2017
pufile_dataUL2017 = "%s/src/PhysicsTools/NanoAODTools/python/postprocessing/data/pileup/PileupHistogram-UL2017-100bins_withVar.root" % os.environ[
    'CMSSW_BASE']
pufile_mcUL2017 = "%s/src/PhysicsTools/NanoAODTools/python/postprocessing/data/pileup/mcPileupUL2017.root" % os.environ[
    'CMSSW_BASE']
puWeight_UL2017 = lambda: puWeightProducer(pufile_mcUL2017,
                                           pufile_dataUL2017,
                                           "pu_mc",
                                           "pileup",
                                           verbose=False,
                                           doSysVar=True)
puAutoWeight_UL2017 = lambda: puWeightProducer(
    "auto", pufile_dataUL2017, "pu_mc", "pileup", verbose=False)

# 2018
pufile_dataUL2018 = "%s/src/PhysicsTools/NanoAODTools/python/postprocessing/data/pileup/PileupHistogram-UL2018-100bins_withVar.root" % os.environ[
    'CMSSW_BASE']
pufile_mcUL2018 = "%s/src/PhysicsTools/NanoAODTools/python/postprocessing/data/pileup/mcPileupUL2018.root" % os.environ[
    'CMSSW_BASE']
puWeight_UL2018 = lambda: puWeightProducer(pufile_mcUL2018,
                                           pufile_dataUL2018,
                                           "pu_mc",
                                           "pileup",
                                           verbose=False,
                                           doSysVar=True)
puAutoWeight_UL2018 = lambda: puWeightProducer(
    "auto", pufile_dataUL2018, "pu_mc", "pileup", verbose=False)

#
pufile_mc2022 = os.path.join(os.environ['CMSSW_BASE'], "src/PhysicsTools/NanoAODTools/python/postprocessing/data/pileup/pu_mc_2022.root")
pufile_data2022 = os.path.join(os.environ['CMSSW_BASE'], "src/PhysicsTools/NanoAODTools/python/postprocessing/data/pileup/pileupHistogram-Cert_Collisions2022_355100_357900_eraBCD_GoldenJson-13p6TeV-69200ub-99bins.root")
pufile_data2022_up = os.path.join(os.environ['CMSSW_BASE'], "src/PhysicsTools/NanoAODTools/python/postprocessing/data/pileup/pileupHistogram-Cert_Collisions2022_355100_357900_eraBCD_GoldenJson-13p6TeV-72400ub-99bins.root")
pufile_data2022_dn = os.path.join(os.environ['CMSSW_BASE'], "src/PhysicsTools/NanoAODTools/python/postprocessing/data/pileup/pileupHistogram-Cert_Collisions2022_355100_357900_eraBCD_GoldenJson-13p6TeV-66000ub-99bins.root")
puWeight_2022 = lambda: puWeightProducer3Files(pufile_mc2022,
                                         pufile_data2022,
                                         "pileup",
                                         "pileup",
                                         verbose=False,
                                         doSysVar=True,
                                         varfile_up=pufile_data2022_up,
                                         varfile_dn=pufile_data2022_dn)
puAutoWeight_2022 = lambda: puWeightProducer(
    "auto", pufile_data2022, "pileup", "pileup", verbose=False)

pufile_data2022EE = os.path.join(os.environ['CMSSW_BASE'], "src/PhysicsTools/NanoAODTools/python/postprocessing/data/pileup/pileupHistogram-Cert_Collisions2022_359022_362760_eraEFG_GoldenJson-13p6TeV-69200ub-99bins.root")
pufile_data2022EE_up = os.path.join(os.environ['CMSSW_BASE'], "src/PhysicsTools/NanoAODTools/python/postprocessing/data/pileup/pileupHistogram-Cert_Collisions2022_359022_362760_eraEFG_GoldenJson-13p6TeV-72400ub-99bins.root")
pufile_data2022EE_dn = os.path.join(os.environ['CMSSW_BASE'], "src/PhysicsTools/NanoAODTools/python/postprocessing/data/pileup/pileupHistogram-Cert_Collisions2022_359022_362760_eraEFG_GoldenJson-13p6TeV-66000ub-99bins.root")
puWeight_2022EE = lambda: puWeightProducer3Files(pufile_mc2022,
                                         pufile_data2022EE,
                                         "pileup",
                                         "pileup",
                                         verbose=False,
                                         doSysVar=True,
                                         varfile_up=pufile_data2022EE_up,
                                         varfile_dn=pufile_data2022EE_dn)
puAutoWeight_2022EE = lambda: puWeightProducer(
    "auto", pufile_data2022EE, "pileup", "pileup", verbose=False)