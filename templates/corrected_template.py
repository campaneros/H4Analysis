import ROOT
import argparse
import glob

ROOT.gSystem.Load("lib/libH4Analysis.so")

parser = argparse.ArgumentParser (description = 'make corrected template')
parser.add_argument('-r', '--run' , help='run to be processed', type = int, default = 15153)
parser.add_argument('--prefix' , default = '')
parser.add_argument('--path' , default = '/eos/user/c/cbasile/ECAL_TB2021/ntuples_templates/')
#/eos/home-c/camendol/ECALTB/ECAL_TB_Oct2021/ntuples/ECAL_H4_Oct2021_templates/ntuples_templates_v5/')
parser.add_argument('--minamp' , type = int, default = 1500)
parser.add_argument('--maxamp' , type = int, default = 3000)

args = parser.parse_args ()
prefix = args.prefix
run = args.run
path = args.path

files = glob.glob(f'{path}/{run}/{prefix}*.root')


h4 = ROOT.TChain('h4')
digi_t = ROOT.TChain('digi_t')
track_tree = ROOT.TChain('track_tree')
hodo1_X = ROOT.TChain('h1X')
hodo1_Y = ROOT.TChain('h1Y')
hodo2_X = ROOT.TChain('h2X')
hodo2_Y = ROOT.TChain('h2Y')
for f in files:
    h4.Add(f)
    digi_t.Add(f)
    track_tree.Add(f)
    hodo1_X.Add(f)
    hodo1_Y.Add(f)
    hodo2_X.Add(f)
    hodo2_Y.Add(f)
    print(f'+ Adding file {f}')

dtime = 'digi_t.time_max[C2_T]-fit_time[MCP1]+fit_time[CLK]-int((digi_t.time_max[C2_T]-fit_time[MCP1]+fit_time[CLK])/6.238)*6.238'
phase = 'digi_t.time_max[C2_T]-int(digi_t.time_max[C2_T]/6.238)*6.238'

fcorr = ROOT.TFile.Open(f'{path}/{run}/templ/phase_correction.root', 'READ')
corr = fcorr.Get('dtime_phase_1');


tmpl_corr = ROOT.TH2F('tmpl_corr', '', 5000, 120, 230,  1000, -0.1, 1.1);
tmpl = ROOT.TH2F('tmpl', '', 5000, 120, 230,  1000, -0.1, 1.1);


nentries = h4.GetEntries()
for e in range(nentries):
    h4.GetEntry(e)
    digi_t.GetEntry(e)
    if e % 1000 == 0: print (f'{e} / {nentries}')
    h4.Draw(f'{dtime}:{phase}: fabs(h1X.clusters.X_) < 5 && fabs(h1Y.clusters.Y_) < 5 && fabs(h2X.clusters.X_) < 5 && fabs(h2Y.clusters.Y_) < 5 && digi_t.amp_max[C2_T]>{args.minamp} && fit_ampl[MCP1]>80 && digi_t.amp_max[C2_T]<{args.maxamp}','','goff', 1, e)
	#n_tracks==1 && fabs(track_tree.fitResult.x()-5)<4 && fabs(track_tree.fitResult.y()-5)<4 (removed: may create bad templates) 
    dtime = h4.GetVal(0)[0]
    phase = h4.GetVal(1)[0]
    selection = h4.GetVal(2)[0]
    if selection == 1:
        n = h4.Draw('WF_val:WF_time>>h','WF_ch==C2', 'goff', 1, e)
        WF_val = h4.GetVal(0)
        WF_time = h4.GetVal(1)
        for i in range (25, 55):
            if h4.amp_max[h4.C2_T] < 1e-9: continue
            tmpl_corr.Fill(WF_time[i]-(digi_t.time_max[h4.C2_T]-corr.GetBinContent(corr.FindBin(digi_t.time_max[h4.C2_T]-int(digi_t.time_max[h4.C2_T]/6.238)*6.238))), WF_val[i]/digi_t.amp_max[h4.C2_T]) 
            tmpl.Fill(WF_time[i], WF_val[i]/digi_t.amp_max[h4.C2_T]) 

histos = ROOT.TFile.Open(f'{path}/{run}/templ/corrected_template_{prefix}.root', 'RECREATE')
print(f'Saved file : {path}/{run}/templ/corrected_template_{prefix}.root')
tmpl.Write()
tmpl_corr.Write()
histos.Close()
