# High purity, bad sync - template-fitter

### INTERCALIBRATION RUN @ 100 GeV
#  with LP template @ 100 GeV
python scripts/submitBatch.py -r 14982 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_100GeV_LP-HP.cfg -v fitLP -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #C2

# with templates for different VFEs
python scripts/submitBatch.py -r 15005 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_100GeV_HP.cfg -v fitVFEs -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #A1
python scripts/submitBatch.py -r 15006 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_100GeV_HP.cfg -v fitVFEs -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #A2
python scripts/submitBatch.py -r 15007 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_100GeV_HP.cfg -v fitVFEs -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #A3
python scripts/submitBatch.py -r 15008 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_100GeV_HP.cfg -v fitVFEs -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #A4
python scripts/submitBatch.py -r 15009 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_100GeV_HP.cfg -v fitVFEs -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #A5

python scripts/submitBatch.py -r 14991 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_100GeV_HP.cfg -v fitVFEs -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #B1
python scripts/submitBatch.py -r 14990 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_100GeV_HP.cfg -v fitVFEs -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #B2
python scripts/submitBatch.py -r 14989 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_100GeV_HP.cfg -v fitVFEs -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #B3
python scripts/submitBatch.py -r 14988 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_100GeV_HP.cfg -v fitVFEs -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #B4
python scripts/submitBatch.py -r 15035 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_100GeV_HP.cfg -v fitVFEs -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #B5 - G1

python scripts/submitBatch.py -r 14992 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_100GeV_HP.cfg -v fitVFEs -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #C1
python scripts/submitBatch.py -r 14982 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_100GeV_HP.cfg -v fitVFEs -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #C2
python scripts/submitBatch.py -r 14918 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_100GeV_HP.cfg -v fitVFEs -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #C3
python scripts/submitBatch.py -r 14987 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_100GeV_HP.cfg -v fitVFEs -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #C4
python scripts/submitBatch.py -r 15040 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_100GeV_HP.cfg -v fitVFEs -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #C5- G1

python scripts/submitBatch.py -r 14999 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_100GeV_HP.cfg -v fitVFEs -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #D1
python scripts/submitBatch.py -r 14983 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_100GeV_HP.cfg -v fitVFEs -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #D2
python scripts/submitBatch.py -r 14984 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_100GeV_HP.cfg -v fitVFEs -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #D3
python scripts/submitBatch.py -r 14985 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_100GeV_HP.cfg -v fitVFEs -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #D4
python scripts/submitBatch.py -r 15045 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_100GeV_HP.cfg -v fitVFEs -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #D5 - G1

python scripts/submitBatch.py -r 15000 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_100GeV_HP.cfg -v fitVFEs -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #E1
python scripts/submitBatch.py -r 15001 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_100GeV_HP.cfg -v fitVFEs -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #E2
python scripts/submitBatch.py -r 15002 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_100GeV_HP.cfg -v fitVFEs -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #E3
python scripts/submitBatch.py -r 15003 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_100GeV_HP.cfg -v fitVFEs -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #E4
python scripts/submitBatch.py -r 15004 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_100GeV_HP.cfg -v fitVFEs -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #E5

# with which templates?
#python scripts/submitBatch.py -r 14918 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates_HP.cfg -v templates -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #C3 
#python scripts/submitBatch.py -r 14982 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_100GeV_HP-HP.cfg -v fitHP -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #C2
python scripts/submitBatch.py -r 14983 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates_HP.cfg -v templates -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #D2
python scripts/submitBatch.py -r 14984 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates_HP.cfg -v templates -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #D3
python scripts/submitBatch.py -r 14985 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates_HP.cfg -v templates -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #D4
python scripts/submitBatch.py -r 14987 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates_HP.cfg -v templates -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #C4
python scripts/submitBatch.py -r 14988 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates_HP.cfg -v templates -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #B4
python scripts/submitBatch.py -r 14989 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates_HP.cfg -v templates -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #B3
python scripts/submitBatch.py -r 14990 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates_HP.cfg -v templates -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #B3
python scripts/submitBatch.py -r 14991 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates_HP.cfg -v templates -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #B1
python scripts/submitBatch.py -r 14992 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates_HP.cfg -v templates -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #C1
python scripts/submitBatch.py -r 14999 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates_HP.cfg -v templates -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #D1
python scripts/submitBatch.py -r 15000 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates_HP.cfg -v templates -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #E1
python scripts/submitBatch.py -r 15001 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates_HP.cfg -v templates -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #E2
python scripts/submitBatch.py -r 15002 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates_HP.cfg -v templates -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #E3
python scripts/submitBatch.py -r 15003 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates_HP.cfg -v templates -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #E4
python scripts/submitBatch.py -r 15004 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates_HP.cfg -v templates -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #E5
python scripts/submitBatch.py -r 15005 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates_HP.cfg -v templates -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #A1
python scripts/submitBatch.py -r 15006 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates_HP.cfg -v templates -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #A2
python scripts/submitBatch.py -r 15007 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates_HP.cfg -v templates -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #A3
python scripts/submitBatch.py -r 15008 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates_HP.cfg -v templates -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #A4
python scripts/submitBatch.py -r 15009 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_templates_HP.cfg -v templates -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow #A5

### ENERGY SCAN ON C3 ###
# with LP template @ 100 GeV
# 100 GeV
python scripts/submitBatch.py -r 14918 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_100GeV_LP-HP.cfg -v fitLP -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow 
## 150 GeV
python scripts/submitBatch.py -r 14934 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_100GeV_LP-HP.cfg -v fitLP -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow 
python scripts/submitBatch.py -r 14943 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_100GeV_LP-HP.cfg -v fitLP -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow 
## 200 GeV
python scripts/submitBatch.py -r 14951 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_100GeV_LP-HP.cfg -v fitLP -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow 
## 250 GeV
python scripts/submitBatch.py -r 14820 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_100GeV_LP-HP.cfg -v fitLP -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow 
python scripts/submitBatch.py -r 14821 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_100GeV_LP-HP.cfg -v fitLP -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow 

# with HP template x VFEs @ 100 GeV
# 100 GeV
python scripts/submitBatch.py -r 14918 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_100GeV_HP.cfg -v fitVFEs -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow 
## 150 GeV
python scripts/submitBatch.py -r 14934 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_100GeV_HP.cfg -v fitVFEs -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow 
python scripts/submitBatch.py -r 14943 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_100GeV_HP.cfg -v fitVFEs -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow 
## 200 GeV
python scripts/submitBatch.py -r 14951 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_100GeV_HP.cfg -v fitVFEs -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow 
## 250 GeV
python scripts/submitBatch.py -r 14820 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_100GeV_HP.cfg -v fitVFEs -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow 
python scripts/submitBatch.py -r 14821 -c cfg/ECAL_H4_Oct2021/ECAL_H4_Phase2_base_100GeV_HP.cfg -v fitVFEs -s /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ --notar  --spills-per-job 1 -q tomorrow 



