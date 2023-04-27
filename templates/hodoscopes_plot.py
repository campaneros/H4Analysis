import ROOT
from ctypes import *
import argparse
import glob

ROOT.gSystem.Load("lib/libH4Analysis.so")
ROOT.gROOT.SetBatch(True)

parser = argparse.ArgumentParser (description = 'make plots from hodoscopes 1 and 2')
parser.add_argument('-r', '--run' , help='run to be processed', type = int, default = 15153)
parser.add_argument('--path' , default = '/eos/user/c/cbasile/ECAL_TB2021/ntuples_templates/ntuples_v1')
parser.add_argument('--outdir' , default = '/eos/user/c/cbasile/ECAL_TB2021/ntuples_templates/ntuples_v1')
parser.add_argument('--crystal' , default = 'C2')
parser.add_argument('--energy' , default = 100, type = int)
parser.add_argument('--hcx' , default = 0., type = float)
parser.add_argument('--hcy' , default = 0., type = float)
parser.add_argument('--tcx' , default = 0., type = float)
parser.add_argument('--tcy' , default = 0., type = float)

args = parser.parse_args ()
run = args.run
path = args.path
outdir = args.outdir 

h4 = ROOT.TChain('h4')
nfiles = h4.Add(f'{path}/{run}/*.root')
print(f' + Added {nfiles} files')

h4.Draw('amp_max[C2]:h1Y.clusters.Y_:h1X.clusters.X_>>hodo1(40, -20, 20, 40, -20, 20,0, 5000)', ' n_tracks == 1', 'PROFCOLZ')
h_hodo1 = ROOT.gPad.GetPrimitive("hodo1")
h1_area = ROOT.TBox(args.hcx-5, args.hcy-5, args.hcx+5, args.hcy+5)

h4.Draw('amp_max[C2]:h2Y.clusters.Y_:h2X.clusters.X_>>hodo2(40, -20, 20, 40, -20, 20,0, 5000)', 'n_tracks == 1', 'PROFCOLZ')
h_hodo2 = ROOT.gPad.GetPrimitive("hodo2")

h4.Draw('amp_max[C2]:Y:X>>tracks(40, -20, 20, 40, -20, 20,0, 5000)', ' n_tracks == 1', 'PROFCOLZ')
h_tracks= ROOT.gPad.GetPrimitive("tracks")
#projX = h_tracks.ProfileX('projX')
#projY = h_tracks.ProfileY('projY')
xmean = args.tcx #projX.GetBinCenter(projX.GetMaximumBin())
ymean = args.tcy #projY.GetBinCenter(projY.GetMaximumBin())
print(f' = track <X> = {xmean} mm <Y> = {ymean} mm')
grmax= ROOT.TH1F('gr_%s_%s'%(args.crystal,args.energy),'gr_%s_%s'%(args.crystal,args.energy),1,xmean-1,xmean+1)
grmax.SetBinContent(1,ymean)
trk_area = ROOT.TBox(xmean-5, ymean-5, xmean+5, ymean+5)

c = ROOT.TCanvas("c", "", 1600, 800)
ROOT.gStyle.SetOptStat(0)

margin = 0.14
c.Divide(2,1)
c.cd(1)
ROOT.gPad.SetMargin(margin, margin, margin, margin)
h_hodo1.GetXaxis().SetTitle("X (mm)")
h_hodo1.GetYaxis().SetTitle("Y (mm)")
h_hodo1.SetTitle("HODOSCOPE 1")
h_hodo1.Draw("PROFCOLZ0")
h1_area.SetLineColor(ROOT.kRed)
h1_area.SetFillStyle(0)
h1_area.Draw("same")
c.cd(2)
ROOT.gPad.SetMargin(margin, margin, margin, margin)
h_hodo2.GetXaxis().SetTitle("X (mm)")
h_hodo2.GetYaxis().SetTitle("Y (mm)")
h_hodo2.SetTitle("HODOSCOPE 2")
h_hodo2.Draw("PROFCOLZ0")
c.SaveAs(outdir+'/AmpHodo_%s_%dGeV.png'%(args.crystal,args.energy))

c2 = ROOT.TCanvas("c2", "", 1024, 1024)
ROOT.gPad.SetMargin(margin, margin, margin, margin)
h_tracks.GetXaxis().SetTitle("X (mm)")
h_tracks.GetYaxis().SetTitle("Y (mm)")
h_tracks.SetTitle("TRACKS")
h_tracks.Draw("PROFCOLZ0")
grmax.SetMarkerColor(ROOT.kRed)
grmax.SetMarkerStyle(34)
grmax.SetMarkerSize(3)
grmax.Draw("LPsame")
trk_area.SetLineColor(ROOT.kRed)
trk_area.SetFillStyle(0)
trk_area.Draw("same")
c2.SaveAs(outdir+'/AmpTracks_%s_%dGeV.png'%(args.crystal,args.energy))
