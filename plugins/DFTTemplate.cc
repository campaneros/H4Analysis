#include "DFTTemplate.h"
#include "TRandom.h"
#include "TCanvas.h"
#include <complex>

//----------Utils-------------------------------------------------------------------------
bool DFTTemplate::Begin(map<string, PluginBase*>& plugins, CfgManager& opts, uint64* index)
{

    //---register shared FFTs
    //   nSamples is divided by two if FFT is from time to frequency domain
    srcInstance_ = opts.GetOpt<string>(instanceName_+".srcInstanceName");    
    channelsNames_ = opts.GetOpt<vector<string> >(instanceName_+".channelsNames");    
    for(auto& channel : channelsNames_)
    {
        if(!opts.OptExist(channel+".fOversampling"))
        {
            Log("configuration for channel < "+channel+" > not found.", ERR);
            return false;
        }
        //---oversampling frequency in GHz
        auto fOversampling = opts.GetOpt<float>(channel+".fOversampling");
        auto tOversampling = 1./fOversampling;
        //---df = 1/t_max, t_max = tUnit*nSamples.
        auto orig_n_sample = opts.OptExist(channel+".signalWin") ?
            opts.GetOpt<int>(channel+".signalWin", 1) - opts.GetOpt<int>(channel+".signalWin", 0):
            opts.GetOpt<float>(channel+".nSamples");
        oversamplingMap_[channel] = make_pair(fOversampling,
                                              opts.GetOpt<float>(channel+".tUnit")*orig_n_sample);
        
		  cout << Form("n_samples= %.0f , fOversampling = %.1f , Nsamples original= %.0f", 
								oversamplingMap_[channel].first*oversamplingMap_[channel].second,
								oversamplingMap_[channel].first,
								orig_n_sample) << endl; 
        //---Register oversampled WF
        auto oversampledName = channel+opts.GetOpt<string>(instanceName_+".outWFSuffix");
        WFs_[channel] = new WFClass(1, tOversampling);
        RegisterSharedData(WFs_[channel], oversampledName, false);
        
        //---Generate automatic cfg info for the oversampled "channel"
        vector<string> newOpts={""};
        newOpts[0] = to_string(tOversampling);
        opts.SetOpt(oversampledName+".tUnit", newOpts);
        newOpts[0] = to_string(int(orig_n_sample*opts.GetOpt<float>(channel+".tUnit")/tOversampling));
        opts.SetOpt(oversampledName+".nSamples", newOpts);
    }

    return true;
}

bool DFTTemplate::ProcessEvent(H4Tree& event, map<string, PluginBase*>& plugins, CfgManager& opts)
{
	//TCanvas* c = new TCanvas("c", "", 1024, 1024);
    for(auto& channel : channelsNames_)
    {
        //---get FFT from source instance data and reset old WF
        WFs_[channel]->Reset();
        auto fft = (FFTClass*)plugins[srcInstance_]->GetSharedData(srcInstance_+"_"+channel, "", false).at(0).obj;
        
        //---build the FFT
        int n_samples = oversamplingMap_[channel].first*oversamplingMap_[channel].second;
        double data[n_samples];
        vector<double> Re, Im;
        Re.reserve(n_samples);
        Im.reserve(n_samples); 
        Re.assign(fft->GetRe()->data(), fft->GetRe()->data()+fft->GetRe()->size());
        Im.assign(fft->GetIm()->data(), fft->GetIm()->data()+fft->GetIm()->size());
		  //auto orig_n_sample = Im.size();

		  //---not so general FIXME
		//  cout << Form ("TH1D: #bins = %.0f xlow = %.2f xhigh = %.2f",
		//		  Re.size()/4.,
		//		  Re.size()/4./oversamplingMap_[channel].second,
		//		  Re.size()/2./oversamplingMap_[channel].second) << endl;
		  TH1D ampl_spectrum("ampl_spectrum","", 
				  Re.size()/4.,
				  Re.size()/4./oversamplingMap_[channel].second,
				  Re.size()/2./oversamplingMap_[channel].second);
		  TF1 ampl_extrapolation("fextr", "expo", Re.size()/4./oversamplingMap_[channel].second, Re.size()/2./oversamplingMap_[channel].second);
		  //cout << Form("FITrange : xlow = %.2f  xhigh = %.2f ", Re.size()/4./oversamplingMap_[channel].second, Re.size()/2./oversamplingMap_[channel].second) << endl;
		  for(unsigned int i=1; i<=ampl_spectrum.GetNbinsX(); ++i)
			  ampl_spectrum.SetBinContent(i, sqrt(pow(Re.at(Re.size()/4+i-1), 2)+pow(Im.at(Im.size()/4+i-1), 2)));
		  ampl_spectrum.Fit(&ampl_extrapolation, "QRSO");
		  //ampl_spectrum.Draw();
		  //c->SaveAs(Form("/eos/user/c/cbasile/www/ECAL_TB2021/PlotDebug/ampl_spectrum_%s.png",channel.c_str()));

		  //TH1D FULLampl_spectrum("FULLampl_spectrum","", 
		  // 	  Re.size(),0., Re.size()/oversamplingMap_[channel].second);
		  //for(unsigned int i=1; i<=FULLampl_spectrum.GetNbinsX(); ++i){
		  //   FULLampl_spectrum.SetBinContent(i, sqrt(pow(Re.at(i-1), 2)+pow(Im.at(i-1), 2)));
		  //   cout << Form(" i = %d \t A = %.2f", i, sqrt(pow(Re.at(i-1), 2)+pow(Im.at(i-1), 2)) ) << endl;
		  //}	  
		  //FULLampl_spectrum.Draw();
		  //c->SaveAs(Form("/eos/user/c/cbasile/www/ECAL_TB2021/PlotDebug/FULLampl_spectrum_%s.png",channel.c_str()));
		  while(Re.size() < n_samples)
		  {
			  auto mag = ampl_extrapolation.Eval(Re.size()/oversamplingMap_[channel].second);
			  auto phase = gRandom->Uniform(-TMath::Pi(), TMath::Pi());
			  // Re.insert(Re.begin()+(Re.size()/2), 2,
			  //           ampl_extrapolation.Eval(Re.size()/oversamplingMap_[channel].second));
            // if(Im.size() < orig_n_sample*2)
            // {
            //     // auto insert_point = Im.size()/2;
            //     // Im.insert(Im.begin()+insert_point, -(2*TMath::Pi()*(Im.size()-orig_n_sample)/orig_n_sample-TMath::Pi()));
            //     // Im.insert(Im.begin()+insert_point, 2*TMath::Pi()*(Im.size()-orig_n_sample)/orig_n_sample-TMath::Pi());
            //     ph1 = -(2*TMath::Pi()*(Im.size()-orig_n_sample)/orig_n_sample-TMath::Pi());
            //     ph2 = 2*TMath::Pi()*(Im.size()-orig_n_sample)/orig_n_sample-TMath::Pi();
            // }
            // else if(Im.size() < orig_n_sample*3)
            // {
            //     // auto insert_point = Im.size()/2;
            //     // Im.insert(Im.begin()+insert_point, -(-2*TMath::Pi()*(Im.size()-orig_n_sample*2)/(orig_n_sample*2)+TMath::Pi()));
            //     // Im.insert(Im.begin()+insert_point, 2*TMath::Pi()*(Im.size()-orig_n_sample)/orig_n_sample-TMath::Pi());
            //     ph1 = -(-2*TMath::Pi()*(Im.size()-orig_n_sample*2)/(orig_n_sample*2)+TMath::Pi());
            //     ph2 = 2*TMath::Pi()*(Im.size()-orig_n_sample)/orig_n_sample-TMath::Pi();
            // }
            // else                
            //     Im.insert(Im.begin()+(Im.size()/2), 2, 0.);
            auto insert_point = Im.size()/2;
            complex<double> c1 = polar(mag, phase);
            complex<double> c2 = polar(mag, -phase);
            Re.insert(Re.begin()+insert_point, c1.real());
            Re.insert(Re.begin()+insert_point, c2.real());
            Im.insert(Im.begin()+insert_point, c1.imag());
            Im.insert(Im.begin()+insert_point, c2.imag());
        }
        //---construct FFT and oversampled WF
        auto fftc2r = TVirtualFFT::FFT(1, &n_samples, "C2R");
        //---apply a Butterworth filter
        if(opts.OptExist(channel+".BWFilter", -1))
        {
            int order = opts.GetOpt<int>(channel+".BWFilter.order");
            float wCut = opts.GetOpt<float>(channel+".BWFilter.wCut");
            float dump;
            for(int iSample=0; iSample<Re.size()/2; ++iSample)
            {
                dump = TMath::Sqrt(1./(1.+TMath::Power(iSample/oversamplingMap_[channel].second/wCut, 2*order)));
                Re[iSample] *= dump;
                Im[iSample] *= dump;
                Re[Re.size()-iSample] = Re[iSample];
                Im[Re.size()-iSample] = Im[iSample];
            }            
        }
        
		  //TH1D OVSAMPampl_spectrum("OVSAMPampl_spectrum","", 
        //Re.size(),0., Re.size()/oversamplingMap_[channel].second);
        //for(unsigned int i=1; i<=OVSAMPampl_spectrum.GetNbinsX(); ++i)
        //OVSAMPampl_spectrum.SetBinContent(i, sqrt(pow(Re.at(i-1), 2)+pow(Im.at(i-1), 2)));
		  //OVSAMPampl_spectrum.Draw();
		  //c->SetLogy();
		  //c->SaveAs(Form("/eos/user/c/cbasile/www/ECAL_TB2021/PlotDebug/OVSAMPampl_spectrum_%s.png",channel.c_str()));
         
		  fftc2r->SetPointsComplex(Re.data(), Im.data());
        fftc2r->Transform();
        fftc2r->GetPoints(data);

        //---fill new, oversampled WF
        for(int iSample=0; iSample<n_samples; ++iSample)
            WFs_[channel]->AddSample(data[iSample]);

        delete fftc2r;
    }
    
    return true;
}
