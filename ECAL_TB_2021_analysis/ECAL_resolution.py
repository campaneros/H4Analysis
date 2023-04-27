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
import CrystalMap as crystMap
from uncertainties import unumpy
from uncertainties import ufloat

ROOT.gROOT.SetBatch(True)


dict_C2_energy      = {'25' : [15183] , '50' : [15145, 15146], '75' : [15199], '100' : [15153], '125' : [15190], '150' : [15158]}

dict_energy_Chi2max = {'25' : 200,   '50' : 1000,  '75': 2300, '100': 2800, '125': 4000, '150': 4300}

dict_energy_Amin    = {'25' : 100,  '50' : 500,  '75': 1000, '100': 1500, '125': 2000, '150': 2000}
dict_energy_Amax    = {'25' : 1000, '50' : 2000, '75': 2500, '100': 3000, '125': 4500, '150': 4500}

dict_energy_Cx      = {'25' : 2.5,    '50' : 2.5,    '75':  0.,   '100':  0.,  '125':  2., '150': 2.5}
dict_energy_Cy      = {'25' : -3.,    '50' : -3.,    '75': -4.,   '100': -2.5, '125': -3., '150': -2.5}

dict_energy_Nbins   = {'25' : 800,   '50' : 500,   '75': 400,  '100': 300, '125': 300, '150': 250}

plot_folder = '/eos/user/c/cbasile/www/ECAL_TB2021/Linearity/FitAmpl'
outstr = '_3x3'
trees_path = '/eos/cms/store/group/dpg_ecal/comm_ecal/upgrade/testbeam/ECALTB_H4_Oct2021/LowPurity/ntuples_fit'

# 3x3 MATRIX around C2
crystal = 'C2'
matrix =  'B2,B3,C3,D3,C2,D2,D1,C1,B1'.split(',')
dict_crystals_calibration = {}
print(f'  MATRIX {matrix}')

c = ROOT.TCanvas("c","c",2000,1000)
c.Divide(3,2)
canvas_num=0
MX3_results = []
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

    myCB.doubleSidedCB = True
    myCB.nbins = dict_energy_Nbins[energy] 
    myCB.xaxis_scale = 0.4
    myCB.a_initial = 1.5
    myCB.a_initial = 0.5
    myCB.n_initial = 5 
    myCB.n_initial = 15 


    myCB.set_crystal(crystal)
    myCB.set_ampLimits(dict_energy_Amin[energy], dict_energy_Amax[energy])
    myCB.set_FitChiThreshold(dict_energy_Chi2max[energy])
    myCB.set_energy(energy)
    myCB.set_position(dict_energy_Cx[energy], dict_energy_Cy[energy], 4)

    myCB.prepare_sumhistogram(dict_crystals_calibration,matrix)
    myCB.xaxis_scale = 0.2
    if myCB.doubleSidedCB==True : 
        myCB.CB2intialization()
    else : myCB.CBintialization()

    myCB.fitToData()
    myCB.plot()
    tmp_dict = {}
    tmp_dict[energy] = myCB.fitResults()
    MX3_results.append(tmp_dict)
    canvas_num+=1
        

c.Draw()
c.SaveAs('%s/intercalibration_fits_%s.pdf'%(plot_folder,outstr))
c.SaveAs('%s/intercalibration_fits_%s.png'%(plot_folder,outstr))

