import ROOT
import argparse
import glob

ROOT.gSystem.Load("lib/libH4Analysis.so")
ROOT.gROOT.SetBatch(True)

parser = argparse.ArgumentParser (description = 'make plots from hodoscopes 1 and 2')
parser.add_argument('-r', '--run' , help='run to be processed', type = int, default = 15153)
parser.add_argument('--path' , default = '/eos/user/c/cbasile/ECAL_TB2021/ntuples_templates/ntuples_v1')
parser.add_argument('--outdir' , default = '/eos/user/c/cbasile/ECAL_TB2021/ntuples_templates/ntuples_v1')

args = parser.parse_args ()
run = args.run
path = args.path
outdir = args.outdir 

files = glob.glob(f'{path}/{run}/*.root')

hodo1_X = ROOT.TChain('h1X')
hodo1_Y = ROOT.TChain('h1Y')
hodo2_X = ROOT.TChain('h2X')
hodo2_Y = ROOT.TChain('h2Y')

for f in files:
    hodo1_X.Add(f)
    hodo1_Y.Add(f)
    hodo2_X.Add(f)
    hodo2_Y.Add(f)
    print(f'+ Adding file {f}')
hodo1_X.AddFriend(hodo1_Y)
hodo2_X.AddFriend(hodo2_Y)
h_hodo1_X = ROOT.TH1F("h_hodo1_X", "HODO1 X", 30, -15, 15)
h_hodo1_Y = ROOT.TH1F("h_hodo1_Y", "HODO1 Y", 30, -15, 15)
h_hodo2_X = ROOT.TH1F("h_hodo2_X", "HODO2 X", 30, -15, 15)
h_hodo2_Y = ROOT.TH1F("h_hodo2_Y", "HODO2 Y", 30, -15, 15)
h_hodo1 = ROOT.TH2F("h_hodo1", "HODO 1", 30, -15, 15, 30, -15, 15)
h_hodo2 = ROOT.TH2F("h_hodo2", "HODO 2", 30, -15, 15, 30, -15, 15)


hodo1_X.Draw('clusters.X_>>h_hodo1_X', '', 'goff')
hodo1_Y.Draw('clusters.Y_>>h_hodo1_Y', '', 'goff')
hodo2_X.Draw('clusters.X_>>h_hodo2_X', '', 'goff')
hodo2_Y.Draw('clusters.Y_>>h_hodo2_Y', '', 'goff')

hodo1_X.Draw('clusters.X_:h1Y.clusters.Y_>>h_hodo1', '', 'goff')
hodo2_X.Draw('clusters.X_:h2Y.clusters.Y_>>h_hodo2', '', 'goff')
c = ROOT.TCanvas("c", "", 1024, 512)
ROOT.gStyle.SetOptStat(0)

c.Divide(2,1)
c.cd(1)
h_hodo1.Draw('COLZ')
c.cd(2)
h_hodo2.Draw('COLZ')
c.SaveAs(outdir+'/Hodoscopes2D.png')

c2 = ROOT.TCanvas("c2", "", 1024, 1024)
c2.Divide(2,2)
c2.cd(1)
h_hodo1_X.Draw()
c2.cd(2)
h_hodo1_Y.Draw()
c2.cd(3)
h_hodo2_X.Draw()
c2.cd(4)
h_hodo2_Y.Draw()
c2.SaveAs(outdir+'/Hodoscopes1D.png')
