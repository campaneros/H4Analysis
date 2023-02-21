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

import numpy as np


import sys
sys.path.insert(0, 'utils/')
import CBfunction as CB
#reload(CB)
import CrystalMap as crystMap
#reload(crystMap)
from uncertainties import unumpy
from uncertainties import ufloat

ROOT.gROOT.SetBatch(True)


dict_C2_energy = { '25' : [15183] , '50' : [15145, 15146], '75' : [15199], '100' : [15153], '125' : [15190], '150' : [15158]}
#dict_C2_energy = { '100' : [15153]}
dict_energy_Chi2max = {'25' : 1000,  '50' : 1000,  '75': 1500, '100': 4000, '125': 4500, '150': 4000}
dict_energy_Amin    = {'25' : 100,  '50' : 500,  '75': 1000, '100': 1500, '125': 2000, '150': 2000}
dict_energy_Amax    = {'25' : 1000, '50' : 2000, '75': 2500, '100': 3000, '125': 4000, '150': 4500}
dict_energy_Cx      = {'25' : 0.,  '50' : 0.,  '75': 0., '100': 0., '125': 0., '150': 5.}
plot_folder = '/eos/user/c/cbasile/www/ECAL_TB2021/Linearity/FitAmpl'
outstr = '_fit'
trees_path = '/eos/user/c/cbasile/ECAL_TB2021/ntuples_templates_v1/'


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
        hodo1_X = ROOT.TChain('h1X')
        hodo1_Y = ROOT.TChain('h1Y')
        for run in runs:
            #tree.Add("%s/ECAL_H4_October2018_%s.root"%(trees_path,run))
            tree.Add(f'{trees_path}/{run}/*.root')
            hodo1_X.Add(f'{trees_path}/{run}/*.root')
            hodo1_Y.Add(f'{trees_path}/{run}/*.root')
        
        myCB = CB.CBfunction(tree)
        myCB.set_hodoscopes(hodo1_X,hodo1_Y)
        myCB.set_crystal(crystal)
        myCB.set_ampLimits(dict_energy_Amin[energy], dict_energy_Amax[energy])
        myCB.set_FitChiThreshold(dict_energy_Chi2max[energy])
        myCB.set_energy(energy)
        myCB.set_position(dict_energy_Cx[energy], -5.0, 5)
                
        myCB.prepare_histogram()
        myCB.CBintialization()
        myCB.fitToData()
        myCB.plot()
        tmp_dict = {}
        tmp_dict[energy] = myCB.fitResults()
        C2_results.append(tmp_dict)
        
        canvas_num+=1

c.Draw()
c.SaveAs('%s/C2_fits_%s.pdf'%(plot_folder,outstr))
c.SaveAs('%s/C2_fits_%s.png'%(plot_folder,outstr))

############## --------------- LINEARITY FIT --------------- ##############

energies_float = []
means_C2 = []
means_C2_err = []
for item in C2_results:
    energies_float.append((float)(list(item.keys())[0]))
    means_C2.append(item[list(item.keys())[0]]['CBmean'][0])
    means_C2_err.append(item[list(item.keys())[0]]['CBmean'][1])

def linear_func(x, a, b):
    return a * x + b

fig, ax = plt.subplots()
#ax.plot(energies_float, means_C3,'bo' )
ax.errorbar(energies_float, means_C2, yerr=means_C2_err,fmt='ko')
popt, pcov = curve_fit(linear_func, energies_float, means_C2, sigma=means_C2_err,absolute_sigma=True)
perr = np.sqrt(np.diag(pcov))
print('fit parametes and 1-sigma errors:')
for i in range(len(popt)):
    print('\t par[%d] = %.3f +- %.3f'%(i,popt[i],perr[i]))


xfine = np.linspace(0., 250., 1000)  # define values to plot the function for
ax.plot(xfine, linear_func(xfine, popt[0], popt[1]), 'r-',label='linear fit \n slope= %.3f +- %.3f \n intercept = %.3f +- %.3f'%(popt[0],perr[0], popt[1],perr[1]))
ax.set(xlabel='Beam Energy (GeV)', ylabel='ADC CBmean ',  title='ADC to GeV')


plt.legend()
plt.grid()
plt.show()
fig.savefig('%s/ADC_to_GeV_%s.png'%(plot_folder,outstr))
fig.savefig('%s/ADC_to_GeV_%s.pdf'%(plot_folder,outstr))
