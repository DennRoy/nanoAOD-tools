# nanoAOD-tools *Custom*
Tools for working with NanoAOD (requiring only python + root, not CMSSW)

## Set up CMSSW (w PY3), NanoAOD-tools and NanoNN

```
cmsrel CMSSW_13_3_0
```

Python3 is needed to re-run the taggers w/ ONNXRuntime.
`NanoNN` is needed for taggers/regression and PF inputs.
It also contains the module for the hh4b analysis selection.

    cd CMSSW_13_3_0/src
    git clone git@github.com:mstamenk/nanoAOD-tools.git PhysicsTools/NanoAODTools
    git clone git@github.com:mstamenk/NanoNN.git PhysicsTools/NanoNN
    cd PhysicsTools/NanoAODTools
    cmsenv
    scram b -j 10


## HHH6b producer

The producer is located in `../NanoNN/python/producer/hhh6bProducerPNetAK4.py` and contains all the code to run the HHH analysis. The produce runs on NanoAOD samples located either on DAS or on the eos space for HHH. 

The list of files are specified under: `condor/samples/`. There's three files, `_MC` for background Monte-Carlo, `_DATA` for data and `_signalMC`. The current version of the analysis uses `hhh6bPNetAK4_` tag. Once these samples are updated, the list of root files used to run on condor are located under:

```
condor/list/nano/v9-pnetAK4
```

To update new samples, please add them the location list there and then update the list files. 

# Samples path
For running on condor with the full production, the samples are given to the framework through a list:
```
NanoAODTools/condor/samples/hhh6b_2017_DATA.yaml
NanoAODTools/condor/samples/hhh6b_2017_MC.yaml
NanoAODTools/condor/samples/hhh6b_2017_signalMC.yaml
NanoAODTools/condor/samples/xSections.dat # with corresponding cross-sections
```
In addition to the config files (yaml) for the samples in the framework, a list of samples path needs to be created and provided with the correct name matching the yaml:
```
NanoAODTools/condor/list/nano/v9-pnetAK4/2017
```

# Launching full production on condor
To simplify the launching of the production, following scripts are avaialble:
```
source launch_data.sh
source launch_signal.sh 
source launch_qcd6b.sh
```

Modify commands to increase or decrease number of jobs to run. Currently runs about 2000 jobs per year.

Once the samples are done, the samples needs to be postprocessed to add the MC weightand merge them into a single file. Use the following script:

```
source post_process_data.sh
source post_process_signal.sh  
source post_process_qcd6b.sh
```

The output paths need to be modified accordingly to write on your private repository.

# Analysis definition
The analysis is defined in:
```
NanoNN/python/producers/hhh6bProducerPNetAK4.py
```

This is where all the main higgs bosons variables are built and defined. This is also where the reocnstruction is done, the pairing of the jets and all the event related variables are built.


## HH4b producer [OLD INSTRUCTION KEPT FOR REFERENCE]

### Testing the post-processing step locally

The instructions to run the usual NanoAODTools post-processing step can be found in the [nanoAOD-tools](https://github.com/cms-nanoAOD/nanoAOD-tools#general-instructions-to-run-the-post-processing-step) repo.

In our case we use e.g. the [hh4bProducer](https://github.com/cmantill/NanoNN/blob/main/python/producers/hh4bProducer.py). To test it locally you can use:

    python scripts/nano_postproc.py tmp/ /eos/uscms//store/group/lpcdihiggsboost/NanoTuples/V2p0//MC_Autumn18/v1/GluGluToHHTo4B_node_cHHH1_TuneCP5_PSWeights_13TeV-powheg-pythia8/NanoTuples-V2p0_RunIIAutumn18MiniAOD-102X_v15-v1/200801_231026/0000/nano_1.root -I PhysicsTools.NanoNN.producers.hh4bProducer hh4bProducer_2017 --cut "(FatJet_pt>250)" -N 1000 --bo scripts/branch_hh4b_output.txt

or with an ``hh_cfg.json` in the same directory you can use:

    python scripts/nano_postproc.py tmp/ /eos/uscms//store/group/lpcdihiggsboost/NanoTuples/V2p0//MC_Autumn18/v1/GluGluToHHTo4B_node_cHHH1_TuneCP5_PSWeights_13TeV-powheg-pythia8/NanoTuples-V2p0_RunIIAutumn18MiniAOD-102X_v15-v1/200801_231026/0000/nano_1.root -I PhysicsTools.NanoNN.producers.hh4bProducer hh4bProducerFromConfig -N 50 --bo scripts/branch_hh4b_output.txt

Here:
* `tmp` is the output directory
* `root://cmseos.fnal.gov//store/group/lpcdihiggsboost/NanoTuples/V2p0/MC_Fall17/v1/GluGluToHHTo4B_node_cHHH1_TuneCP5_PSWeights_13TeV-powheg-pythia8/NanoTuples-V2p0_RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_v14-v1/200801_230741/0000/nano_16.root` is the input file
* `-I PhysicsTools.NanoNN.producers.hh4bProducer hh4bProducer_2017` is the module and function to run
* the `-c`,`--cut` option is used to pass a string expression (using the same syntax as in TTree::Draw) that will be used to select events.
* the `-J`,`--json` option is used to pass the name of a JSON file that will be used to select events. It is used for data events.
* the `-N` option is selecting only 1000 events for this test.
* `--bi` and `--bo` allows to specify the keep/drop file separately for input and output trees. For `hh4b` we use [these output branches](https://github.com/cmantill/nanoAOD-tools/blob/master/scripts/branch_hh4b_output.txt)

### Scripts to create jobs

Go to the condor directory:

    cd Physics/NanoAODTools/condor
    
All the samples are listed [in the samples directory](https://github.com/cmantill/nanoAOD-tools/tree/master/condor/samples) in yaml files that point to list of files.

The main script to produce condor jobs (and later submit them), is (runPostProcessing.py)[https://github.com/cmantill/nanoAOD-tools/blob/master/condor/runPostProcessing.py], e.g.:

    python runPostProcessing.py [-i /path/of/input] -o /path/to/output -d datasets.yaml -I PhysicsTools.NanoNN.producers.hh4bProducer hh4bProducer_2017 -n 1

However, the [runHH4b.py](https://github.com/cmantill/nanoAOD-tools/blob/master/condor/runHH4b.py) script allows to input some fixed options for the HH4b analysis.

Inside `runHH4b.py` you can specify the samples you want to run for each year [here](https://github.com/cmantill/nanoAOD-tools/blob/master/condor/runHH4b.py#L26-L29). Or you can keep `samples=None` to run over all the samples listed over `--sample-dir` (by default `samples/`).

To run, and create jobs:

    python runHH4b.py --option OPTION -o EOSOUTPUTDIR --year YEAR
    
Here:
* `--option` is equivalent to the selection option in the HHBoostedAnalyzer. Although for now only option=5 (signal region) has been implemented.
* `-o` is the output directory in eos.
* `--year` is the sample year.

### Preparing to run jobs

First, you need to re-tar the CMSSW environment (this needs to be re-done if you modify the producer or any files):

    cd $CMSSW_BASE/../
    tar -zvcf CMSSW_11_1_0_pre5_PY3.tgz CMSSW_11_1_0_pre5_PY3 --exclude="*.pdf" --exclude="*.pyc" --exclude=tmp --exclude-vcs --exclude-caches-all --exclude="*err*" --exclude=*out_* --exclude=condor --exclude=.git

and then copy to your eos directory (change your username here):

    mv CMSSW_11_1_0_pre5_PY3.tgz /eos/uscms/store/user/$USER/

You will also need to change the condor script that points to this tar in [run_processor.sh](https://github.com/cmantill/nanoAOD-tools/blob/master/condor/run_processor.sh#L10).

### Running jobs

Once you have made these changes you can run `runHH4b.py`. For example, for the year 2018:

    python runHH4b.py --option 5 -o  /eos/uscms/store/user/cmantill/analyzer/v0 --year 2018

which will create a metadata json file in `jobs_v0_ak8_option5_2018/mc/metadata.json` and tell you the command to submit the condor jobs:

    condor_submit jobs_v0_ak8_option5_2018/mc/submit.cmd

Command line options:

* the preselection for each option is coded in `runHH4b.py`.
* add `--run-data` to make data trees
* can run data & MC for multiple years together w/ e.g., --year 2016,2017,2018. The --run-data option will be ignored in this case. Add also --run-syst to make the systematic trees. (TODO)
* use --sample-dir to specify the directory containing the sample lists. The main one is running over the HH4b NanoAOD datasets listed in `lists`.
* the --batch option will submit jobs to condor automatically without confirmation
* remove -i to run over remote files (e.g., official NanoAOD, or private NanoAOD published on DAS); consider adding --prefetch to copy files first before running
* add --run-mass-regression to run new ParticleNet mass regression on-the-fly.

e.g. to submit data:

    python runHH4b.py --option 5 -o /eos/uscms/store/user/cmantill/analyzer/v0 --year 2018 --run-data -n 10

### Adding and Re-weighting samples

The `--post` option will `hadd` the output of the condor jobs into `OUTPUTDIR/pieces/` and add the weight branch (computed with the sum of genWeights) to the tree.

    python runHH4b.py --option 5 -o /eos/uscms/store/user/cmantill/analyzer/v0 --year 2018 --post

## Producing training samples

### Preparing to run jobs

First, you need to re-tar the CMSSW environment (this needs to be re-done if you modify the producer in NanoNN or add any files):

    cd $CMSSW_BASE/../
    tar -zvcf CMSSW_11_1_0_pre5_PY3.tgz CMSSW_11_1_0_pre5_PY3 --exclude="*.pdf" --exclude="*.pyc" --exclude=tmp --exclude-vcs --exclude-caches-all --exclude="*err*" --exclude=*out_* --exclude=condor --exclude=".tgz" --exclude=".tar.gz"

and then copy to your eos directory (change your username here):

    mv CMSSW_11_1_0_pre5_PY3.tgz /eos/uscms/store/user/$USER/

You will also need to change the condor script that points to this tar in run_skim_input.sh. While  you are there make sure you change the output directory to your username.

### Testing locally:

For AK8:

    mkdir tmp/
    python scripts/nano_postproc_custom.py tmp/  /eos/uscms/store/user/lpcdihiggsboost/cmantill/PFNano/2017_preUL/GluGluZH_HToWW_M125_13TeV_powheg_pythia8_TuneCP5/RunIIFall17Jan22-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/210202_002923/0000/nano_mc2017_1.root  -I PhysicsTools.NanoNN.producers.inputProducer inputProducer_AK8 --cut "(FatJet_pt>300)&&(FatJet_msoftdrop>20)" --bi scripts/branch_inputs.txt --bo scripts/branch_inputs_output.txt --perJet -N 50000

    python scripts/nano_postproc_custom.py tmp/ /eos/uscms/store/user/lpcdihiggsboost/cmantill/PFNano/2017_preUL_private/GravitonToHHToWWWW/apresyan-crab_PrivateProduction_Fall17_DR_step3_GravitonToHHToWWWW_batch1_v2-5f646ecd4e1c7a39ab0ed099ff55ceb9_Jan22/210202_164913/0000/nano_mc2017_93.root -I PhysicsTools.NanoNN.producers.inputProducer inputProducer_AK8  --bi scripts/branch_inputs.txt --bo scripts/branch_inputs_output.txt --perJet -N 10

    python scripts/nano_postproc_custom.py tmp/ /eos/uscms/store/user/lpcpfnano/cmantill/v2_2/2017/HWW/GluGluHToWWToLNuQQ_M125_TuneCP5_PSweight_13TeV-powheg2-jhugen727-pythia8/GluGluHToWWToLNuQQ/211115_173633/0000/nano_mc2017_1-1.root -I PhysicsTools.NanoNN.producers.inputProducer inputProducer_AK8 --cut "(FatJet_pt>300)&&(FatJet_msoftdrop>20)" --bi scripts/branch_inputs.txt --bo scripts/branch_inputs_output.txt --perJet -N 50000

    python scripts/nano_postproc_custom.py tmp/ /eos/uscms/store/user/lpcpfnano/cmantill/v2_2/2017/HWW/GluGluHToWWToLNuQQ_M125_TuneCP5_PSweight_13TeV-powheg2-jhugen727-pythia8/GluGluHToWWToLNuQQ/211115_173633/0000/nano_mc2017_1-1.root -I PhysicsTools.NanoNN.producers.inputProducer inputProducer_AK8_PFNano --bi scripts/branch_inputs.txt --bo scripts/branch_inputs_output.txt --perJet -N 50000

For AK15: 

    python scripts/nano_postproc_custom.py tmp/ /eos/uscms/store/user/lpcdihiggsboost/cmantill/PFNano/2017_preUL_private_ak15/GravitonToHHToWWWW/apresyan-crab_PrivateProduction_Fall17_DR_step3_GravitonToHHToWWWW_batch1_v2-5f646ecd4e1c7a39ab0ed099ff55ceb9_Mar16/210317_160124/0000/nano_mc2017_1.root  -I PhysicsTools.NanoNN.producers.inputProducer inputProducer_AK15  --cut "(FatJetAK15_pt>300)&&(FatJetAK15_msoftdrop>20)" --bi scripts/branch_inputs.txt --bo scripts/branch_inputs_output.txt --perJet -N 50000

    python scripts/nano_postproc_custom.py tmp/ /eos/uscms/store/user/lpcpfnano/cmantill/v2_2/2017/HWW/GluGluHToWWToLNuQQ_M125_TuneCP5_PSweight_13TeV-powheg2-jhugen727-pythia8/GluGluHToWWToLNuQQ/211115_173633/0000/nano_mc2017_1-1.root -I PhysicsTools.NanoNN.producers.inputProducer inputProducer_AK15_PFNano --cut "(FatJetAK15_pt>300)&&(FatJetAK15_msoftdrop>20)" --bi scripts/branch_inputs.txt --bo scripts/branch_inputs_output.txt --perJet -N 50000

### Running jobs

Run:

    python runSkim.py --tag $TAG --jet $JET_TYPE 

where:
- $TAG is the tag name for the output directory, e.g. ak8_v01hww_30Apr21
- $JET is the type of jet, by default is AK8
- --test allows you run test jobs in condor (recommended)

## Running hh4bWWProducer

To test locally:

    python scripts/nano_postproc.py tmp/ /eos/uscms/store/user/lpcdihiggsboost/cmantill/PFNano/2017_preUL_private_ak15/HHToBBVVToBBQQQQ_cHHH1/apresyan-crab_PrivateProduction_Fall17_DR_step3_HHToBBVVToBBQQQQ_cHHH1_batch2_v1-5f646ecd4e1c7a39ab0ed099ff55ceb9_Mar16/210317_160337/0000/nano_mc2017_7.root -I PhysicsTools.NanoNN.producers.hhbbWWProducer hhbbWWProducer --bo scripts/branch_hh4b_output.txt ```

Running jobs:

    cd condor/
    python runHHbbWW.py --option 1 -o  /eos/uscms/store/user/cmantill/analyzer/v0bbWW --year 2017 # (for mc)
    python runHHbbWW.py --option 1 -o  /eos/uscms/store/user/cmantill/analyzer/v0bbWW --year 2017 --run-signal # (for signal)
    python runHHbbWW.py --option 1 -o  /eos/uscms/store/user/cmantill/analyzer/v0bbWW --year 2017	--run-data # (for data)
 
Make sure to re-tar the directory and copy to your eos space if there are any changes.

You will also need to change the condor script that points to this tar in [run_processor.sh](https://github.com/cmantill/nanoAOD-tools/blob/master/condor/run_processor.sh#L10).
