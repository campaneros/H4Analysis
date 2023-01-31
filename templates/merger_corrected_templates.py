import ROOT
import argparse
import glob

ROOT.gSystem.Load("lib/libH4Analysis.so")

parser = argparse.ArgumentParser (description = 'merge root files with corrected template')
parser.add_argument('-r', '--run' , help='run to be processed', type = int, default = 15153)
parser.add_argument('--prefix' , default = '')
parser.add_argument('--path' , default = '/eos/user/c/cbasile/ECAL_TB2021/ntuples_templates/ntuples_v1')

args = parser.parse_args ()
run = args.run
path = args.path


files = glob.glob(f'{path}/{run}/templ/corrected_template_*.root')
tmpl = ROOT.TH2F('tmpl', '', 5000, 120, 230,  1000, -0.1, 1.1)
tmpl_corr = ROOT.TH2F('tmpl_corr', '', 5000, 120, 230,  1000, -0.1, 1.1)
for file in files:
    rootFile = ROOT.TFile.Open(file)
    tmpl.Add(rootFile.Get("tmpl"))
    tmpl_corr.Add(rootFile.Get("tmpl_corr"))
    print(f'... added file {file}')
    rootFile.Close()
print(f' ---> Total number of entries {tmpl_corr.GetEntries()}')

outfile = ROOT.TFile(f'{path}/{run}/templ/corrected_template.root', "RECREATE")
outfile.cd()
tmpl.Write()
tmpl_corr.Write()
outfile.Close()

print(f'Output saved in {outfile.GetName()}')
