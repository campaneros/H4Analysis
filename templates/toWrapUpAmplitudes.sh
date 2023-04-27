#
# To write on file the amolitudes to fit
#

### 25 GeV

python templates/plot_amplitudes.py -r 15183 -e 25 --path /eos/user/c/cbasile/ECAL_TB2021/ntuples_templates_v2 --minamp 100 --maxamp 700 --out /eos/user/c/cbasile/ECAL_TB2021/ntuples_templates_v2/plot_results/ --maxchi 200 --cx 2.5 --cy -3 

### 50 GeV

python templates/plot_amplitudes.py -r 15146 -e 50 --path /eos/user/c/cbasile/ECAL_TB2021/ntuples_templates_v2 --minamp 500 --maxamp 2000 --out /eos/user/c/cbasile/ECAL_TB2021/ntuples_templates_v2/plot_results/ --maxchi 1000 --cx 2.5 --cy -3 


### 75 GeV

python templates/plot_amplitudes.py -r 15199 -e 75 --path /eos/user/c/cbasile/ECAL_TB2021/ntuples_templates_v2 --minamp 1000 --maxamp 2500 --out /eos/user/c/cbasile/ECAL_TB2021/ntuples_templates_v2/plot_results/ --maxchi 2500 --cx 0.  --cy -4 

### 100 GeV

python templates/plot_amplitudes.py -r 15153 -e 100 --path /eos/user/c/cbasile/ECAL_TB2021/ntuples_templates_v2 --minamp 1500 --maxamp 3000 --out /eos/user/c/cbasile/ECAL_TB2021/ntuples_templates_v2/plot_results/ --maxchi 2400 --cx 0. --cy -2.5 

### 125 GeV

python templates/plot_amplitudes.py -r 15190 -e 125 --path /eos/user/c/cbasile/ECAL_TB2021/ntuples_templates_v2 --minamp 2000 --maxamp 4000 --out /eos/user/c/cbasile/ECAL_TB2021/ntuples_templates_v2/plot_results/ --maxchi 4000 --cx 2. --cy -3 

### 150 GeV

python templates/plot_amplitudes.py -r 15158 -e 150 --path /eos/user/c/cbasile/ECAL_TB2021/ntuples_templates_v2 --minamp 2000 --maxamp 4500 --out /eos/user/c/cbasile/ECAL_TB2021/ntuples_templates_v2/plot_results/ --maxchi 5000 --cx 2.5 --cy -2.5 


