import ROOT
from ROOT import RooRealVar,RooCBShape,RooDataHist,RooArgList,RooFit
from ROOT import gROOT,gStyle,gPad
import csv
import json
import array as array
import matplotlib
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os
#import mplhep as hep
#hep.style.use("CMS")

import numpy as np


import sys
sys.path.insert(0, 'utils/')
import CBfunction as CB
import CrystalMap as crystMap
from uncertainties import unumpy
from uncertainties import ufloat

ROOT.gROOT.SetBatch(True)


dict_C2_energy = { '25' : [15183] ,'50' : [15145, 15146], '75' : [15199], '100' : [15153], '125' : [15190], '150' : [15158]}
dict_energy_Chi2max = {'25' : 200,   '50' : 1000,  '75': 2300, '100': 2800, '125': 4000, '150': 4300}
dict_energy_Amin    = {'25' : 400,   '50' : 800,   '75': 1300, '100': 1600, '125': 2000, '150': 2000}
dict_energy_Amax    = {'25' : 700,   '50' : 1500,  '75': 2100, '100': 2800, '125': 3400, '150': 4500}


dict_energy_Cx      = {'25' : 2.5,    '50' : 2.5,    '75':  0.,   '100':  0.,  '125':  0., '150': 2.5}
dict_energy_Cy      = {'25' : -3.,    '50' : -3.,    '75': -4.,   '100': -2.5, '125': -3., '150': -2.5}

dict_energy_Nbins   = {'25' : 800,   '50' : 500,   '75': 400,  '100': 300, '125': 300, '150': 250}
plot_folder = '/eos/user/c/cbasile/www/ECAL_TB2021/Linearity/FitAmpl'
outstr = 'poster'
trees_path = '/eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/LowPurity/ntuples_fit'


c = ROOT.TCanvas("c","c",2000,1000)
c.Divide(3,2)
canvas_num=0
C2_results = []
crystal='C2'
energies = sorted([int(item) for item in dict_C2_energy.keys()])
print(energies)
energies = [str(item) for item in energies]
print(energies)

for energy in energies :
        c.cd(canvas_num+1) 
        
        runs = dict_C2_energy[energy]
        tree = ROOT.TChain("h4")
        for run in runs:
            tree.Add(f'{trees_path}/{run}/*.root')
        
        myCB = CB.CBfunction(tree)
        myCB.set_crystal(crystal)
        myCB.xaxis_scale = 0.3
        myCB.a_initial = 0.5
        myCB.set_energy(energy)
        myCB.set_position(dict_energy_Cx[energy], dict_energy_Cy[energy], 4)

        myCB.nbins=dict_energy_Nbins[energy]
        myCB.prepare_histogram()
        if (myCB.doubleSidedCB):
            myCB.CB2intialization()
        else : myCB.CBintialization()

        myCB.fitToData()
        myCB.plot()
        tmp_dict = {}
        tmp_dict[energy] = myCB.fitResults()
        C2_results.append(tmp_dict)
        
        canvas_num+=1

c.Draw()
c.SaveAs('%s/C2_fits_%s.pdf'%(plot_folder,outstr))
c.SaveAs('%s/C2_fits_%s.png'%(plot_folder,outstr))

with open("results/C2results_%s.json"%outstr, "w") as fp:
    json.dump(C2_results,fp) 

energies_float = []
means_C2 = []
means_C2_err = []
sigma_C2 = []
sigma_C2_err = []
sigma_over_mean_C2 = []
energies_float_unc = []
for item in C2_results:
    energies_float.append((float)(list(item.keys())[0]))
    energies_float_unc.append((float)(list(item.keys())[0])*0.005)
    means_C2.append(item[list(item.keys())[0]]['CBmean'][0])
    means_C2_err.append(item[list(item.keys())[0]]['CBmean'][1])
    sigma_C2.append(item[list(item.keys())[0]]['CBsigma'][0])
    sigma_C2_err.append(item[list(item.keys())[0]]['CBsigma'][1])
    

means =  unumpy.umatrix(means_C2, means_C2_err)
sigmas =  unumpy.umatrix(sigma_C2, sigma_C2_err)

sigma_over_mean_C2 = sigmas/means



############## --------------- LINEARITY FIT --------------- ##############


def linear_func(x, a, b):
    return a * x + b
c0 = ROOT.TCanvas("C2_linearity", "", 800, 800)



fig, ax = plt.subplots()
#ax.plot(energies_float, means_C3,'bo' )
ax.errorbar(energies_float, means_C2, yerr=means_C2_err,fmt='ko')
popt, pcov = curve_fit(linear_func, energies_float, means_C2, sigma=means_C2_err,absolute_sigma=True)
perr = np.sqrt(np.diag(pcov))
print('fit parametes and 1-sigma errors:')
for i in range(len(popt)):
    print('\t par[%d] = %.3f +- %.3f'%(i,popt[i],perr[i]))


xfine = np.linspace(0., 200, 1000)  # define values to plot the function for
ax.plot(xfine, linear_func(xfine, popt[0], popt[1]), 'r-',label='linear fit') #\n slope= %.3f +- %.3f \n intercept = %.3f +- %.3f'%(popt[0],perr[0], popt[1],perr[1]))
ax.set(xlabel='Beam Energy (GeV)', ylabel='Reconstructed energy [counts]',  title='') #title ? single crystal response



plt.legend()
plt.grid()
plt.show()
fig.savefig('%s/ADC_to_GeV_%s.png'%(plot_folder,outstr))
fig.savefig('%s/ADC_to_GeV_%s.pdf'%(plot_folder,outstr))

residuals = (means_C2 - linear_func(np.asarray(energies_float), popt[0], popt[1]))/means_C2_err
fig, ax = plt.subplots()
ax.errorbar(energies_float, residuals, yerr=means_C2_err,fmt='ko')
ax.plot(xfine, np.zeros(len(xfine)), 'r-')
ax.set(xlabel='Beam Energy (GeV)', ylabel='residuals', ylim = [-10,10])

plt.grid()
fig.savefig('%s/residuals_ADC_to_GeV_%s.png'%(plot_folder,outstr))
fig.savefig('%s/residuals_ADC_to_GeV_%s.pdf'%(plot_folder,outstr))


############## --------------- RESOLUTION --------------- ##############

    
### ECAL text
ECALtex = ROOT.TLatex()
ECALtex.SetTextFont(42)
ECALtex.SetTextAngle(0)
ECALtex.SetTextColor(ROOT.kBlack)    
ECALtex.SetTextSize(0.04)    
ECALtex.SetTextAlign(12)

c1 = ROOT.TCanvas("C2_resolution", "", 800, 800)
    
y=array.array('d',unumpy.nominal_values(sigma_over_mean_C2).tolist()[0])
ey=array.array('d',unumpy.std_devs(sigma_over_mean_C2).tolist()[0])
gr = ROOT.TGraphErrors(len(energies_float),array.array('d',energies_float),y,array.array('d',energies_float_unc) ,ey )
gr.SetMarkerStyle( 20 )

gr.SetTitle('')
gr.GetYaxis().SetLabelSize(0.04)
gr.GetYaxis().SetRangeUser(0.016, 0.032)
gr.GetXaxis().SetLabelSize(0.04)
gr.GetYaxis().SetTitleOffset(1.7)
gr.GetYaxis().SetTitle( '#sigma(E)/E' )
gr.GetXaxis().SetTitle( 'E (GeV)' )
gr.Draw( 'AP' )
leg = ROOT.TLegend(0.55,0.65,0.8,0.9)
leg.SetFillStyle(-1)
leg.SetBorderSize(0)
leg.SetTextFont(42)
leg.SetTextSize(0.03)
leg.AddEntry(gr,'ECAL C2 crystal','P')
leg.Draw()
ECALtex.DrawLatex(21,0.03, "#bf{ECAL} Test Beam 2021")

c1.Draw()  
ROOT.gStyle.SetLineWidth(2)
ROOT.gPad.SetMargin(0.13,0.13,0.13, 0.13)
ROOT.gPad.SetGridx(1); ROOT.gPad.SetGridy(1);
c1.SaveAs('%s/EnergyResolution_C2_%s.pdf'%(plot_folder,outstr))
c1.SaveAs('%s/EnergyResolution_C2_%s.png'%(plot_folder,outstr))



