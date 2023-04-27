# Low purity, good synch
# --- TEMPLATE MAKER --- #
# 25 GeV
python scripts/submitBatch.py -r 15183 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates.cfg -v v1 -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/LowPurity/templates --notar  --spills-per-job 1 -q workday 
# 50 GeV 
python scripts/submitBatch.py -r 15139 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates.cfg -v v1 -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/LowPurity/templates --notar  --spills-per-job 1 -q workday 
python scripts/submitBatch.py -r 15145 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates.cfg -v v1 -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/LowPurity/templates --notar  --spills-per-job 1 -q workday 
python scripts/submitBatch.py -r 15146 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates.cfg -v v1 -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/LowPurity/templates --notar  --spills-per-job 1 -q workday 
# 75 GeV
python scripts/submitBatch.py -r 15199 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates.cfg -v v1 -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/LowPurity/templates --notar  --spills-per-job 1 -q workday 
# 100 GeV
#python scripts/submitBatch.py -r 15153 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates.cfg -v v1 -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/LowPurity/templates --notar  --spills-per-job 1 -q workday 
# 125 GeV
python scripts/submitBatch.py -r 15190 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates.cfg -v v1 -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/LowPurity/templates --notar  --spills-per-job 1 -q tomorrow 
# 150 GeV
python scripts/submitBatch.py -r 15158 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates.cfg -v v1 -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/LowPurity/templates --notar  --spills-per-job 1 -q workday 
# 175 GeV
python scripts/submitBatch.py -r 15208 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates.cfg -v v1 -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/LowPurity/templates --notar  --spills-per-job 1 -q tomorrow 
# 200 GeV
python scripts/submitBatch.py -r 15175 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates.cfg -v v1 -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/LowPurity/templates --notar  --spills-per-job 1 -q tomorrow 

