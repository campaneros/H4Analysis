import ROOT
import argparse
import glob

ROOT.gSystem.Load("/eos/home-c/camendol/H4Analysis/lib/libH4Analysis.so")

parser = argparse.ArgumentParser (description = 'make corrected template')
parser.add_argument('-r', '--run' , help='run to be processed', type = int, default = 15153)
parser.add_argument('--prefix' , default = '')
parser.add_argument('--path' , default = '/eos/home-c/camendol/ECALTB/ECAL_TB_Oct2021/ntuples/ECAL_H4_Oct2021/ntuples_c2escan_v1/')

args = parser.parse_args ()
prefix = args.prefix
run = args.run
path = args.path

files = glob.glob(f'{path}/{run}/{prefix}.root')

h4 = ROOT.TChain('h4')
for f in files:
    h4.Add(f)
    print(f'+ Adding file {f}')


h4.Draw('WF_val/amp_max[MCP1]:WF_time - time_max[MCP1]>>tmpl_MCP1(600, -5, 10,  1000, -0.5, 1.1)','WF_ch==MCP1 && amp_max[MCP1]>120', 'goff', 50000)
tmpl_MCP1 = ROOT.gDirectory.Get("tmpl_MCP1")
print("filled MCP1")
h4.Draw('WF_val/amp_max[MCP2]:WF_time - time_max[MCP2]>>tmpl_MCP2(600, -5, 10,  1000, -0.5, 1.1)','WF_ch==MCP2 && amp_max[MCP2]>120', 'goff', 50000)
tmpl_MCP2 = ROOT.gDirectory.Get("tmpl_MCP2")
print("filled MCP2")
h4.Draw('WF_val/amp_max[CLK]:WF_time - time_max[CLK]>>tmpl_CLK(300, -3.2, 4,  1000, -1.1, 1.1)','WF_ch==CLK && Entry$%2==0', 'goff', 50000)
tmpl_CLK = ROOT.gDirectory.Get("tmpl_CLK")
print("filled CLK")



histos = ROOT.TFile.Open(f'{path}/{run}/templ/digitizer_template.root', 'RECREATE')
tmpl_MCP1.SetTitle("")
tmpl_MCP2.SetTitle("")
tmpl_CLK.SetTitle("")
tmpl_MCP1.Write()
tmpl_MCP2.Write()
tmpl_CLK.Write()

histos.Close()
