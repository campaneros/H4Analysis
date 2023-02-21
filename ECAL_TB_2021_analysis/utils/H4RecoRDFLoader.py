import PyRDF
import ROOT

def LoadH4RecoData(files=[]):
    """
    Load correctly H4 reco trees (and friends) into a ROOT RDataFrame (using PyRDF)
    """
    
    h4t_list = {}
    for fname in files:
        f = ROOT.TFile.Open(fname)
        if f and f.GetListOfKeys().FindObject('h4'):
            if len(h4t_list)==0:
                h4t_list['h4'] = ROOT.TChain('h4')
                for ft in f.Get('h4').GetListOfFriends():
                    h4t_list[ft.GetName()] = ROOT.TChain(ft.GetName())
                    h4t_list['h4'].AddFriend(h4t_list[ft.GetName()])
            for name, t in h4t_list.items():
                t.Add(fname)
            f.Close()
    
    return PyRDF.RDataFrame(h4t_list['h4'])
