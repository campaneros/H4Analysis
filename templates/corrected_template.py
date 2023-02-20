import ROOT
import argparse
import glob
import numpy

ROOT.gSystem.Load("lib/libH4Analysis.so")

parser = argparse.ArgumentParser (description = 'make corrected template')
parser.add_argument('-r', '--run' , help='run to be processed', type = int, default = 15153)
parser.add_argument('--prefix' , default = '')
parser.add_argument('--path' , default = '/eos/user/c/cbasile/ECAL_TB2021/ntuples_templates/')
#/eos/home-c/camendol/ECALTB/ECAL_TB_Oct2021/ntuples/ECAL_H4_Oct2021_templates/ntuples_templates_v5/')
parser.add_argument('--minamp' , type = int, default = 1500)
parser.add_argument('--maxamp' , type = int, default = 3000)
parser.add_argument('--cx' , type = float, default =  0.0)
parser.add_argument('--cy' , type = float, default = -5.0)

args = parser.parse_args ()
prefix = args.prefix
run = args.run
path = args.path
Cx = args.cx
Cy = args.cy

files = glob.glob(f'{path}/{run}/{prefix}*.root')


h4 = ROOT.TChain('h4')
digi_t = ROOT.TChain('digi_t')
digi= ROOT.TChain('digi')
track_tree = ROOT.TChain('track_tree')
hodo1_X = ROOT.TChain('h1X')
hodo1_Y = ROOT.TChain('h1Y')
hodo2_X = ROOT.TChain('h2X')
hodo2_Y = ROOT.TChain('h2Y')
for f in files:
    h4.Add(f)
    digi_t.Add(f)
    digi.Add(f)
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
print(f'... {nentries} events to be processed')
Nsaturated = 0
for e in range(nentries):
    h4.GetEntry(e)
    digi_t.GetEntry(e)
    digi.GetEntry(e)
    hodo1_X.GetEntry(e)
    hodo1_Y.GetEntry(e)
    if e % 1000 == 0: print (f'{e} / {nentries}')

    N = h4.Draw(f'{dtime}:{phase}: trg ==PHYS && fabs(h1X.clusters.X_- {Cx}) < 5 && fabs(h1Y.clusters.Y_ - {Cy} ) < 5  && digi_t.amp_max[C2_T]>{args.minamp} && fit_ampl[MCP1]>120&& digi_t.amp_max[C2_T]<{args.maxamp}','','goff', 1, e)
    
    dtime = h4.GetVal(0)[0]
    phase = h4.GetVal(1)[0]
    selection = h4.GetVal(2)[0]

    #if selection == 1:
    if N > 0 :
        print(N)
        n = h4.Draw('WF_val:WF_time>>h','WF_ch==C2', 'goff', 1, e)
        if( n > 90 ):
            Nsaturated += 1
            continue
        WF_val = h4.GetVal(0)
        WF_time = h4.GetVal(1)
        noZeros = True 
        max_time = digi.time_max[h4.C2]-(digi_t.time_max[h4.C2_T]-corr.GetBinContent(corr.FindBin(digi_t.time_max[h4.C2_T]-int(digi_t.time_max[h4.C2_T]/6.238)*6.238)))
        if (max_time <155 or max_time > 170): noZeros = False 

        if (noZeros):
            #print(f'{e} max time {max_time} ampl {digi.amp_max[h4.C2]}')
            #print(f'{e} templ max time {max_t_time} ampl {digi_t.amp_max[h4.C2_T]}')
            for i in range (25, 55):
                if h4.amp_max[h4.C2_T] < 1e-9: continue
                corr_time = WF_time[i]-(digi_t.time_max[h4.C2_T]-corr.GetBinContent(corr.FindBin(digi_t.time_max[h4.C2_T]-int(digi_t.time_max[h4.C2_T]/6.238)*6.238)))
                ampl = WF_val[i]#/digi_t.amp_max[h4.C2_T]
                print(f't = {corr_time}  A = {ampl}')
                tmpl_corr.Fill(WF_time[i]-(digi_t.time_max[h4.C2_T]-corr.GetBinContent(corr.FindBin(digi_t.time_max[h4.C2_T]-int(digi_t.time_max[h4.C2_T]/6.238)*6.238))), WF_val[i]/digi_t.amp_max[h4.C2_T])
                tmpl.Fill(WF_time[i], WF_val[i]/digi_t.amp_max[h4.C2_T]) 
Nsaturated = float(Nsaturated)/nentries
print(f' ... number of saturated events {Nsaturated}')
histos = ROOT.TFile.Open(f'{path}/{run}/templ/corrected_template_{prefix}.root', 'RECREATE')
print(f'Saved file : {path}/{run}/templ/corrected_template_{prefix}.root')
tmpl.Write()
tmpl_corr.Write()
histos.Close()
