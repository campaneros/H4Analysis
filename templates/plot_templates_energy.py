import ROOT
import argparse
import glob

ROOT.gSystem.Load("lib/libH4Analysis.so")

parser = argparse.ArgumentParser (description = 'merge root files with corrected template')
#parser.add_argument('-r', '--run' , help='run to be processed', type = int, default = 15153)
parser.add_argument('--prefix' , default = '')
parser.add_argument('--path' , default = '/eos/user/c/cbasile/ECAL_TB2021/ntuples_templates/ntuples_v1')

args = parser.parse_args ()
path = args.path


h_50  = ROOT.TH1F('h_50', '', 2500, 120, 230)
h_100 = ROOT.TH1F('h_100', '', 2500, 120, 230)
h_150 = ROOT.TH1F('h_150', '', 2500, 120, 230)

runs = {
   "50 GeV" : 15146,
  "100 GeV" : 15153,
#  "150 GeV" : 15158
}
Ecolors = {
  "50 GeV" : 5, #yellow
 "100 GeV" : 2,  #red
 "150 GeV" : 3  #verde
}
Ehist = {
  "50 GeV" : h_50,
 "100 GeV" : h_100,
 "150 GeV" : h_150
}
print(runs.values())
print(Ecolors.values())

tmpl_smooth = ROOT.THStack("templates", "") #ROOT.TH1F('tmpl_smooth', '', 5000, 120, 230)
ROOT.gStyle.SetOptStat(0)
legend = ROOT.TLegend(0.75, 0.75, 0.89,0.89)
legend.SetBorderSize(0)

h4 = ROOT.TChain('h4')
for e in runs.keys() :
    h4.Add(f'{path}/{runs[e]}/*.root')
    templFile = ROOT.TFile.Open(f'{path}/{runs[e]}/templ/corrected_template.root')
    print(f' ... reading file {templFile.GetName()}')
    Ehist[e] = templFile.Get('tmpl_corr_smooth').Clone()
    templFile.Close()
    print(type(Ehist[e]))
    Ehist[e].SetLineColor(Ecolors[e])
    tmpl_smooth.Add(Ehist[e])
    legend.AddEntry(Ehist[e], f'E = '+e)

c = ROOT.TCanvas("c", "", 1024, 1024)
c.cd()
tmpl_smooth.Draw()
legend.Draw()
c.SaveAs(f'/eos/user/c/cbasile/www/ECAL_TB2021/my_templates/tempaltes_vs_energy.png')
#c.SaveAs(f'/eos/user/c/cbasile/www/ECAL_TB2021/my_templates/tempaltes_vs_energy.pdf')
