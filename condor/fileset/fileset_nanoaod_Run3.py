import os
from pprint import pprint

nAOD = "v12"

data = {
	"2022": {
		"JetMET" : [ "/JetHT/Run2022C-22Sep2023-v1/NANOAOD",
					"/JetMET/Run2022C-22Sep2023-v1/NANOAOD",
					"/JetMET/Run2022D-22Sep2023-v1/NANOAOD"],

                    # HHH
                    "HHHTo6B_c3_0_d4_0_TuneCP5_13p6TeV_amcatnlo-pythia8" : ["/HHHTo6B_c3_0_d4_0_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"],
                    "HHHto4B2Tau_c3-0_d4-0_TuneCP5_13p6TeV_amcatnlo-pythia8" : ["/HHHto4B2Tau_c3-0_d4-0_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"],

                    # HH
                    "GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8" : ["/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"],
                    "GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8" : ["/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"],
                    "VBFHHto4B_CV-1_C2V-1_C3-1_TuneCP5_13p6TeV_madgraph-pythia8" : ["/VBFHHto4B_CV-1_C2V-1_C3-1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM", "/VBFHHto4B_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"],
                    "VBFHHto2B2Tau_CV-1_C2V-1_C3-1_TuneCP5_13p6TeV_madgraph-pythia8" : ["/VBFHHto2B2Tau_CV-1_C2V-1_C3-1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM", "/VBFHHto2B2Tau_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"],

                    # QCD
                    "QCD-4Jets_HT-40to70_TuneCP5_13p6TeV_madgraphMLM-pythia8" : ["/QCD-4Jets_HT-40to70_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"], 
                    "QCD-4Jets_HT-70to100_TuneCP5_13p6TeV_madgraphMLM-pythia8" : ["/QCD-4Jets_HT-70to100_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"], 
                    "QCD-4Jets_HT-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8" : ["/QCD-4Jets_HT-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"], 
                    "QCD-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8" : ["/QCD-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"], 
                    "QCD-4Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8"  : ["/QCD-4Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"], 
                    "QCD-4Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8"  : ["/QCD-4Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"], 
                    "QCD-4Jets_HT-800to1000_TuneCP5_13p6TeV_madgraphMLM-pythia8" : ["/QCD-4Jets_HT-800to1000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"], 
                    "QCD-4Jets_HT-1000to1200_TuneCP5_13p6TeV_madgraphMLM-pythia8": [ "/QCD-4Jets_HT-1000to1200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"], 
                    "QCD-4Jets_HT-1200to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8": [ "/QCD-4Jets_HT-1200to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"], 
                    "QCD-4Jets_HT-1500to2000_TuneCP5_13p6TeV_madgraphMLM-pythia8": [  "/QCD-4Jets_HT-1500to2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"], 
                    "QCD-4Jets_HT-2000_TuneCP5_13p6TeV_madgraphMLM-pythia8" : ["/QCD-4Jets_HT-2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"], 
                    # TTbar
                    "TTto4Q_TuneCP5_13p6TeV_powheg-pythia8"        : ["/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM", "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM"], 
                    "TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8"    : ["/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM", "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM"], 
                    "TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8"    : ["/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM", "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM"], 
                    # DY
                    "DYto2L-4Jets_MLL-50_TuneCP5_13p6TeV_madgraphMLM-pythia8"    : ["/DYto2L-4Jets_MLL-50_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM", "/DYto2L-4Jets_MLL-50_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM"], 
                    "DYTo2L_MLL-4to50_TuneCP5_13p6TeV_pythia8" : ["/DYTo2L_MLL-4to50_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"],
                    # VV
                    "WW_TuneCP5_13p6TeV_pythia8" : ["/WW_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"],
                    "WZ_TuneCP5_13p6TeV_pythia8" : ["/WZ_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"],
                    "ZZ_TuneCP5_13p6TeV_pythia8" : ["/ZZ_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"],
                    "WWto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8" : ["/WWto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM", "/WWto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM"],
                    "WWtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8" : ["/WWtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM", "/WWtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM"],
                    "WWto4Q_TuneCP5_13p6TeV_powheg-pythia8" : ["/WWto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  "/WWto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM"],
                    # VVV
                    "WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8" : ["/WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"],
                    "WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8" : ["/WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"],
                    "WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8" : ["/WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"],
                    "ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8" : ["/ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"],
                    # V+Jets
                    "WtoLNu-4Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8"    : ["/WtoLNu-4Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM", "/WtoLNu-4Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM"], 
                    "Zto2Q-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8" : ["/Zto2Q-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"],
                    "Zto2Q-4Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8" : ["/Zto2Q-4Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"],
                    "Zto2Q-4Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8" : ["/Zto2Q-4Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"],
                    "Zto2Q-4Jets_HT-800_TuneCP5_13p6TeV_madgraphMLM-pythia8" : ["/Zto2Q-4Jets_HT-800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"],
                    "Wto2Q-3Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8" : ["/Wto2Q-3Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"],
                    "Wto2Q-3Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8" : ["/Wto2Q-3Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"],
                    "Wto2Q-3Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8" : ["/Wto2Q-3Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"],
                    "Wto2Q-3Jets_HT-800_TuneCP5_13p6TeV_madgraphMLM-pythia8" : ["/Wto2Q-3Jets_HT-800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"],
	},

	"2022EE": {
		"JetMET" : [ "/JetMET/Run2022E-22Sep2023-v1/NANOAOD",
     "/JetMET/Run2022F-22Sep2023-v1/NANOAOD",
					"/JetMET/Run2022G-22Sep2023-v1/NANOAOD",],

                    # HHH
                    "HHHTo6B_c3_0_d4_0_TuneCP5_13p6TeV_amcatnlo-pythia8" : ["/HHHTo6B_c3_0_d4_0_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"],
                    "HHHto4B2Tau_c3-0_d4-0_TuneCP5_13p6TeV_amcatnlo-pythia8" : ["/HHHto4B2Tau_c3-0_d4-0_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"],

                    # HH
                    "GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8" : ["/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-Poisson60KeepRAW_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"],
                    "GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8" : ["/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-Poisson60KeepRAW_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"],
                    "VBFHHto4B_CV-1_C2V-1_C3-1_TuneCP5_13p6TeV_madgraph-pythia8" : ["/VBFHHto4B_CV-1_C2V-1_C3-1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-Poisson60KeepRAW_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"],
                    "VBFHHto2B2Tau_CV-1_C2V-1_C3-1_TuneCP5_13p6TeV_madgraph-pythia8" : ["/VBFHHto2B2Tau_CV-1_C2V-1_C3-1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-Poisson60KeepRAW_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM", "/VBFHHto2B2Tau_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"],

                    # QCD
                    "QCD-4Jets_HT-40to70_TuneCP5_13p6TeV_madgraphMLM-pythia8" : ["/QCD-4Jets_HT-40to70_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM"],
                    "QCD-4Jets_HT-70to100_TuneCP5_13p6TeV_madgraphMLM-pythia8" : ["/QCD-4Jets_HT-70to100_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"], 
                    "QCD-4Jets_HT-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8" : ["/QCD-4Jets_HT-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"], 
                    "QCD-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8" : ["/QCD-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"], 
                    "QCD-4Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8"  : ["/QCD-4Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"], 
                    "QCD-4Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8"  : ["/QCD-4Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"], 
                    "QCD-4Jets_HT-800to1000_TuneCP5_13p6TeV_madgraphMLM-pythia8" : ["/QCD-4Jets_HT-800to1000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"], 
                    "QCD-4Jets_HT-1000to1200_TuneCP5_13p6TeV_madgraphMLM-pythia8": [ "/QCD-4Jets_HT-1000to1200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"],
                    "QCD-4Jets_HT-1200to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8": [ "/QCD-4Jets_HT-1200to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"],
                    "QCD-4Jets_HT-1500to2000_TuneCP5_13p6TeV_madgraphMLM-pythia8": [  "/QCD-4Jets_HT-1500to2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"], 
                    "QCD-4Jets_HT-2000_TuneCP5_13p6TeV_madgraphMLM-pythia8" : ["/QCD-4Jets_HT-2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"], 
                    # TTbar
                    "TTto4Q_TuneCP5_13p6TeV_powheg-pythia8"        : ["/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM", "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM"], 
                    "TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8"    : ["/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM", "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM"], 
                    "TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8"    : ["/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM", "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM"], 
                    # DY
                    "DYto2L-4Jets_MLL-50_TuneCP5_13p6TeV_madgraphMLM-pythia8"    : ["/DYto2L-4Jets_MLL-50_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM", "/DYto2L-4Jets_MLL-50_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM"], 
                    "DYTo2L_MLL-4to50_TuneCP5_13p6TeV_pythia8" : ["/DYToLL_M-4To50_TuneCP5_13p6TeV-pythia8/Run3Summer22EENanoAODv12-Poisson60KeepRAW_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"],
                    # VV
                    "WW_TuneCP5_13p6TeV_pythia8" : ["/WW_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"],
                    "WZ_TuneCP5_13p6TeV_pythia8" : ["/WZ_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"],
                    "ZZ_TuneCP5_13p6TeV_pythia8" : ["/ZZ_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"],
                    "WWto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8" : ["/WWto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM", "/WWto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM"],
                    "WWtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8" : ["/WWtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM", "/WWtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM"],
                    "WWto4Q_TuneCP5_13p6TeV_powheg-pythia8" : ["/WWto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM", "/WWto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM"],
                    # VVV
                    "WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8" : ["/WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"],
                    "WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8" : ["/WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"],
                    "WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8" : ["/WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"],
                    "ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8" : ["/ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"],
                    # V+Jets
                    "WtoLNu-4Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8"    : ["/WtoLNu-4Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM", "/WtoLNu-4Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM"], 
                    "Zto2Q-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8" : ["/Zto2Q-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"],
                    "Zto2Q-4Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8" : ["/Zto2Q-4Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"],
                    "Zto2Q-4Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8" : ["/Zto2Q-4Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"],
                    "Zto2Q-4Jets_HT-800_TuneCP5_13p6TeV_madgraphMLM-pythia8" : ["/Zto2Q-4Jets_HT-800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"],
                    "Wto2Q-3Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8" : ["/Wto2Q-3Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"],
                    "Wto2Q-3Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8" : ["/Wto2Q-3Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"],
                    "Wto2Q-3Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8" : ["/Wto2Q-3Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"],
                    "Wto2Q-3Jets_HT-800_TuneCP5_13p6TeV_madgraphMLM-pythia8" : ["/Wto2Q-3Jets_HT-800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"],
					},
}

def EnsureDir(directory):
  if not os.path.exists(directory):
    os.makedirs(directory)

if __name__ == "__main__":
    for year in ["2022","2022EE"]:
        print(year)
        for sample, subsamples in data[year].items():
            list_name = "../list/nano/%s/%s/%s.list"%(nAOD,year.replace('UL',''),sample)
            if os.path.isfile(list_name): continue
            print(sample)
            list_samples = ""
            for subsample in subsamples:
                pdname = subsample.split("/")[1]
                pdpostfix = subsample.split("/")[2].split("_")[0]
                samplename = year + "_" + pdname + "_" + pdpostfix
                EnsureDir("%s/textfiles"%(nAOD))
                os.system("dasgoclient -query=\"file dataset={}\" 2>&1 | tee {}/textfiles/{}.txt".format(subsample, nAOD, samplename))
                with open("%s/textfiles/%s.txt"%(nAOD,samplename), 'r') as f:
                    list_samples += f.read()
            list_samples = list_samples.replace('/store/','root://cmsxrootd.fnal.gov//store/')
            #if 'JetMET' not in sample:
            #    list_name = "../list/nano/%s/%s/%s.list"%(nAOD,year.replace('UL',''),sample)
            #else:
            #    list_name = "../list/nano/%s/%s/%s_%s.list"%(nAOD,year.replace('UL',''),sample,pdpostfix.split('-')[0].replace('Run',''))

            print(list_name)
            EnsureDir(os.path.dirname(list_name))
            with open(list_name, 'w') as o:
                o.write(list_samples)
