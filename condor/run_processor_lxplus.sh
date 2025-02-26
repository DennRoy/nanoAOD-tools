#!/bin/bash

jobid=$1
source /cvmfs/cms.cern.ch/cmsset_default.sh
# export X509_USER_PROXY=/afs/cern.ch/user/x/xgeng/HHH/CMSSW_13_3_0/src/PhysicsTools/NanoAODTools/x509up_u153871
echo "Proxy file path: $X509_USER_PROXY"
voms-proxy-info

function peval { echo ">>> $@"; eval "$@"; }




# check out local environment
WORKDIR="$PWD"
if [ ! -z "$CMSSW_BASE" -a -d "$CMSSW_BASE/src" ]; then
  peval "cd $CMSSW_BASE/src"
  peval 'eval `scramv1 runtime -sh`'
  ls -l 
  ls -l PhysicsTools/NanoAODTools/   
  ls -l PhysicsTools/NanoNN/
  peval "cd $WORKDIR"
fi
export PYTHONPATH=PYTHONPATH:"${CMSSW_BASE}/lib/${SCRAM_ARCH}"
export PYTHONPATH=PYTHONPATH:"/afs/cern.ch/user/x/xgeng/HHH/CMSSW_13_3_0/src/PhysicsTools:$PYTHONPATH"


# run
echo "---RUN---"
ls -l
python3 -c "import sys; print('\n'.join(sys.path))"

# python3 /afs/cern.ch/user/x/xgeng/HHH/CMSSW_13_3_0/src/PhysicsTools/NanoAODTools/condor/jobs_v33_ak8_option4_2017/signal/processor.py $jobid
python3 processor.py $jobid
status=$?

ls -l

exit $status
