import ROOT
import argparse
import glob

ROOT.gSystem.Load("lib/libH4Analysis.so")
ROOT.gROOT.SetBatch(True)

parser = argparse.ArgumentParser (description = 'merge root files with corrected template')
parser.add_argument('-r', '--run' , help='run to be processed', type = int, default = 15153)
parser.add_argument('-e', '--energy' , help='energy of the run', type = int, default = 100)
parser.add_argument('--prefix' , default = '')
parser.add_argument('--path' , default = '/eos/user/c/cbasile/ECAL_TB2021/ntuples_templates_v0')
parser.add_argument('--out' , default = '/eos/user/c/cbasile/ECAL_TB2021/ntuples_templates_v0/plot_results')
parser.add_argument('--minamp' , type = int, default = 1500)
parser.add_argument('--maxamp' , type = int, default = 3000)
parser.add_argument('--maxchi' , type = int, default = 10000)
parser.add_argument('--cx' , type = float, default =  0.0)
parser.add_argument('--cy' , type = float, default = -2.5)

args = parser.parse_args ()
path = args.path
out = args.out
run = args.run
E = args.energy
Amin = args.minamp
Amax = args.maxamp

ROOT.gStyle.SetOptStat(0)
binWidth = 30 # ADC counts
Nbins = (args.maxamp-args.minamp)/binWidth
amps = ROOT.TH1F(f'amps_{E}', "", int(Nbins), Amin, Amax)
amps.SetTitle(f'{E} GeV')
amps.GetXaxis().SetTitle("ADC counts")
amps.GetYaxis().SetTitle(f'entries/{amps.GetXaxis().GetBinWidth(10)} ADC')

h4 = ROOT.TChain('h4')
h4.Add(f'{path}/{run}/*.root')
#hodo1_X = ROOT.TChain('h1X')
#hodo1_X.Add(f'{path}/{run}/*.root')
#hodo1_Y = ROOT.TChain('h1Y')
#hodo1_Y.Add(f'{path}/{run}/*.root')
#
nentries = h4.GetEntries()
print(f'... {nentries} events to be processed')

h4.Draw(f'fit_ampl[C2]>>amps_{E}', f'trg==PHYS && fit_chi2[C2] < {args.maxchi} && fit_ampl[MCP1]> 200 && fabs(X- {args.cx}) < 4 && fabs(Y- {args.cy}) < 4', 'goff')


outFile = ROOT.TFile(f'{out}/amp_{E}.root', "RECREATE")
print(f'... OUTPUT saved in {out}/amp_{E}.root')
amps.Write()
outFile.Close()

c = ROOT.TCanvas("c", "", 1024, 1024)
amps.SetLineWidth(2)
amps.Draw()
c.SaveAs(f'/eos/user/c/cbasile/www/ECAL_TB2021/Linearity/{E}GeV/FitAmplCuts_{run}_{E}GeV.png')
