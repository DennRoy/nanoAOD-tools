import json
import os
import re
import sys

import argparse

import htcondor

pjoin = os.path.join

# list of samples to run
samples = {}

samples["AK15"] = {
    "2017preUL_ak15": [
        # "BulkGravTohhTohVVhbb_narrow_M-1000_TuneCP5_13TeV-madgraph-pythia8",
        # "BulkGravTohhTohVVhbb_narrow_M-1800_TuneCP5_13TeV-madgraph-pythia8",
        # "BulkGravTohhTohVVhbb_narrow_M-2000_TuneCP5_13TeV-madgraph-pythia8",
        # "BulkGravTohhTohVVhbb_narrow_M-3000_TuneCP5_13TeV-madgraph-pythia8",
        # "Radion_hh_hVVhbb_inclusive_narrow_M-800_TuneCP5_13TeV-madgraph-pythia8",
        # "Radion_hh_hVVhbb_inclusive_narrow_M-1600_TuneCP5_13TeV-madgraph-pythia8",
        # "Radion_hh_hVVhbb_inclusive_narrow_M-1800_TuneCP5_13TeV-madgraph-pythia8"
        # "Radion_hh_hVVhbb_inclusive_narrow_M-2500_TuneCP5_13TeV-madgraph-pythia8",
        # "Radion_hh_hVVhbb_inclusive_narrow_M-3000_TuneCP5_13TeV-madgraph-pythia8",
        # "Radion_hh_hVVhbb_inclusive_narrow_M-4500_TuneCP5_13TeV-madgraph-pythia8",
        # "BulkGravTohhTohWWhbb_width0p05_M-1000_TuneCP2_13TeV-madgraph_pythia8",
        # "BulkGravTohhTohWWhbb_width0p05_M-1100_TuneCP2_13TeV-madgraph_pythia8",
        # "BulkGravTohhTohWWhbb_width0p05_M-1200_TuneCP2_13TeV-madgraph_pythia8",
        # "BulkGravTohhTohWWhbb_width0p05_M-1400_TuneCP2_13TeV-madgraph_pythia8",
        # "BulkGravTohhTohWWhbb_width0p05_M-1500_TuneCP2_13TeV-madgraph_pythia8",
        # "BulkGravTohhTohWWhbb_width0p05_M-1700_TuneCP2_13TeV-madgraph_pythia8",
        # "BulkGravTohhTohWWhbb_width0p05_M-1800_TuneCP2_13TeV-madgraph_pythia8",
        # "BulkGravTohhTohWWhbb_width0p05_M-1900_TuneCP2_13TeV-madgraph_pythia8",
        
        # "GravitonToHHToWWWW",
        # "GravitonToHHToWWWW_part1",
        # "GravitonToHHToWWWW_part2",

        # "HHToBBVVToBBQQQQ_cHHH1",
        # "HHToBBVVToBBQQQQ_cHHH2p45",
        # "HHToBBVVToBBQQQQ_cHHH5",
        # "HHToBBVVToBBQQQQ_cHHH0",

        # "VBF_HHToBBVVToBBQQQQ_CV_1_C2V_2_C3_1_dipoleRecoilOff",
        
        # "GluGluZH_HToWW_M125_13TeV_powheg_pythia8_TuneCP5",
        # "HWminusJ_HToWW_M125_13TeV_powheg_pythia8_TuneCP5",
        # "HWplusJ_HToWW_M125_13TeV_powheg_pythia8_TuneCP5",
        # "HZJ_HToWW_M125_13TeV_powheg_jhugen714_pythia8_TuneCP5",

        # "GluGluToHHTo4V_node_cHHH1_TuneCP5_PSWeights_13TeV-powheg-pythia8",

        # "BulkGravitonToHHTo4Q_MX-600to6000_MH-15to250_part2_TuneCP5_13TeV-madgraph_pythia8",
        # "BulkGravitonToHHTo4Q_MX-600to6000_MH-15to250_part1_TuneCP5_13TeV-madgraph_pythia8",

        "QCD_HT300to500_TuneCP5_13TeV-madgraph-pythia8",
        "QCD_HT500to700_TuneCP5_13TeV-madgraph-pythia8",
        "QCD_HT700to1000_TuneCP5_13TeV-madgraph-pythia8",
        "QCD_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8",
        "QCD_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8",
        "QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8",

    ],
}

samples["AK8"] = {
    "GravitonToHHToWWWW_lnuqq",
    
    "VBFHToWWToLNuQQ_M125_NNPDF31_TuneCP5_PSweights_13TeV_powheg_JHUGen710_pythia8",
    "GluGluHToWWToLNuQQ_M125_NNPDF31_TuneCP5_PSweights_13TeV_powheg_JHUGen710_pythia8",
    "GluGluToHHTo2B2WToLNu2J_node_SM_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
    
    "GravitonToHHToWWWW",
    "GravitonToHHToWWWW_part1",
    "GravitonToHHToWWWW_part2",
    
    "TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8",
    "TTToHadronic_TuneCP5_13TeV-powheg-pythia8",  
    
    "WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8",
    "WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8",
    "WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8",
    "WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8",
    "WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8", 
}

samples["AK15_PFNano"] = {
    "HWW": {
        "GluGluHToWWToLNuQQ_M125_TuneCP5_PSweight_13TeV-powheg2-jhugen727-pythia8",
        "GluGluToHHTobbVV_node_cHHH1_TuneCP5_13TeV-powheg-pythia8",
        "GluGluToHHTobbVV_node_cHHH0_TuneCP5_13TeV-powheg-pythia8",
        "VBF_HHTobbVV_CV_1_C2V_1_C3_1_TuneCP5_13TeV-madgraph-pythia8",
    },
    "HWWPrivate": {
        "BulkGravitonToHHTo4W_JHUGen_MX-600to6000_MH-15to250_v2",
        "BulkGravitonToHHTo4W_JHUGen_MX-600to6000_MH-15to250_v2_ext1",
        "GluGluHToWWTo4q_HiggspTgt190_M-125_TuneCP5_13TeV-powheg-pythia8",
        "GluGluHToWWTo4q_M-125_TuneCP5_13TeV-powheg-pythia8",
        "GluGluHToWWToLNuQQ_HpT190_M125_TuneCP5_13TeV-powheg-jhugen727-pythia8",
        "GluGluToBulkGravitonToHHTo4W_JHUGen_M-2500_narrow",
    },
    "QCD": {
        # "QCD_Pt_170to300_TuneCP5_13TeV_pythia8",
        "QCD_Pt_300to470_TuneCP5_13TeV_pythia8",
        "QCD_Pt_470to600_TuneCP5_13TeV_pythia8",
        "QCD_Pt_600to800_TuneCP5_13TeV_pythia8",
        "QCD_Pt_800to1000_TuneCP5_13TeV_pythia8",
        "QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8",
        "QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8",
        "QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8",
        "QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8",
        "QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8",
    },
    "TTbar": {
        "TTToHadronic_TuneCP5_13TeV-powheg-pythia8",
        "TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8",
    },
    "WJetsToLNu": {
        # "WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8",
        # "WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8",
        "WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8",
        "WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8",
        "WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8",
        "WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8",
        "WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8",
        "WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8",
    },
}

samples["AK8_PFNano"] = samples["AK15_PFNano"]

# submit job for a dataset
def submit_job(dataset, files, tag, jet, test=False):
    
    outdir = "/store/user/cmantill/PFNano/training/%s/%s"%(tag, dataset)
        
    os.system("eos root://cmseos.fnal.gov/ mkdir -p %s"%outdir) 
            
    # max-entries (for input only now)
    nentries = 4000
    if "HH" in dataset or "HToWW" in dataset or 'hh' in dataset or 'HHTo4W' in dataset:
        nentries = 500000

    print(dataset,nentries)

    # script to run
    execname = "run_skim_input.sh"
    executable = os.path.abspath("./%s"%execname)

    for ifile,f in enumerate(files):
        if test:
            if ifile>0: continue

        lfiles = f
        
        #cut = "(FatJet_pt>300&&FatJet_msoftdrop>20)"
        #if jet=="AK15": cut = "(FatJetAK15_pt>300&&FatJetAK15_msoftdrop>20)"

        arguments = [
            f,
            nentries,
            tag,
            dataset,
            jet,
            #cut
        ]
        
        # define submission settings
        subdir = "log/%s/"%tag
        os.system('mkdir -p %s'%subdir)

        condor_templ_file = open("run_skim_input.jdl")
        jobfile = pjoin(subdir, "%s_%s_%i.jdl"% (execname.replace('.sh',''), dataset, ifile) )                                                                                                           
        condor_file = open(jobfile,"w")
        for line in condor_templ_file:
            line=line.replace('DIREXE',executable)
            line=line.replace('DIRECTORY',subdir)
            line=line.replace('PREFIX',dataset)
            line=line.replace('JOBID',str(ifile))
            line=line.replace('ARGS'," ".join([str(x) for x in arguments]))
            condor_file.write(line)
        condor_file.close()
        
        os.system('condor_submit %s'%jobfile)
        
def main(args):
    for fileset in samples[args.jet].keys():
        if "PFNano" in args.jet:
            with open("fileset/v2_2/2017.json") as f:
                datasets = json.loads(f.read())[fileset]
        else:
            with open("fileset/%s.json"%fileset) as f:
                datasets = json.loads(f.read())

        for dataset,files in datasets.items():
            if "PFNano" in args.jet:
                files = ["root://cmseos.fnal.gov/"+f for f in files]
            if dataset in samples[args.jet][fileset]:
                submit_job(dataset, files, args.tag, args.jet, args.test)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--tag',        dest='tag',      default="test", help="output tag")
    parser.add_argument('--jet',        dest='jet',      default="AK8", help="jet Type")
    parser.add_argument('--test',       dest='test',     action='store_true', default=False, help="test with one file")

    args = parser.parse_args()

    main(args)
