#ifndef LLMINIMIZER
#define LLMINIMIZER

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <random>

#include "Math/Interpolator.h"
#include "Math/Minimizer.h"
#include "Math/Factory.h"
#include "Math/Functor.h"
#include "TFitResult.h"
#include "TMath.h"
#include "TH1F.h"
#include "TF1.h"
#include "TError.h"
 
using namespace std;


class LLminimizer
{
private:
    int minuit_print_level_;
    vector<float>  m_mcp1_ampl_;
    vector<float>  m_mcp2_ampl_;
    vector<double>  m_dt_ecal_mcp1_;
    vector<double>  m_dt_ecal_mcp2_;
    vector<float>  m_dt_mcp2_mcp1_;
    vector<double>  m_weights_;
    vector<float>  m_energy_;
    long m_data_size_;
    double t_unit_;
    TString m_crystal_;
 
 
public:
  //  LLminimizer(vector<double> mcp1_ampl,vector<double> mcp2_ampl,vector<double> dt_ecal_mcp1,vector<double> dt_ecal_mcp2,vector<double> dt_mcp2_mcp1,  TString crystal, TString energy);
   // void SetData(vector<double> mcp1_ampl,vector<double> mcp2_ampl,vector<double> dt_ecal_mcp1,vector<double> dt_ecal_mcp2,vector<double> dt_mcp2_mcp1);
    LLminimizer(int events_num, float *mcp1_ampl,float *mcp2_ampl,double *dt_ecal_mcp1,double *dt_ecal_mcp2,float *dt_mcp2_mcp1, double* weights, float *energy, double t_unit=1, TString crystal="C3", int print_level=0);
    void SetData(int events_num, float *mcp1_ampl,float *mcp2_ampl,double *dt_ecal_mcp1,double *dt_ecal_mcp2,float *dt_mcp2_mcp1, double* weights, float *energy);
 
    void SetCrystal(TString crystal);
    double NegLogLikelihood(const double* par=NULL);
    int MinimizeNLL(float tolerance=1., int minuit_print_level= 1);
    double NegLogLikelihoodSimultaneous(const double* par=NULL);
    int MinimizeNLLSimultaneous(float tolerance=1., int minuit_print_level=1.);
    
    void Clear()
    {
        m_nll_.clear();
        m_mcp1_ampl_.clear();
        m_mcp2_ampl_.clear();
        m_dt_ecal_mcp1_.clear();
        m_dt_ecal_mcp2_.clear();
        m_dt_mcp2_mcp1_.clear();
        m_weights_.clear();
        m_energy_.clear();        
    };
    
    vector<double> m_Cm_, m_alpha_,m_beta_,m_alpha_cb1_,m_alpha_cb2_,m_n_cb1_,m_n_cb2_;
    vector<double> m_Cm_e_, m_alpha_e_,m_beta_e_,m_alpha_cb1_e_,m_alpha_cb2_e_,m_n_cb1_e_,m_n_cb2_e_;

    double m_a1_,m_a2_,m_b1_,m_b2_,m_gamma_;
    double m_a1_e_,m_a2_e_,m_b1_e_,m_b2_e_,m_gamma_e_;
    
    vector<double>  m_nll_;
 
};
 
#endif
