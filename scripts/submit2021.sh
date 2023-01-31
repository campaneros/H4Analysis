### Legacy
# intercalibration
# python scripts/submitBatch.py -r cfg/ECAL_H4_Oct2021/runlist_phase1_intercalibration_nohodo_3x5.txt -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase1_base.cfg -v legacy_v1 -s /eos/home-c/camendol/ECALTB/ECAL_TB_Oct2021/ntuples/ --notar  --spills-per-job 1 -q microcentury
# template
# python scripts/submitBatch.py -r 14635 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase1_templates.cfg -v legacy_templates_v1 -s /eos/home-c/camendol/ECALTB/ECAL_TB_Oct2021/ntuples/ --notar  --spills-per-job 1 -q microcentury 

### Phase 2
# intercalibration
# python scripts/submitBatch.py -r cfg/ECAL_H4_Oct2021/runlist_intercalibration_gainswitch.txt -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base.cfg -v v2 -s /eos/home-c/camendol/ECALTB/ECAL_TB_Oct2021/ntuples/ --notar  --spills-per-job 1 

# base 
# 25 GeV
python scripts/submitBatch.py -r 15183 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_25GeV.cfg  -v templates_v0 -s /eos/user/c/cbasile/ECAL_TB2021/ --notar  --spills-per-job 1 -q microcentury
# 50 GeV
python scripts/submitBatch.py -r 15145 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_50GeV.cfg  -v templates_v0 -s /eos/user/c/cbasile/ECAL_TB2021/ --notar  --spills-per-job 1 -q microcentury
python scripts/submitBatch.py -r 15146 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_50GeV.cfg  -v templates_v0 -s /eos/user/c/cbasile/ECAL_TB2021/ --notar  --spills-per-job 1 -q microcentury
# 75 GeV
python scripts/submitBatch.py -r 15199 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_75GeV.cfg  -v templates_v0 -s /eos/user/c/cbasile/ECAL_TB2021/ --notar  --spills-per-job 1 -q microcentury 
# 100 GeV
#python scripts/submitBatch.py -r 15153 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_100GeV.cfg -v templates_v0 -s /eos/user/c/cbasile/ECAL_TB2021/ --notar  --spills-per-job 1 -q microcentury 
# 125 GeV
python scripts/submitBatch.py -r 15190 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_125GeV.cfg -v templates_v0 -s /eos/user/c/cbasile/ECAL_TB2021/ --notar  --spills-per-job 1 -q microcentury 
# 150 GeV
python scripts/submitBatch.py -r 15158 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_150GeV.cfg -v templates_v0 -s /eos/user/c/cbasile/ECAL_TB2021/ --notar  --spills-per-job 1 -q microcentury 

# template
# High purity, bad synch
#python scripts/submitBatch.py -r 14918 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates.cfg -v templates_v7 -s /eos/home-c/camendol/ECALTB/ECAL_TB_Oct2021/ntuples/ --notar  --spills-per-job 1 -q microcentury # 100 GeV
#python scripts/submitBatch.py -r 14951 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates.cfg -v templates_v7 -s /eos/home-c/camendol/ECALTB/ECAL_TB_Oct2021/ntuples/ --notar  --spills-per-job 1 -q microcentury # 200 GeV
#python scripts/submitBatch.py -r 14821 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates.cfg -v templates_v7 -s /eos/home-c/camendol/ECALTB/ECAL_TB_Oct2021/ntuples/ --notar  --spills-per-job 1 -q microcentury # 250 GeV

# Low purity, good synch
# --- TEMPLATE MAKER --- #
# 25 GeV
#python scripts/submitBatch.py -r 15183 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates.cfg -v v1 -s /eos/user/c/cbasile/ECAL_TB2021/ntuples_templates/ --notar  --spills-per-job 1 -q workday 
# 50 GeV 
#python scripts/submitBatch.py -r 15139 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates.cfg -v v1 -s /eos/user/c/cbasile/ECAL_TB2021/ntuples_templates/ --notar  --spills-per-job 1 -q workday 
#python scripts/submitBatch.py -r 15145 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates.cfg -v v1 -s /eos/user/c/cbasile/ECAL_TB2021/ntuples_templates/ --notar  --spills-per-job 1 -q workday 
#python scripts/submitBatch.py -r 15146 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates.cfg -v v1 -s /eos/user/c/cbasile/ECAL_TB2021/ntuples_templates/ --notar  --spills-per-job 1 -q workday 
# 75 GeV
#python scripts/submitBatch.py -r 15199 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates.cfg -v v1 -s /eos/user/c/cbasile/ECAL_TB2021/ntuples_templates/ --notar  --spills-per-job 1 -q workday 
# 100 GeV
#python scripts/submitBatch.py -r 15153 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates.cfg -v v1 -s /eos/user/c/cbasile/ECAL_TB2021/ntuples_templates/ --notar  --spills-per-job 1 -q workday 
# 125 GeV
#python scripts/submitBatch.py -r 15190 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates.cfg -v v1 -s /eos/user/c/cbasile/ECAL_TB2021/ntuples_templates/ --notar  --spills-per-job 1 -q tomorrow 
# 150 GeV
#python scripts/submitBatch.py -r 15158 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates.cfg -v v1 -s /eos/user/c/cbasile/ECAL_TB2021/ntuples_templates/ --notar  --spills-per-job 1 -q workday 
# 175 GeV
#python scripts/submitBatch.py -r 15208 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates.cfg -v v1 -s /eos/user/c/cbasile/ECAL_TB2021/ntuples_templates/ --notar  --spills-per-job 1 -q tomorrow 
# 200 GeV
#python scripts/submitBatch.py -r 15175 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates.cfg -v v1 -s /eos/user/c/cbasile/ECAL_TB2021/ntuples_templates/ --notar  --spills-per-job 1 -q tomorrow 

#python scripts/submitBatch.py -r 15153 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates.cfg -v testnov22 -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/ --notar  --spills-per-job 1 -q microcentury # 100 GeV


