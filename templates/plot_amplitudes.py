import ROOT
import argparse
import glob

ROOT.gSystem.Load("lib/libH4Analysis.so")

parser = argparse.ArgumentParser (description = 'merge root files with corrected template')
parser.add_argument('-r', '--run' , help='run to be processed', type = int, default = 15153)
parser.add_argument('-e', '--energy' , help='energy of the run', type = int, default = 100)
parser.add_argument('--prefix' , default = '')
parser.add_argument('--path' , default = '/eos/user/c/cbasile/ECAL_TB2021/ntuples_templates_v0')
parser.add_argument('--out' , default = '/eos/user/c/cbasile/ECAL_TB2021/ntuples_templates_v0/plot_results')
parser.add_argument('--minamp' , type = int, default = 1500)
parser.add_argument('--maxamp' , type = int, default = 3000)
parser.add_argument('--maxchi' , type = int, default = 10000)
parser.add_argument('--cx' , type = float, default = 0.0)
parser.add_argument('--cy' , type = float, default = -5.0)

args = parser.parse_args ()
path = args.path
out = args.out
run = args.run
E = args.energy
Amin = args.minamp
Amax = args.maxamp

ROOT.gStyle.SetOptStat(0)
amps = ROOT.TH1F(f'amps_{E}', "", 100, Amin, Amax)
amps.SetTitle(f'{E} GeV')
amps.GetXaxis().SetTitle("ADC counts")
amps.GetYaxis().SetTitle(f'entries/{amps.GetXaxis().GetBinWidth(10)} ADC')

h4 = ROOT.TChain('h4')
h4.Add(f'{path}/{run}/*.root')
hodo1_X = ROOT.TChain('h1X')
hodo1_X.Add(f'{path}/{run}/*.root')
hodo1_Y = ROOT.TChain('h1Y')
hodo1_Y.Add(f'{path}/{run}/*.root')

nentries = h4.GetEntries()
Nsaturated = 0
print(f'... {nentries} events to be processed')
for e in range(nentries):
    #if (e > 10000): break
    h4.GetEntry(e)
    hodo1_X.GetEntry(e)
    hodo1_Y.GetEntry(e)
    n = h4.Draw('WF_val:WF_time>>h','WF_ch==C2', 'goff', 1, e)
    #print(f' nWF = {n}')
    if( n > 90 ): 
        Nsaturated += 1
        continue

    n = h4.Draw(f'fit_ampl[C2]', f'trg==PHYS&&amp_max[C2] > {Amin} && amp_max[C2]<{Amax} && fit_ampl[MCP1]>150 && fabs(h1X.clusters.X_- {args.cx}) && fabs(h1Y.clusters.Y_- {args.cy})', 'goff',1,e)
    if(n < 1): continue 
    fit_ampl = h4.GetVal(0)[0]
    #print(f' N = {n} Afit = {fit_ampl}')
    amps.Fill(fit_ampl)

Nsaturated = float(Nsaturated)/nentries
print(f' = fraction of saturated events {Nsaturated}')
outFile = ROOT.TFile(f'{out}/amp_{E}.root', "RECREATE")
print(f'... OUTPUT saved in {out}/amp_{E}.root')
amps.Write()
outFile.Close()
