// g++ templates/phase_correction.cc -O3 -std=c++17 -lstdc++fs `root-config --libs --cflags` -o bin/phase_correction.exe
// ./bin/phase_correction.exe [run] [Amin] [Amax] [path]

#include "ROOT/RDataFrame.hxx"
#include "ROOT/RResultPtr.hxx"
#include "ROOT/RVec.hxx"
#include "TSystem.h"
#include "TDirectory.h"
#include "TCanvas.h"
#include "TStyle.h"
#include "TH1F.h"
#include "TF1.h"
#include <stdlib.h>
#include <vector>
#include <tuple>
#include <experimental/filesystem>
namespace fs = std::experimental::filesystem;

using namespace std;


int main (int argc, char *argv[])
{
    int run = atoi(argv[1]);
    int minamp = atoi(argv[2]);
    int maxamp = atoi(argv[3]);
    TString path = argv[4]; 
    bool debug = false; 
    bool save_friend = true; 
    bool iter = false; 


	 if (path == "") path = "/eos/user/c/cbasile/ECAL_TB2021/ntuples_templates";
    cout << Form ( "Ntuples path: %s/%i", path.Data(), run) <<endl; 

    gSystem->Load("lib/libH4Analysis.so");
    gStyle->SetOptStat(0);
	
    cout << "LIBs set-up" << endl;

    if (!save_friend) ROOT::EnableImplicitMT();
    ROOT::RDataFrame df("h4", Form("%s/%i/*.root", path.Data(), run)); //("tree_name", "path")

    string selection = "";
    if (iter)
        selection = Form("trg == PHYS && digi.fit_ampl[C3]>%i && fit_ampl[MCP1]>120 && digi.fit_ampl[C3]<%i", minamp, maxamp);
    else
        selection = Form("trg == PHYS && evt_flag == 1 && digi_t.amp_max[C3_T]>%i && fit_ampl[MCP1]>200 && digi_t.amp_max[C3_T]<%i", minamp, maxamp);
        //selection = Form("trg == PHYS && evt_flag == 1 && digi_t.amp_max[C3_T]>%i && fit_ampl[MCP1]>500 && digi_t.amp_max[C3_T]<%i&&(phase<1.407||phase>1.408)", minamp, maxamp);

    cout << "Selection: " << selection << endl;

    ROOT::RDF::RNode fn = df;
    
    if (iter)
        fn = df.Define("dtime", "digi.fit_time[C3]-fit_time[MCP1]+fit_time[CLK]-int((digi.fit_time[C3]-fit_time[MCP1]+fit_time[CLK])/6.238)*6.238")
            .Define("phase", "digi_t.fit_time[C3_T]-int(digi_t.fit_time[C3_T]/6.238)*6.238")
            .Define("amp", "digi_t.fit_ampl[C3_T]")
            .Define("timeMCP", "fit_time[MCP1]")
            .Define("timeCLK", "fit_time[CLK]")
            .Define("maxtime", "time_max[C3_T]")
            .Define("maxtimeCLK", "time_max[CLK]")
            .Define("maxtimeMCP", "time_max[MCP1]")
            .Define("ampMCP", "amp_max[MCP1]")
            .Define("gainxtal", "gain[C3_T]");
    else
        fn = df.Define("dtime", "digi_t.time_max[C3_T]-fit_time[MCP1]+fit_time[CLK]-int((digi_t.time_max[C3_T]-fit_time[MCP1]+fit_time[CLK])/6.238)*6.238")
            .Define("phase", "digi_t.time_max[C3_T]-int(digi_t.time_max[C3_T]/6.238)*6.238")
            .Define("amp", "digi_t.amp_max[C3_T]")
            .Define("timeMCP", "fit_time[MCP1]")
            .Define("timeCLK", "fit_time[CLK]")
            .Define("maxtime", "time_max[C3_T]")
            .Define("maxtimeCLK", "time_max[CLK]")
            .Define("maxtimeMCP", "time_max[MCP1]")
            .Define("ampMCP", "amp_max[MCP1]")
            .Define("gainxtal", "gain[C3_T]");


    fn = fn.Filter(selection, "selection");

    // make phase correction
    auto c = new TCanvas("c", "c", 600, 600);
    float ylow = 4.6, yhigh = 6.2;
    auto dtime_phase = fn.Histo2D({"dtime_phase", ";APD sampling phase (ns); #Deltat_{APD-MCP}", 60, 0, 6.238, 60, ylow, yhigh}, "phase", "dtime");
    dtime_phase->FitSlicesY();
    

    TH1F * mean  = (TH1F*) gDirectory->Get("dtime_phase_1");
    TH1F * sigma = (TH1F*) gDirectory->Get("dtime_phase_2");
    mean->Draw();
    for (int i = 1; i < mean->GetNbinsX(); i++)
    {
        mean->SetBinError(i, sigma->GetBinContent(i));
    }

    mean->SetAxisRange(2.2,2.7,"Y");
    mean->SetAxisRange(5,6.2,"Y");
    TF1 * fsine = (TF1* ) new TF1("fsine", "[0]*sin([1]*x+[2])+[3]", 0, 6.238);
    fsine->SetParameters(0.005, 0.9, 0., 3.);
    fsine->SetParLimits(1, 0.5, 3.);
    mean->Fit(fsine);
    mean->Draw();

    dtime_phase->Draw("colz");
    fsine->Draw("same");
    c->Draw();
    c->SaveAs(Form("%s/%i/ECAL_vs_MCP_dt_vs_phase_sinefit.pdf",path.Data(), run));
    
    fn = fn.DefineSlotEntry("dtime_corr", 
                            [&mean](unsigned int,  ULong64_t, double dtime, double phase) { 
                                return dtime-mean->GetBinContent(mean->FindBin(phase)); 
                            }, 
                            {"dtime", "phase"});
    auto dtime_phase_corr = fn.Histo2D({"dtime_phase_corr", ";APD sampling phase (ns); #Deltat_{APD-MCP}", 60, 0, 6.238, 60, -0.6, 0.6}, "phase", "dtime_corr");
    dtime_phase_corr->Draw("colz");
    c->Draw();
    c->SaveAs(Form("%s/%i/ECAL_vs_MCP_dt_vs_phase_after.pdf",path.Data(), run));
    if (debug)
    {
        vector<tuple< TString, TString, int, double, double >> tuples1d; 
        tuples1d.push_back(make_tuple("X", "X" ,60, -20, 20));
        tuples1d.push_back(make_tuple("Y", "Y" ,60, -20, 20));
        tuples1d.push_back(make_tuple("dtime_corr", "dtime_corr" ,60, -.6, .6));

        vector<tuple< TString, TString, TString, int, double, double, int, double, double > >  tuples2d;
        tuples2d.push_back(make_tuple("dtime_corr_phase","dtime_corr","phase", 25, 0, 6.238, 25, -.6, .6));
        tuples2d.push_back(make_tuple("dtime_phase","dtime","phase", 25, 0, 6.238, 25, ylow, yhigh));
        tuples2d.push_back(make_tuple("dtime_corr_vs_amplMCP", "dtime_corr", "ampMCP",  100, 0, 3000, 60, -.6, .6)); 
        tuples2d.push_back(make_tuple("dtime_corr_vs_ampl", "dtime_corr", "amp",  100, 0, 3000, 60, -.6, .6)); 
        tuples2d.push_back(make_tuple("dtime_corr_vs_time", "dtime_corr", "time",  100, 20, 100,  60, -.6, .6)); 
        tuples2d.push_back(make_tuple("dtime_corr_vs_timeMCP", "dtime_corr", "timeMCP",  100, 20, 40,  60, -.6, .6)); 
        tuples2d.push_back(make_tuple("dtime_corr_vs_timeCLK", "dtime_corr", "timeCLK",  100, 30, 40,  60, -.6, .6)); 
        tuples2d.push_back(make_tuple("dtime_corr_vs_maxtimeMCP", "dtime_corr", "maxtimeMCP",  100, 20, 100,  60, -.6, .6)); 
        tuples2d.push_back(make_tuple("dtime_corr_vs_maxtimeCLK", "dtime_corr", "maxtimeCLK",  100, 20, 200,  60, -.6, .6)); 
        tuples2d.push_back(make_tuple("dtime_corr_vs_ampl", "dtime_corr", "amp" ,100, 0, 3000, 60, -.6, .6));
        tuples2d.push_back(make_tuple("dtime_corr_vs_spill", "dtime_corr", "spill" ,150, 0, 150, 60, -.6, .6));
        tuples2d.push_back(make_tuple("dtime_corr_vs_X", "dtime_corr", "X" ,60, -20, 20, 60, -.6, .6));
        tuples2d.push_back(make_tuple("dtime_corr_vs_Y", "dtime_corr", "Y" ,60, -20, 20, 60, -.6, .6));
        tuples2d.push_back(make_tuple("dtime_corr_vs_gain", "dtime_corr", "gainxtal", 11, 0, 11, 60, .6, .6));

        // Fixme: rdataframe crashes with fitResult members, use python version temporarly
        //tuples.push_back(make_tuple("dtime_corr_vs_trackX", "dtime_corr", "track_tree.fitResult.x()" ,60, -20, 20, 60, -.6, .6));
        //tuples.push_back(make_tuple("dtime_corr_vs_trackY", "dtime_corr", "track_tree.fitResult.y()" ,60, -20, 20, 60, -.6, .6)); 
        //tuples.push_back(make_tuple("trackX_vs_trackY", "track_tree.fitResult.x()", "track_tree.fitResult.y()", 60, -20, 20, 60, -20, 20));

        for (auto [name, var, bins, low, high] : tuples1d)
        {
            auto histo = fn.Histo1D({name.Data(), Form("; %s ; %s ", var.Data()), bins, low, high}, var);
            histo->Draw("hist");
            c->Draw();
            c->SaveAs(Form("/eos/user/c/cbasile/www/ECAL_TB2021/my_templates/%i/skimmed/%s.pdf", run, name.Data()));
            c->SaveAs(Form("/eos/user/c/cbasile/www/ECAL_TB2021/my_templates/%i/skimmed/%s.png", run, name.Data()));
        }

        
        for (auto [name, yvar, xvar, xbins, xlow, xhigh, ybins, ylow, yhigh] : tuples2d)
        {
            auto histo = fn.Histo2D({name.Data(), Form("; %s ; %s ", xvar.Data(), yvar.Data()),  xbins, xlow, xhigh, ybins, ylow, yhigh}, xvar, yvar);
            histo->Draw("colz");
            c->Draw();
            c->SaveAs(Form("/eos/user/c/cbasile/www/ECAL_TB2021/my_templates/%i/skimmed/%s.pdf", run, name.Data()));
            c->SaveAs(Form("/eos/user/c/cbasile/www/ECAL_TB2021/my_templates/%i/skimmed/%s.png", run, name.Data()));
        }
    }
    
	 fs::path out_path = Form("%s/%i/templ", path.Data(), run);
    cout << " the directory exists ? " << fs::exists(out_path) << endl;
    if (!fs::exists(out_path)) fs::create_directory(Form("%s/%i/templ", path.Data(), run));
    cout << " the directory exists ? " << fs::exists(out_path) << endl;
    if (save_friend){
        ROOT::RDF::RNode corr = df;
        //corr = corr.Define("dtime", "digi_t.fit_time[C3_T]-fit_time[MCP1]+fit_time[CLK]-int((digi_t.fit_time[C3_T]-fit_time[MCP1]+fit_time[CLK])/6.238)*6.238")
        //    .Define("phase", "digi_t.fit_time[C3_T]-int(digi_t.fit_time[C3_T]/6.238)*6.238");

        corr = corr.Define("dtime", "digi_t.time_max[C3_T]-fit_time[MCP1]+fit_time[CLK]-int((digi_t.time_max[C3_T]-fit_time[MCP1]+fit_time[CLK])/6.238)*6.238")
            .Define("phase", "digi_t.time_max[C3_T]-int(digi_t.time_max[C3_T]/6.238)*6.238");
        
        corr = corr.DefineSlotEntry("dtime_corr", 
                                    [&mean](unsigned int,  ULong64_t, double dtime, double phase) { 
                                        return dtime-mean->GetBinContent(mean->FindBin(phase)); 
                                    }, 
                                    {"dtime", "phase"});
                
        corr.Snapshot("dtime_corr", Form("%s/%i/templ/dtime_corr.root",path.Data(), run), {"dtime_corr"});
    }
    
    auto histos = new TFile(Form("%s/%i/templ/phase_correction.root", path.Data(), run), "RECREATE");
    dtime_phase->Write();
    dtime_phase_corr->Write();
    mean->SetTitle("corr");
    mean->Write();
    histos->Close();
    cout << Form("... dtime vs phase histograms saved in %s/%i/templ/phase_correction.root\n", path.Data(), run) << endl ;
    return 0;
}
