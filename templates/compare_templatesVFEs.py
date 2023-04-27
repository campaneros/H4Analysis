import ROOT
import argparse

ROOT.gSystem.Load("lib/libH4Analysis.so")
ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetLineWidth(2)
ROOT.gStyle.SetPadTickX(1)
ROOT.gStyle.SetPadTickY(1)

parser = argparse.ArgumentParser (description = 'make corrected template')
#parser.add_argument('-r', '--run' , help='run to be processed', type = int, default = 15153)
parser.add_argument('--path' , default = '/eos/user/c/cbasile/ECAL_TB2021/ntuples_templates_v2/plot_results/')


args = parser.parse_args ()

crystal  = {'A3' : 15007, 'B3': 14989, 'C2': 14982, 'D4': 14985, 'E4': 15003}
c_colors = {'A3' :  94 , 'B3' :   4, 'C2' :  7, 'D4':   2, 'E4':   8}

inFile = ROOT.TFile(f'{args.path}/template_smooth_VFEs.root', "READ" )

legend = ROOT.TLegend(0.70,0.55, 0.89,0.89)
legend.SetBorderSize(0)

Stk_tmpl = ROOT.THStack("Stk_peak", "")
Stk_peak = ROOT.THStack("Stk_peak", "")
Stk_raise = ROOT.THStack("Stk_raise", "")
Stk_tail = ROOT.THStack("Stk_tail", "")
Stk_ratio = ROOT.THStack("Stk_ratio", "")
h_reference = inFile.Get(f'tmpl_corr_smooth_100GeV_C2_HP')
c = ROOT.TCanvas('c', '', 2048, 1536)
c.Divide(2,2)
c_ratio = ROOT.TCanvas('c_ratio', '', 800, 1024)
up_pad = ROOT.TPad("up_pad", "", 0., 0.30, 1.,1.) 
up_pad.SetBottomMargin(0.01)
up_pad.SetGrid()
up_pad.Draw()

### ECAL text
ECALtex = ROOT.TLatex()
ECALtex.SetTextFont(42)
ECALtex.SetTextAngle(0)
ECALtex.SetTextColor(ROOT.kBlack)    
ECALtex.SetTextSize(0.05)    
ECALtex.SetTextAlign(12)



for e in crystal.keys():
    h = inFile.Get(f'tmpl_corr_smooth_100GeV_{e}_HP')
    print(f'+ tmpl_corr_smooth_100GeV_{e}_HP')
    h.SetLineColor(c_colors[e])
    h.SetLineWidth(3)
    legend.AddEntry(h, f'{e}')
    Stk_tmpl.Add(h)
    h_zoom = h.Clone("h_zoom")
    Stk_peak.Add(h_zoom)
    Stk_raise.Add(h_zoom)
    Stk_tail.Add(h_zoom)
    h_ratio = h.Clone("h_ratio")
    h_ratio.Divide(h_reference)
    Stk_ratio.Add(h_ratio)

c.cd(1)
Stk_tmpl.Draw("nostack")
Stk_tmpl.GetXaxis().SetTitle("time [ns]"); Stk_tmpl.GetXaxis().SetTitleSize(0.05) 
Stk_tmpl.GetYaxis().SetTitle("a.u."); Stk_tmpl.GetYaxis().SetTitleSize(0.05) 
legend.Draw()
c.cd(2)
Stk_peak.Draw("nostack")
Stk_peak.GetXaxis().SetRangeUser(158, 166)
Stk_peak.SetMinimum(0.85)
Stk_peak.GetXaxis().SetTitle("time [ns]");Stk_peak.GetXaxis().SetTitleSize(0.05) 
Stk_peak.GetYaxis().SetTitle("a.u."); Stk_peak.GetYaxis().SetTitleSize(0.05); Stk_peak.GetYaxis().SetTitleOffset(1.) 
c.cd(3)
Stk_raise.Draw("nostack")
Stk_raise.GetXaxis().SetRangeUser(140, 150)
Stk_raise.SetMaximum(0.1)
Stk_raise.GetXaxis().SetTitle("time [ns]"); Stk_raise.GetXaxis().SetTitleSize(0.05) 
Stk_raise.GetYaxis().SetTitle("a.u."); Stk_raise.GetYaxis().SetTitleSize(0.05); Stk_raise.GetYaxis().SetTitleOffset(1.) 
c.cd(4)
Stk_tail.Draw("nostack")
Stk_tail.GetXaxis().SetRangeUser(180, 220)
Stk_tail.SetMaximum(0.02)
Stk_tail.GetXaxis().SetTitle("time [ns]"); Stk_tail.GetXaxis().SetTitleSize(0.05)
Stk_tail.GetYaxis().SetTitle("a.u."); Stk_tail.GetYaxis().SetTitleSize(0.05) ; Stk_tail.GetYaxis().SetTitleOffset(1.) 
c.SaveAs('/eos/user/c/cbasile/www/ECAL_TB2021/HighPurity/VFEs_scan/compare_templates.png');
c.SaveAs('/eos/user/c/cbasile/www/ECAL_TB2021/HighPurity/VFEs_scan/compare_templates.pdf');

up_pad.cd()
up_pad.SetBottomMargin(0.02)
Stk_tmpl.Draw("nostack")
Stk_tmpl.SetMaximum(1.2)
Stk_tmpl.SetMinimum(0)
Stk_tmpl.GetXaxis().SetRangeUser(150, 180)
Stk_tmpl.GetXaxis().SetLabelSize(0)
Stk_tmpl.GetYaxis().SetTitle("a.u."); Stk_tmpl.GetYaxis().SetTitleOffset(0.8); Stk_tmpl.GetYaxis().SetTitleSize(0.06)
Stk_tmpl.GetYaxis().SetLabelSize(0.04); 
legend.Draw()
ECALtex.DrawLatex(151,1.1, "#bf{ECAL} Test Beam 2021")
c_ratio.cd()
ratio_pad = ROOT.TPad("ratio_pad", "",0., 0., 1.,0.30)
ratio_pad.SetBottomMargin(0.3)
ratio_pad.SetTopMargin(0.03)
ratio_pad.SetGrid()
ratio_pad.Draw()
ratio_pad.cd()
Stk_ratio.Draw('nostack')
Stk_ratio.SetMaximum(1.1)
Stk_ratio.SetMinimum(0.9)
Stk_ratio.GetXaxis().SetRangeUser(150, 180)
Xaxis = ROOT.TGaxis(150.,0.9,180,0.9,0,30,510,"+");
#Stk_ratio.GetXaxis().SetTitle("time [ns]"); Stk_ratio.GetXaxis().SetTitleOffset(1.5); Stk_ratio.GetXaxis().SetTitleSize(0.1)
#Stk_ratio.GetXaxis().SetLabelSize(0.1); Stk_ratio.GetXaxis().SetLabelOffset(0.04)
Stk_ratio.GetYaxis().SetLabelSize(0.1) 
Stk_ratio.GetYaxis().CenterTitle(ROOT.kTRUE); 
Stk_ratio.GetYaxis().SetTitle("Ratio w.r.t. C2"); Stk_ratio.GetYaxis().SetTitleOffset(0.6); Stk_ratio.GetYaxis().SetTitleSize(0.08)
Stk_ratio.GetYaxis().SetNdivisions(-502, ROOT.kTRUE)
Stk_ratio.GetXaxis().SetLabelSize(0)
Xaxis.SetTitle("time [ns]"); Xaxis.SetTitleOffset(1.5); Xaxis.SetTitleSize(0.1); Xaxis.SetTitleFont(42);
Xaxis.SetLabelSize(0.1);Xaxis.SetLabelOffset(0.04); Xaxis.SetLabelFont(42); 
Xaxis.Draw()

c_ratio.SaveAs('/eos/user/c/cbasile/www/ECAL_TB2021/HighPurity/VFEs_scan/compare_templates_ratio.png');
c_ratio.SaveAs('/eos/user/c/cbasile/www/ECAL_TB2021/HighPurity/VFEs_scan/compare_templates_ratio.pdf');

