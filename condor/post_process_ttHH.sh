VERSION=v33

python3 runHHH6bPNetAK4.py --option 4 -o /eos/user/x/xgeng/workspace/HHH/CMSSW_12_5_2/src/hhh-analysis-framework/output/mva-input/${VERSION} --year 2017 --run-signal -n 2 --post



PATHOUTPUT=/eos/user/x/xgeng/workspace/HHH/CMSSW_12_5_2/src/hhh-analysis-framework/output/mva-input/v33_new/2017
mkdir $PATHOUTPUT


python3 /afs/cern.ch/user/x/xgeng/HHH/CMSSW_13_3_0/src/PhysicsTools/NanoAODTools/scripts/haddnano.py $PATHOUTPUT/TTHHTo4b_HEFT_c2-3.root  /eos/user/x/xgeng/workspace/HHH/CMSSW_12_5_2/src/hhh-analysis-framework/output/mva-input/v33_ak8_option4_2017/signal/pieces/TTHHTo4b_HEFT_c2-3*.root






