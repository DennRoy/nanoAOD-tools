VERSION=v34-LPCDR
YEAR=$1

#python2 runHHH6b.py --option 0 -o ${VERSION} --year 2017 -n 1
#condor_submit jobs_${VERSION}_ak8_option0_2017/mc/submit.cmd

#python2 runHHH6b.py --option 1 -o ${VERSION} --year 2017 -n 1
#condor_submit jobs_${VERSION}_ak8_option1_2017/mc/submit.cmd

#python2 runHHH6b.py --option 2 -o ${VERSION} --year 2017 -n 1
#condor_submit jobs_${VERSION}_ak8_option2_2017/mc/submit.cmd

#python2 runHHH6b.py --option 3 -o ${VERSION} --year 2017 -n 1
#condor_submit jobs_${VERSION}_ak8_option3_2017/mc/submit.cmd

python3 runHHH6bPNetAK4.py --option 4 -o /isilon/data/users/mstamenk/hhh-6b-producer-run3/CMSSW_13_3_0/src/PhysicsTools/NanoAODTools/condor/${VERSION} --year ${YEAR} -n 1 --jobprocessor run_processor_lxplus.sh --condordesc 2 --tmpoutdir "\$TMPDIR" 
