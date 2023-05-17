import ROOT
import csv
import json
import array as array
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os
from uncertainties import unumpy
from uncertainties import ufloat


import argparse

ROOT.gSystem.Load("../lib/libH4Analysis.so")
ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetLineWidth(2)
ROOT.gStyle.SetPadTickX(1)
ROOT.gStyle.SetPadTickY(1)

# read a JSON file which contains the CB means and sigmas to build
# - LINEARITY PLOT
# - RESOLUTION PLOT

import locale
loc = locale.getlocale()
print(loc)
locale.setlocale(locale.LC_ALL, 'en_US')
loc = locale.getlocale()
print(loc)

parser = argparse.ArgumentParser (description = 'make ECAL plots')
parser.add_argument('-i', '--input', help = 'JSON file to read in input')
parser.add_argument('-o', '--output', help = 'folder to save plots', default = '/eos/user/c/cbasile/www/ECAL_TB2021/Linearity/FitAmpl')
parser.add_argument('--tag', default = 'C2')
parser.add_argument('--crystal', default= 'C2 crystal')

args = parser.parse_args ()
plot_folder = args.output

with open(args.input, 'r') as openfile:
    # Reading from json file
    results= json.load(openfile)

#print(results)

energies_float = []
CBmeans= []
CBmeans_err = []
CBsigma = []
CBsigma_err = []
sigma_over_mean_C2 = []
energies_float_unc = []
for item in results:
    energies_float.append((float)(list(item.keys())[0]))
    energies_float_unc.append((float)(list(item.keys())[0])*0.005)
    CBmeans.append(item[list(item.keys())[0]]['CBmean'][0])
    CBmeans_err.append(item[list(item.keys())[0]]['CBmean'][1])
    CBsigma.append(item[list(item.keys())[0]]['CBsigma'][0])
    CBsigma_err.append(item[list(item.keys())[0]]['CBsigma'][1])

print(f' -> E [GeV] : {energies_float}')


means =  unumpy.umatrix(CBmeans, CBmeans_err)
sigmas =  unumpy.umatrix(CBsigma, CBsigma_err)

sigma_over_mean = sigmas/means



############## --------------- LINEARITY FIT --------------- ##############

### ECAL text
ECALtex = ROOT.TLatex()
ECALtex.SetTextFont(42)
ECALtex.SetTextAngle(0)
ECALtex.SetTextColor(ROOT.kBlack)    
ECALtex.SetTextSize(0.05)    
ECALtex.SetTextAlign(12)

def linear_func(x, a, b):
    return a * x + b
popt, pcov = curve_fit(linear_func, energies_float, CBmeans, sigma=CBmeans_err,absolute_sigma=True)
perr = np.sqrt(np.diag(pcov))
covariance = pcov[0,1]
print('fit parametes and 1-sigma errors:')
for i in range(len(popt)):
    print('\t par[%d] = %.3f +- %.3f'%(i,popt[i],perr[i]))
print('\t covariance = %.3f '%(covariance))

fit_CBmeans = linear_func(np.asarray(energies_float), popt[0], popt[1])
fit_CBmeans_err = np.sqrt(perr[1]**2 + (perr[0]*np.asarray(energies_float))**2)
fit_means = unumpy.umatrix(fit_CBmeans, fit_CBmeans_err)
#print(means)
#print(fit_means)
#residuals = (CBmeans - linear_func(np.asarray(energies_float), popt[0], popt[1]))/linear_func(np.asarray(energies_float), popt[0], popt[1])
residuals = (means - fit_means)/fit_means
pull = (means -fit_means)/CBmeans_err
#print(residuals)
xfine = np.linspace(0., 200, 1000)  # define values to plot the function for

c0 = ROOT.TCanvas("C2_linearity", "", 900, 1024)
up_pad = ROOT.TPad("up_pad", "", 0., 0.30, 1.,1.) 
up_pad.Draw()
up_pad.SetMargin(0.15, 0.1,0.0,0.1)
up_pad.SetGrid()
up_pad.cd()
lin_gr = ROOT.TGraphErrors(len(energies_float), np.array(energies_float).astype("float"),np.array(CBmeans).astype("float"),np.array(energies_float_unc).astype("float") ,np.array(CBmeans_err).astype("float"))
fit_func = ROOT.TF1("lin_func", "[0]*x + [1]", 10, 300)
fit_func.SetParameter(0, popt[0]); fit_func.SetParameter(1, popt[1])
fit_func.SetLineWidth(3)
lin_gr.SetMarkerStyle(20)
#FitRes = lin_gr.Fit(linear_func, "FS", "L", 20, 200)
#print(f' = Linear-fit Chi2 = {FitRes.Chi2}')
lin_gr.SetTitle("")
lin_gr.GetYaxis().SetTitle("Reconstructed energy (ADC count)"); lin_gr.GetYaxis().SetTitleSize(0.05)
lin_gr.GetYaxis().SetLabelSize(0.04); 
lin_gr.Draw('AP')
fit_func.Draw("same")
lin_gr.Draw('P')
ECALtex.DrawLatex(21, 0.9*lin_gr.GetYaxis().GetXmax(), "#bf{ECAL} Test Beam 2021")
ECALtex.SetTextSize(0.035)    
ECALtex.DrawLatex(21, 0.85*lin_gr.GetYaxis().GetXmax(), 'ADCtoGeV = %.4f #pm %.4f'%(popt[0], perr[0]))
ECALtex.DrawLatex(21, 0.80*lin_gr.GetYaxis().GetXmax(), 'offset = %.4f #pm %.4f'%(popt[1], perr[1]))
c0.cd()
ratio_pad = ROOT.TPad("ratio_pad", "",0., 0., 1.,0.30)
ratio_pad.SetMargin(0.15,0.1,0.25,0.04)
ratio_pad.Draw()
ratio_pad.cd()
ratio_pad.SetGrid()
ratio_pad.Draw()
print(type(energies_float))
res_gr= ROOT.TGraphErrors(len(energies_float),np.array(energies_float, dtype= float),unumpy.nominal_values(residuals)*100,np.array(energies_float_unc, dtype= float),unumpy.std_devs(residuals)*100) 
#res_gr= ROOT.TGraphErrors(len(energies_float),np.array(energies_float, dtype= float),unumpy.nominal_values(pull),np.array(energies_float_unc, dtype= float), np.ones(len(energies_float)))
zero_level = ROOT.TLine(lin_gr.GetXaxis().GetXmin(),0, lin_gr.GetXaxis().GetXmax(),0); zero_level.SetLineWidth(3); zero_level.SetLineColor(ROOT.kRed)
res_gr.SetTitle("")
res_gr.GetXaxis().SetTitle("Beam energy (GeV)"); res_gr.GetXaxis().SetTitleSize(0.1); res_gr.GetXaxis().SetTitleOffset(1)
res_gr.GetXaxis().SetLabelSize(0.1)
res_gr.GetYaxis().SetRangeUser(-5,5)
res_gr.GetYaxis().SetTitle("(E_{reco}-E_{reco}^{fit})/E_{reco}^{fit}(%)"); res_gr.GetYaxis().CenterTitle(); res_gr.GetYaxis().SetTitleSize(0.1); res_gr.GetYaxis().SetTitleOffset(0.65)
#res_gr.GetYaxis().SetTitle("Pull")
res_gr.GetYaxis().SetLabelSize(0.1); res_gr.GetYaxis().SetNdivisions(-504)
res_gr.SetMarkerStyle(20)
res_gr.Draw('AP')
zero_level.Draw('same')
res_gr.Draw('P')

c0.SaveAs('%s/ADC_to_GeV_%s.png'%(plot_folder,args.tag))
c0.SaveAs('%s/ADC_to_GeV_%s.pdf'%(plot_folder,args.tag))



############## --------------- RESOLUTION --------------- ##############

    

c1 = ROOT.TCanvas("C2_resolution", "", 800, 800)

ROOT.gStyle.SetLabelFont(42);
    
y=array.array('d',unumpy.nominal_values(sigma_over_mean).tolist()[0])
ey=array.array('d',unumpy.std_devs(sigma_over_mean).tolist()[0])

# resolution fit
def resol_func(x, N, S, C):
    #N = 0.51 # fixed noise term (Simone)
    resol = N*N/(x*x) + S*S/x + C*C
    return np.sqrt(resol)
popt, pcov = curve_fit(resol_func, energies_float, y, sigma=ey,absolute_sigma=True)
perr = np.sqrt(np.diag(pcov))
print('fit parametes and 1-sigma errors:')
for i in range(len(popt)):
    print('\t par[%d] = %.3f +- %.3f'%(i,popt[i],perr[i]))

fit_resol = ROOT.TF1("resol_func", "sqrt([0]*[0]/(x*x) + [1]*[1]/x + [2]*[2])", 10, 300)
fit_resol.SetParameter(0, popt[0]); fit_resol.SetParameter(1, popt[1]); fit_resol.SetParameter(2, popt[2]);
fit_resol.SetLineWidth(3)


# make plot

gr = ROOT.TGraphErrors(len(energies_float),array.array('d',energies_float),y,array.array('d',energies_float_unc) ,ey )
gr.SetMarkerStyle(20)

gr.SetTitle('')
gr.GetYaxis().SetTitleSize(0.04)
gr.GetYaxis().SetLabelSize(0.04)
Ymin = 0.; Ymax = 0.05
gr.GetYaxis().SetRangeUser(Ymin, Ymax)
#gr.GetYaxis().SetNdivisions(-510)
gr.GetYaxis().SetTitleOffset(1.9)
gr.GetYaxis().SetTitle( '#sigma(E)/E')
gr.GetXaxis().SetTitleOffset(1.5)
gr.GetXaxis().SetTitleSize(0.04)
gr.GetXaxis().SetLabelSize(0.04)
gr.GetXaxis().SetRangeUser(0., 300)
gr.GetXaxis().SetTitle( 'E (GeV)' )
gr.Draw( 'AP' )
fit_resol.Draw('same')
# legend
leg = ROOT.TLegend(0.5,0.7,0.8,0.9)
leg.SetFillStyle(-1)
leg.SetBorderSize(0)
leg.SetTextFont(42)
leg.SetTextSize(0.035)
leg.AddEntry(gr,f'ECAL {args.crystal}','P')
leg.AddEntry(fit_resol, "#frac{N}{E} #oplus #frac{S}{#sqrt{E}} #oplus C", "l")
leg.Draw()
# text on plot
fit_txt = ROOT.TLatex()
fit_txt.SetTextFont(42)
fit_txt.SetTextAngle(0)
fit_txt.SetTextColor(ROOT.kBlack)    
fit_txt.SetTextSize(0.035)    
fit_txt.SetTextAlign(12)
fit_txt.DrawLatex(20, 0.014, 'N = %.4f #pm %.4f'%(popt[0], perr[0]))
fit_txt.DrawLatex(20, 0.012, 'S = %.4f #pm %.4f'%(popt[1], perr[1]))
fit_txt.DrawLatex(20, 0.010, 'C = %.4f #pm %.4f'%(popt[2], perr[2]))
ECALtex.SetTextSize(0.045)
ECALtex.DrawLatex(20,0.005, "#bf{ECAL} Test Beam 2021")

c1.Draw()  
ROOT.gStyle.SetLineWidth(2)
ROOT.gPad.SetMargin(0.15,0.10,0.15, 0.10)
ROOT.gPad.SetGridx(1); ROOT.gPad.SetGridy(1)
c1.SaveAs('%s/EnergyResolution_C2_%s.pdf'%(plot_folder,args.tag))
c1.SaveAs('%s/EnergyResolution_C2_%s.png'%(plot_folder,args.tag))
