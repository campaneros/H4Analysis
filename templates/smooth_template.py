import ROOT
import argparse

parser = argparse.ArgumentParser (description = 'get smooth template')
parser.add_argument('-r', '--run' , help='run to be processed', type = int, default = 15153)
parser.add_argument('--path' , default = '/eos/user/c/cbasile/ECAL_TB2021/ntuples_templates/ntuples_v0')
#/eos/home-c/camendol/ECALTB/ECAL_TB_Oct2021/ntuples/ECAL_H4_Oct2021/ntuples_c2escan_v2//')
parser.add_argument('--fname' , default = 'corrected_template')
parser.add_argument('--hname' , default = 'tmpl') # histogram

args = parser.parse_args()

fname = args.fname.replace('.root', '')
hname = args.hname
f = ROOT.TFile.Open(f"{args.path}/{args.run}/templ/{fname}.root", "UPDATE")

tmpl= f.Get(args.hname)
print(type(tmpl))
smooth_tmpl = tmpl.ProjectionX()
n_rebin = 4
smooth_tmpl.Rebin(n_rebin)
for ibin in range(1, tmpl.GetNbinsX(), n_rebin):
    thisbin = tmpl.ProjectionY("thisbin", ibin, ibin+n_rebin)
    thisbin.SetAxisRange(thisbin.GetMean()-1*thisbin.GetRMS(), thisbin.GetMean()+1*thisbin.GetRMS())
    smooth_tmpl.SetBinContent(int(ibin/n_rebin)+1, thisbin.GetMean())
    #print (ibin, thisbin.GetMean())

smooth_tmpl.SetDirectory(f)
if (hname+"_smooth" in ROOT.gDirectory.GetListOfKeys()): ROOT.gDirectory.Delete(hname+"_smooth*");
smooth_tmpl.SetName(hname+"_smooth")
smooth_tmpl.SetTitle("")
smooth_tmpl.Write()
f.Close()
