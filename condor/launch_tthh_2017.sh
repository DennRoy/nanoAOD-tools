VERSION=v33
YEAR=$1

# python3 runHHH6bPNetAK4.py --option 4 -o /afs/cern.ch/user/x/xgeng/HHH/CMSSW_13_3_0/src/PhysicsTools/NanoAODTools/condor/${VERSION} --year 2017 --run-signal -n 2 --jobprocessor run_processor_lxplus.sh --condordesc 2 --tmpoutdir "/eos/user/x/xgeng/workspace/HHH/CMSSW_12_5_2/src/hhh-analysis-framework/output/mva-input/" --post
# python3 runHHH6bPNetAK4.py --option 4 -o /eos/user/x/xgeng/workspace/HHH/CMSSW_12_5_2/src/hhh-analysis-framework/output/mva-input/${VERSION} --year 2017 --run-signal -n 2 --jobprocessor run_processor_lxplus.sh --condordesc 2 --tmpoutdir "/eos/user/x/xgeng/workspace/HHH/CMSSW_12_5_2/src/hhh-analysis-framework/output/mva-input/" 
python3 runHHH6bPNetAK4.py --option 4 -o /eos/user/x/xgeng/workspace/HHH/CMSSW_12_5_2/src/hhh-analysis-framework/output/mva-input/${VERSION} --year 2017 --run-signal -n 2 --jobprocessor run_processor_lxplus.sh --condordesc 2 --tmpoutdir "\$TMPDIR" 


# --tmpoutdir "\$TMPDIR"