VERSION=v2022

python3 runHHH6bPNetAK4.py --option 4 -o /eos/user/d/dmroy/HHH/sampleProduction/${VERSION} --year 2022EE --run-data -n 1 --jobprocessor run_processor_lxplus.sh --condordesc 2 --tmpoutdir "\$TMPDIR"
#condor_submit jobs_${VERSION}_ak8_option4_2022/data/submit.cmd
