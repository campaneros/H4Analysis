import ROOT
import argparse

ROOT.gSystem.Load("lib/libH4Analysis.so")
ROOT.gROOT.SetBatch(True)

parser = argparse.ArgumentParser (description = 'make corrected template')
#parser.add_argument('-r', '--run' , help='run to be processed', type = int, default = 15153)
parser.add_argument('--path' , default = '/eos/user/c/cbasile/ECAL_TB2021/ntuples_templates_v0/plot_results/')


args = parser.parse_args ()

energies = {'25 GeV' : '25','50 GeV' : '50', '75 GeV' : 75, '100 GeV': 100, '125 GeV': 125, '150 GeV': '150'}
e_colors = {'25 GeV' :  94 ,'50 GeV' :   4, '75 GeV' :  7, '100 GeV':   2, '125 GeV':   6, '150 GeV': 3}

inFile = ROOT.TFile(f'{args.path}/template_smooth.root', "READ" )

legend = ROOT.TLegend(0.65,0.60, 0.89,0.89)
legend.SetBorderSize(0)

Stk_tmpl = ROOT.THStack("Stk_peak", "")
Stk_peak = ROOT.THStack("Stk_peak", "")
Stk_raise = ROOT.THStack("Stk_raise", "")
Stk_tail = ROOT.THStack("Stk_tail", "")
Stk_ratio = ROOT.THStack("Stk_ratio", "")
h_reference = inFile.Get(f'tmpl_corr_smooth_100GeV')
c = ROOT.TCanvas('c', '', 2048, 1536)
c.Divide(2,2)
c_ratio = ROOT.TCanvas('c_ratio', '', 800, 1024)
up_pad = ROOT.TPad("up_pad", "", 0., 0.30, 1.,1.) 
up_pad.SetBottomMargin(0)
up_pad.Draw()

ROOT.gStyle.SetOptStat(0)

for e in energies.keys():
    h = inFile.Get(f'tmpl_corr_smooth_{energies[e]}GeV')
    h.SetLineColor(e_colors[e])
    h.SetLineWidth(2)
    legend.AddEntry(h, f'{e}')
    Stk_tmpl.Add(h)
    h_zoom = h.Clone("h_zoom")
    Stk_peak.Add(h_zoom)
    Stk_raise.Add(h_zoom)
    Stk_tail.Add(h_zoom)
    h_ratio = h.Clone("h_ratio")
    h_ratio.Divide(h_reference)
    Stk_ratio.Add(h_ratio)
    #c.cd(1)
    #h.Draw('same')
    #up_pad.cd()
    #h.Draw('same')

c.cd(1)
Stk_tmpl.Draw("nostack")
legend.Draw()
c.cd(2)
Stk_peak.Draw("nostack")
Stk_peak.GetXaxis().SetRangeUser(158, 166)
Stk_peak.SetMinimum(0.85)
c.cd(3)
Stk_raise.Draw("nostack")
Stk_raise.GetXaxis().SetRangeUser(140, 150)
Stk_raise.SetMaximum(0.1)
c.cd(4)
Stk_tail.Draw("nostack")
Stk_tail.GetXaxis().SetRangeUser(180, 220)
Stk_tail.SetMaximum(0.02)
c.SaveAs('/eos/user/c/cbasile/www/ECAL_TB2021/Linearity/compare_templates.png')
c.SaveAs('/eos/user/c/cbasile/www/ECAL_TB2021/Linearity/compare_templates.pdf')

up_pad.cd()
Stk_tmpl.Draw("nostack")
Stk_tmpl.GetXaxis().SetRangeUser(150, 180)
legend.Draw()
c_ratio.cd()
ratio_pad = ROOT.TPad("ratio_pad", "",0., 0., 1.,0.30)
ratio_pad.SetBottomMargin(0.4)
ratio_pad.SetTopMargin(0)
ratio_pad.Draw()
ratio_pad.cd()
Stk_ratio.Draw('nostack')
Stk_ratio.SetMaximum(1.1)
Stk_ratio.SetMinimum(0.9)
Stk_ratio.GetXaxis().SetRangeUser(150, 180)
c_ratio.SaveAs('/eos/user/c/cbasile/www/ECAL_TB2021/Linearity/compare_templates_ratio.png')
c_ratio.SaveAs('/eos/user/c/cbasile/www/ECAL_TB2021/Linearity/compare_templates_ratio.pdf')

#c.SetLogy(1)
#c.SaveAs('/eos/user/c/cbasile/www/ECAL_TB2021/Linearity/compare_templates_log.png')
#c.SaveAs('/eos/user/c/cbasile/www/ECAL_TB2021/Linearity/compare_templates_log.pdf')

    
