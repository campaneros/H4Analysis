import ROOT
import argparse
import glob

ROOT.gSystem.Load("lib/libH4Analysis.so")

parser = argparse.ArgumentParser (description = 'merge root files with corrected template')
parser.add_argument('-r', '--run' , help='run to be processed', type = int, default = 15153)
parser.add_argument('-e', '--energy' , help='beam energy', type = int, default = 15153)
parser.add_argument('--prefix' , default = '')
parser.add_argument('--path' , default = '/eos/user/c/cbasile/ECAL_TB2021/ntuples_templates/ntuples_v1')
parser.add_argument('--out' , default = '/eos/user/c/cbasile/ECAL_TB2021/ntuples_templates_v0/plot_results/')

args = parser.parse_args ()
path = args.path
out = args.out
energy = args.energy

path_to_file = f'{path}/{args.run}/templ/corrected_template.root'
path_to_out = f'{out}/template_smooth_{energy}.root'

templ_file = ROOT.TFile(path_to_file, "READ")
tmpl_corr = templ_file.Get("tmpl_corr_smooth")
tmpl_corr.SetName(f'tmpl_corr_smooth_{energy}GeV')

out_file = ROOT.TFile(path_to_out, "RECREATE")
out_file.cd()
tmpl_corr.Write()
out_file.Close()

templ_file.Close()
