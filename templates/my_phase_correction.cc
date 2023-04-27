// g++ templates/my_phase_correction.cc -O3 -std=c++17 -lstdc++fs `root-config --libs --cflags` -o bin/my_phase_correction.exe
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
    bool save_friend = false; 
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
        selection = Form("trg == PHYS && digi.fit_ampl[C2]>%i && fit_ampl[MCP1]>120 && digi.fit_ampl[C2]<%i", minamp, maxamp);
    else
        selection = Form("trg == PHYS && digi.amp_max[C2]>%i && fit_ampl[MCP1]>120 && digi.amp_max[C2]<%i", minamp, maxamp);

    cout << Form("Selection: %s", selection) <<endl; 
    cout << "Selection: " << selection << endl;

    ROOT::RDF::RNode fn = df;
    
    if (iter)
        fn = df.Define("dtime", "digi.fit_time[C2]-fit_time[MCP1]+fit_time[CLK]-int((digi.fit_time[C2]-fit_time[MCP1]+fit_time[CLK])/6.238)*6.238")
            .Define("phase", "digi_t.fit_time[C2_T]-int(digi_t.fit_time[C2_T]/6.238)*6.238")
            .Define("amp", "digi_t.fit_ampl[C2_T]")
            .Define("timeMCP", "fit_time[MCP1]")
            .Define("timeCLK", "fit_time[CLK]")
            .Define("maxtime", "time_max[C2_T]")
            .Define("maxtimeCLK", "time_max[CLK]")
            .Define("maxtimeMCP", "time_max[MCP1]")
            .Define("ampMCP", "amp_max[MCP1]")
            .Define("gainxtal", "gain[C2_T]");
    else
        fn = df.Define("dtime", "digi.time_max[C2]-fit_time[MCP1]+fit_time[CLK]-int((digi.time_max[C2]-fit_time[MCP1]+fit_time[CLK])/6.238)*6.238")
            .Define("MCPtime", "digi.time_max[MCP]-int(digi.time_max[MCP]/6.238)*6.238")
            .Define("phase", "digi.time_max[C2]-int(digi.time_max[C2]/6.238)*6.238")
            .Define("phaseCLK", "int(digi.time_max[MCP]/6.238)*6.238")
            .Define("amp", "digi.amp_max[C2]")
            .Define("timeMCP", "fit_time[MCP1]")
            .Define("timeCLK", "fit_time[CLK]")
            .Define("maxtime", "time_max[C2_T]")
            .Define("maxtimeCLK", "time_max[CLK]")
            .Define("maxtimeMCP", "time_max[MCP1]")
            .Define("ampMCP", "amp_max[MCP1]")
            .Define("gainxtal", "gain[C2_T]");


    fn = fn.Filter(selection, "selection");

    // make phase correction
    auto c = new TCanvas("c", "c", 600, 600);
    auto dtime_phase = fn.Histo2D({"dtime_phase", ";APD sampling phase (ns); #Deltat_{APD-MCP}", 60, 0, 6.238, 60, 0., 1.}, "phase", "dtime");
    auto MCPvsCLK_time= fn.Histo2D({"MCPvsCLK_time", ";clock phase (ns); t{MCP}", 60, 0, 6.238, 60, 0., 1.}, "MCPtime", "dtime");
    //dtime_phase->FitSlicesY();
    //

    //TH1F * mean  = (TH1F*) gDirectory->Get("dtime_phase_1");
    //TH1F * sigma = (TH1F*) gDirectory->Get("dtime_phase_2");
    //mean->Draw();
    //for (int i = 1; i < mean->GetNbinsX(); i++)
    //{
    //    mean->SetBinError(i, sigma->GetBinContent(i));
    //}

    //mean->SetAxisRange(2.2,2.7,"Y");
    //mean->SetAxisRange(5,6.2,"Y");
    //TF1 * fsine = (TF1* ) new TF1("fsine", "[0]*sin([1]*x+[2])+[3]", 0, 6.238);
    //fsine->SetParameters(0.005, 0.9, 0., 3.);
    //fsine->SetParLimits(1, 0.5, 2.);
    //mean->Fit(fsine);
    //mean->Draw();

    dtime_phase->Draw("colz");
    //fsine->Draw("same");
    c->Draw();
    c->SaveAs(Form("%s/%i/my_ECAL_vs_MCP_dt_vs_phase_sinefit.pdf",path.Data(), run));
    
    //fn = fn.DefineSlotEntry("dtime_corr", 
    //                        [&mean](unsigned int,  ULong64_t, double dtime, double phase) { 
    //                            return dtime-mean->GetBinContent(mean->FindBin(phase)); 
    //                        }, 
    //                        {"dtime", "phase"});
    //auto dtime_phase_corr = fn.Histo2D({"dtime_phase_corr", ";APD sampling phase (ns); #Deltat_{APD-MCP}", 60, 0, 6.238, 60, -0.6, 0.6}, "phase", "dtime_corr");
    //dtime_phase_corr->Draw("colz");
    //c->Draw();
    //c->SaveAs(Form("%s/%i/ECAL_vs_MCP_dt_vs_phase_after.pdf",path.Data(), run));
    //
    fs::path out_path = Form("%s/%i/my_templ", path.Data(), run);
    cout << " the directory exists ? " << fs::exists(out_path) << endl;
    if (!fs::exists(out_path)) fs::create_directory(Form("%s/%i/my_templ", path.Data(), run));
    cout << " the directory exists ? " << fs::exists(out_path) << endl;
    //if (save_friend){
    //    ROOT::RDF::RNode corr = df;
    //    //corr = corr.Define("dtime", "digi_t.fit_time[C2_T]-fit_time[MCP1]+fit_time[CLK]-int((digi_t.fit_time[C2_T]-fit_time[MCP1]+fit_time[CLK])/6.238)*6.238")
    //    //    .Define("phase", "digi_t.fit_time[C2_T]-int(digi_t.fit_time[C2_T]/6.238)*6.238");

    //    corr = corr.Define("dtime", "digi_t.time_max[C2_T]-fit_time[MCP1]+fit_time[CLK]-int((digi_t.time_max[C2_T]-fit_time[MCP1]+fit_time[CLK])/6.238)*6.238")
    //        .Define("phase", "digi_t.time_max[C2_T]-int(digi_t.time_max[C2_T]/6.238)*6.238");
    //    
    //    corr = corr.DefineSlotEntry("dtime_corr", 
    //                                [&mean](unsigned int,  ULong64_t, double dtime, double phase) { 
    //                                    return dtime-mean->GetBinContent(mean->FindBin(phase)); 
    //                                }, 
    //                                {"dtime", "phase"});
    //            
    //    corr.Snapshot("dtime_corr", Form("%s/%i/templ/dtime_corr.root",path.Data(), run), {"dtime_corr"});
    //}
    
    auto histos = new TFile(Form("%s/%i/my_templ/phase_correction.root", path.Data(), run), "RECREATE");
    dtime_phase->Write();
    //dtime_phase_corr->Write();
    //mean->SetTitle("corr");
    //mean->Write();
    histos->Close();
    cout << Form("... dtime vs phase histograms saved in %s/%i/templ/phase_correction.root\n", path.Data(), run) << endl ;
    return 0;
}
