import ROOT
import argparse
import glob

ROOT.gSystem.Load("/eos/home-c/camendol/H4Analysis/lib/libH4Analysis.so")

parser = argparse.ArgumentParser (description = 'make corrected template')
parser.add_argument('-r', '--run' , help='run to be processed', type = int, default = 15153)
parser.add_argument('--path' , default = '/eos/home-c/camendol/ECALTB/ECAL_TB_Oct2021/ntuples/ECAL_H4_Oct2021_templates/ntuples_templates_v6/')


args = parser.parse_args ()

h4 = ROOT.TChain('h4')
#digi_t = ROOT.TChain('digi_t')
#track_tree = ROOT.TChain('track_tree')

h4.Add(f'{args.path}/{args.run}/*.root')
#digi_t.Add(f'{args.path}/{args.run}/*.root')
#track_tree.Add(f'{args.path}/{args.run}/*.root')

print("loaded chain")

dtime_corr = ROOT.TFile.Open(f"{args.path}/{args.run}/templ/dtime_corr.root","READ")
ftree = dtime_corr.Get("dtime_corr")

h4.AddFriend(ftree)
print("added friend")

selection = "trg == PHYS && digi_t.amp_max[C2_T]>1500 && fit_ampl[MCP1]>120 && digi_t.amp_max[C2_T]<3000"

plots2D = {
    "dtime_corr_vs_trackX": ["dtime_corr:fitResult.x()" ,"60, -20, 20, 60, -.6, .6", selection],
    "dtime_corr_vs_trackY": ["dtime_corr:fitResult.y()" ,"60, -20, 20, 60, -.6, .6", selection], 
    "trackX_vs_trackY": ["fitResult.x():fitResult.y()", "60, -20, 20, 60, -20, 20", selection]
}


c = ROOT.TCanvas("", "", 600, 600)

for key, value in plots2D.items():
    print (key)
    print(f'{value[0]}>>h' + value[1] if len(value[1]) else '')
    h4.Draw(f'{value[0]}>>h' + f'({value[1]})' if len(value[1]) else '', value[2], "goff") 
    print("created")
    h = ROOT.gDirectory.Get("h")
    h.Draw("colz")
    c.SaveAs(f'/eos/home-c/camendol/www/ECALTB2021/templates/{args.run}/{key}.pdf')
    c.SaveAs(f'/eos/home-c/camendol/www/ECALTB2021/templates/{args.run}/{key}.png')
    
