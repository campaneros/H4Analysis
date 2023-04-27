#
# To put all templates in separated files
#
#
### 25 GeV

python templates/plot_templates_energy.py -r 15183 -e 25 --out /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/LowPurity/templates/ntuples_v1/results --path /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/LowPurity/templates/ntuples_v1/ 

### 50 GeV

python templates/plot_templates_energy.py -r 15146 -e 50 --out /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/LowPurity/templates/ntuples_v1/results --path /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/LowPurity/templates/ntuples_v1/ 

### 75 GeV

python templates/plot_templates_energy.py -r 15199 -e 75 --out /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/LowPurity/templates/ntuples_v1/results --path /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/LowPurity/templates/ntuples_v1/ 

### 100 GeV

python templates/plot_templates_energy.py -r 15153 -e 100 --out /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/LowPurity/templates/ntuples_v1/results --path /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/LowPurity/templates/ntuples_v1/ 

### 125 GeV

python templates/plot_templates_energy.py -r 15190 -e 125 --out /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/LowPurity/templates/ntuples_v1/results --path /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/LowPurity/templates/ntuples_v1/ 

### 150 GeV

python templates/plot_templates_energy.py -r 15158 -e 150 --out /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/LowPurity/templates/ntuples_v1/results --path /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/LowPurity/templates/ntuples_v1/ 

### VFEs scan ###
python templates/plot_templates_energy.py -r 15007 --crystal A3 -e 100 --out /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ntuples_templates/VFEscan/ --path /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ntuples_templates --beam HP

python templates/plot_templates_energy.py -r 14989 --crystal B3 -e 100 --out /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ntuples_templates/VFEscan/ --path /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ntuples_templates --beam HP

python templates/plot_templates_energy.py -r 14982 --crystal C2 -e 100 --out /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ntuples_templates/VFEscan/ --path /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ntuples_templates --beam HP

python templates/plot_templates_energy.py -r 14985 --crystal D4 -e 100 --out /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ntuples_templates/VFEscan/ --path /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ntuples_templates --beam HP

python templates/plot_templates_energy.py -r 15003 --crystal E4 -e 100 --out /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ntuples_templates/VFEscan/ --path /eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/HighPurity/ntuples_templates --beam HP
