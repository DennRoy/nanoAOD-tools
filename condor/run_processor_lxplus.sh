#!/bin/bash

jobid=$1
source /cvmfs/cms.cern.ch/cmsset_default.sh
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

# run
echo "---RUN---"
ls -l
python3 -c "import sys; print('\n'.join(sys.path))"
python3 processor.py $jobid
status=$?

ls -l

exit $status
