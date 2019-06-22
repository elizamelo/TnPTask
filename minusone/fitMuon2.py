import FWCore.ParameterSet.Config as cms
import sys, os, shutil
from optparse import OptionParser
### USAGE: cmsRun fitMuonID.py TEST tight loose mc mc_all
###_id: tight, loose, medium, soft

#_*_*_*_*_*_
#Read Inputs
#_*_*_*_*_*_

def FillNumDen(num, den):
    '''Declares the needed selections for a givent numerator, denominator'''

    #Define the mass distribution
    if den == "highptid" or den == "trkhighptid":
        if 'mass_up' in sample:
            process.TnP_MuonID.Variables.pair_newTuneP_mass = cms.vstring("Tag-muon Mass", _mrange, "140", "GeV/c^{2}")
            print 'SISTEMATIC STUDIES: mass_up upper edge = 140 GeV'
        elif 'mass_down' in sample:
            process.TnP_MuonID.Variables.pair_newTuneP_mass = cms.vstring("Tag-muon Mass", _mrange, "120", "GeV/c^{2}")
            print 'SISTEMATIC STUDIES: mass_down upper edge = 120 GeV'
        else:
            process.TnP_MuonID.Variables.pair_newTuneP_mass = cms.vstring("Tag-muon Mass", _mrange, "130", "GeV/c^{2}")
    else:
        if 'mass_up' in sample:
            process.TnP_MuonID.Variables.mass = cms.vstring("Tag-muon Mass", _mrange, "140", "GeV/c^{2}")
            print 'SISTEMATIC STUDIES: mass_up upper edge = 140 GeV'
        elif 'Charmonium' in sample:
             process.TnP_MuonID.Variables.mass = cms.vstring("Tag-muon Mass", _mrange,"3.3","GeV/c^{2}")
        elif 'mass_down' in sample:
            process.TnP_MuonID.Variables.mass = cms.vstring("Tag-muon Mass", _mrange, "120", "GeV/c^{2}")
            print 'SISTEMATIC STUDIES: mass_up upper edge = 120 GeV'
        else:
            process.TnP_MuonID.Variables.mass = cms.vstring("Tag-muon Mass", _mrange, "130", "GeV/c^{2}")
        #New selector:





    if num == "looseid":
        process.TnP_MuonID.Categories.CutBasedIdLoose  = cms.vstring("PassLooseid", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Expressions.CutBasedIdLooseVar = cms.vstring("CutBasedIdLooseVar", "CutBasedIdLoose==1", "CutBasedIdLoose")
        process.TnP_MuonID.Cuts.LooseCutid  = cms.vstring("LooseCutid", "CutBasedIdLooseVar", "0.5")
    elif num == "mediumid":
        process.TnP_MuonID.Categories.CutBasedIdMedium  = cms.vstring("PassMediumid", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Expressions.CutBasedIdMediumVar = cms.vstring("CutBasedIdMediumVar", "CutBasedIdMedium==1", "CutBasedIdMedium")
        process.TnP_MuonID.Cuts.MediumCutid  = cms.vstring("MediumCutid", "CutBasedIdMediumVar", "0.5")
    elif num == "mediumidprompt":
        process.TnP_MuonID.Categories.CutBasedIdMediumPrompt  = cms.vstring("PassMediumidprompt", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Expressions.CutBasedIdMediumPromptVar = cms.vstring("CutBasedIdMediumPromptVar", "CutBasedIdMediumPrompt==1", "CutBasedIdMediumPrompt")
        process.TnP_MuonID.Cuts.MediumCutidPrompt  = cms.vstring("MediumCutidPrompt", "CutBasedIdMediumPromptVar", "0.5")
    elif num == "tightid":
        process.TnP_MuonID.Categories.CutBasedIdTight  = cms.vstring("PassTightid", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Expressions.CutBasedIdTightVar = cms.vstring("CutBasedIdTightVar", "CutBasedIdTight==1", "CutBasedIdTight")
        process.TnP_MuonID.Cuts.TightCutid  = cms.vstring("TightCutid", "CutBasedIdTightVar", "0.5")
    elif num == "SIP":
        process.TnP_MuonID.Variables.SIP  = cms.vstring("SIP", "0", "2000", "")
        process.TnP_MuonID.Expressions.SIPVar = cms.vstring("SIPCut", "SIP<4.", "SIP")
        process.TnP_MuonID.Cuts.SIPCut = cms.vstring("SIPCut", "SIPVar", "0.5")
    elif num == "tightid_all":
        process.TnP_MuonID.Categories.Glb  = cms.vstring("Glb Muon", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Categories.PF  = cms.vstring("PF Muon", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Variables.glbChi2  = cms.vstring("glbChi2", "-1000", "1000", "")
        process.TnP_MuonID.Variables.glbValidMuHits  = cms.vstring("glbValidMuHits", "-1000", "1000", "")
        process.TnP_MuonID.Variables.numberOfMatchedStations  = cms.vstring("numberOfMatchedStations", "-1000", "1000", "")
        process.TnP_MuonID.Variables.dB  = cms.vstring("dB", "-1000", "1000", "")
        process.TnP_MuonID.Variables.dzPV  = cms.vstring("dzPV", "-1000", "1000", "")
        process.TnP_MuonID.Variables.tkValidPixelHits  = cms.vstring("tkValidPixelHits", "-1000", "1000", "")
        process.TnP_MuonID.Variables.tkTrackerLay  = cms.vstring("tkTrackerLay", "-1000", "1000", "")
        process.TnP_MuonID.Expressions.TightCutVar = cms.vstring("TightCut", "Glb == 1 && PF == 1 && glbChi2 < 10. && glbValidMuHits > 0 && numberOfMatchedStations > 1 && abs(dB) < 0.2 && abs(dzPV) < 0.5 && tkValidPixelHits > 0 && tkTrackerLay > 5", "Glb", "PF" , "glbChi2", "glbValidMuHits", "numberOfMatchedStations", "dB", "dzPV", "tkValidPixelHits", "tkTrackerLay")
        process.TnP_MuonID.Cuts.TightCut = cms.vstring("TightCut", "TightCutVar", "0.5")
    elif num == "tightid_Glb":
        process.TnP_MuonID.Categories.PF  = cms.vstring("PF Muon", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Variables.glbChi2  = cms.vstring("glbChi2", "-1000", "1000", "")
        process.TnP_MuonID.Variables.glbValidMuHits  = cms.vstring("glbValidMuHits", "-1000", "1000", "")
        process.TnP_MuonID.Variables.numberOfMatchedStations  = cms.vstring("numberOfMatchedStations", "-1000", "1000", "")
        process.TnP_MuonID.Variables.dB  = cms.vstring("dB", "-1000", "1000", "")
        process.TnP_MuonID.Variables.dzPV  = cms.vstring("dzPV", "-1000", "1000", "")
        process.TnP_MuonID.Variables.tkValidPixelHits  = cms.vstring("tkValidPixelHits", "-1000", "1000", "")
        process.TnP_MuonID.Variables.tkTrackerLay  = cms.vstring("tkTrackerLay", "-1000", "1000", "")
        process.TnP_MuonID.Expressions.TightCutVar = cms.vstring("TightCut", "PF == 1 && glbChi2 < 10. && glbValidMuHits > 0 && numberOfMatchedStations > 1 && abs(dB) < 0.2 && abs(dzPV) < 0.5 && tkValidPixelHits > 0 && tkTrackerLay > 5", "PF" , "glbChi2", "glbValidMuHits", "numberOfMatchedStations", "dB", "dzPV", "tkValidPixelHits", "tkTrackerLay")
        process.TnP_MuonID.Cuts.TightCut = cms.vstring("TightCut", "TightCutVar", "0.5")
    elif num == "tightid_PF":
        process.TnP_MuonID.Categories.Glb  = cms.vstring("Glb Muon", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Variables.glbChi2  = cms.vstring("glbChi2", "-1000", "1000", "")
        process.TnP_MuonID.Variables.glbValidMuHits  = cms.vstring("glbValidMuHits", "-1000", "1000", "")
        process.TnP_MuonID.Variables.numberOfMatchedStations  = cms.vstring("numberOfMatchedStations", "-1000", "1000", "")
        process.TnP_MuonID.Variables.dB  = cms.vstring("dB", "-1000", "1000", "")
        process.TnP_MuonID.Variables.dzPV  = cms.vstring("dzPV", "-1000", "1000", "")
        process.TnP_MuonID.Variables.tkValidPixelHits  = cms.vstring("tkValidPixelHits", "-1000", "1000", "")
        process.TnP_MuonID.Variables.tkTrackerLay  = cms.vstring("tkTrackerLay", "-1000", "1000", "")
        process.TnP_MuonID.Expressions.TightCutVar = cms.vstring("TightCut", "Glb == 1 && glbChi2 < 10. && glbValidMuHits > 0 && numberOfMatchedStations > 1 && abs(dB) < 0.2 && abs(dzPV) < 0.5 && tkValidPixelHits > 0 && tkTrackerLay > 5","Glb", "glbChi2", "glbValidMuHits", "numberOfMatchedStations", "dB", "dzPV", "tkValidPixelHits", "tkTrackerLay")
        process.TnP_MuonID.Cuts.TightCut = cms.vstring("TightCut", "TightCutVar", "0.5")
    elif num == "tightid_glbChi2":
        process.TnP_MuonID.Categories.Glb  = cms.vstring("Glb Muon", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Categories.PF  = cms.vstring("PF Muon", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Variables.glbValidMuHits  = cms.vstring("glbValidMuHits", "-1000", "1000", "")
        process.TnP_MuonID.Variables.numberOfMatchedStations  = cms.vstring("numberOfMatchedStations", "-1000", "1000", "")
        process.TnP_MuonID.Variables.dB  = cms.vstring("dB", "-1000", "1000", "")
        process.TnP_MuonID.Variables.dzPV  = cms.vstring("dzPV", "-1000", "1000", "")
        process.TnP_MuonID.Variables.tkValidPixelHits  = cms.vstring("tkValidPixelHits", "-1000", "1000", "")
        process.TnP_MuonID.Variables.tkTrackerLay  = cms.vstring("tkTrackerLay", "-1000", "1000", "")
        process.TnP_MuonID.Expressions.TightCutVar = cms.vstring("TightCut", "Glb == 1 && PF == 1 && glbValidMuHits > 0 && numberOfMatchedStations > 1 && abs(dB) < 0.2 && abs(dzPV) < 0.5 && tkValidPixelHits > 0 && tkTrackerLay > 5", "PF" ,"Glb", "glbValidMuHits", "numberOfMatchedStations", "dB", "dzPV", "tkValidPixelHits", "tkTrackerLay")
        process.TnP_MuonID.Cuts.TightCut = cms.vstring("TightCut", "TightCutVar", "0.5")
    elif num == "tightid_glbValidMuHits":
        process.TnP_MuonID.Categories.Glb  = cms.vstring("Glb Muon", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Categories.PF  = cms.vstring("PF Muon", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Variables.glbChi2  = cms.vstring("glbChi2", "-1000", "1000", "")
        process.TnP_MuonID.Variables.numberOfMatchedStations  = cms.vstring("numberOfMatchedStations", "-1000", "1000", "")
        process.TnP_MuonID.Variables.dB  = cms.vstring("dB", "-1000", "1000", "")
        process.TnP_MuonID.Variables.dzPV  = cms.vstring("dzPV", "-1000", "1000", "")
        process.TnP_MuonID.Variables.tkValidPixelHits  = cms.vstring("tkValidPixelHits", "-1000", "1000", "")
        process.TnP_MuonID.Variables.tkTrackerLay  = cms.vstring("tkTrackerLay", "-1000", "1000", "")
        process.TnP_MuonID.Expressions.TightCutVar = cms.vstring("TightCut", "Glb == 1 && PF == 1 && glbChi2 < 10. && numberOfMatchedStations > 1 && abs(dB) < 0.2 && abs(dzPV) < 0.5 && tkValidPixelHits > 0 && tkTrackerLay > 5", "PF" ,"Glb", "glbChi2", "numberOfMatchedStations", "dB", "dzPV", "tkValidPixelHits", "tkTrackerLay")
        process.TnP_MuonID.Cuts.TightCut = cms.vstring("TightCut", "TightCutVar", "0.5")
    elif num == "tightid_numberOfMatchedStations":
        process.TnP_MuonID.Categories.Glb  = cms.vstring("Glb Muon", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Categories.PF  = cms.vstring("PF Muon", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Variables.glbChi2  = cms.vstring("glbChi2", "-1000", "1000", "")
        process.TnP_MuonID.Variables.glbValidMuHits  = cms.vstring("glbValidMuHits", "-1000", "1000", "")
        process.TnP_MuonID.Variables.dB  = cms.vstring("dB", "-1000", "1000", "")
        process.TnP_MuonID.Variables.dzPV  = cms.vstring("dzPV", "-1000", "1000", "")
        process.TnP_MuonID.Variables.tkValidPixelHits  = cms.vstring("tkValidPixelHits", "-1000", "1000", "")
        process.TnP_MuonID.Variables.tkTrackerLay  = cms.vstring("tkTrackerLay", "-1000", "1000", "")
        process.TnP_MuonID.Expressions.TightCutVar = cms.vstring("TightCut", "Glb == 1 && PF == 1 && glbChi2 < 10. && glbValidMuHits > 0 && abs(dB) < 0.2 && abs(dzPV) < 0.5 && tkValidPixelHits > 0 && tkTrackerLay > 5", "PF" ,"Glb", "glbChi2", "glbValidMuHits", "dB", "dzPV", "tkValidPixelHits", "tkTrackerLay")
        process.TnP_MuonID.Cuts.TightCut = cms.vstring("TightCut", "TightCutVar", "0.5")
    elif num == "tightid_dB":
        process.TnP_MuonID.Categories.Glb  = cms.vstring("Glb Muon", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Categories.PF  = cms.vstring("PF Muon", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Variables.glbChi2  = cms.vstring("glbChi2", "-1000", "1000", "")
        process.TnP_MuonID.Variables.glbValidMuHits  = cms.vstring("glbValidMuHits", "-1000", "1000", "")
        process.TnP_MuonID.Variables.numberOfMatchedStations  = cms.vstring("numberOfMatchedStations", "-1000", "1000", "")
        process.TnP_MuonID.Variables.dzPV  = cms.vstring("dzPV", "-1000", "1000", "")
        process.TnP_MuonID.Variables.tkValidPixelHits  = cms.vstring("tkValidPixelHits", "-1000", "1000", "")
        process.TnP_MuonID.Variables.tkTrackerLay  = cms.vstring("tkTrackerLay", "-1000", "1000", "")
        process.TnP_MuonID.Expressions.TightCutVar = cms.vstring("TightCut", "Glb == 1 && PF == 1 && glbChi2 < 10. && glbValidMuHits > 0 && numberOfMatchedStations > 1 && abs(dzPfV) < 0.5 && tkValidPixelHits > 0 && tkTrackerLay > 5", "PF" ,"Glb", "glbChi2", "glbValidMuHits", "numberOfMatchedStations", "dzPV", "tkValidPixelHits", "tkTrackerLay")
        process.TnP_MuonID.Cuts.TightCut = cms.vstring("TightCut", "TightCutVar", "0.5")
    elif num == "tightid_dzPV":
        process.TnP_MuonID.Categories.Glb  = cms.vstring("Glb Muon", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Categories.PF  = cms.vstring("PF Muon", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Variables.glbChi2  = cms.vstring("glbChi2", "-1000", "1000", "")
        process.TnP_MuonID.Variables.glbValidMuHits  = cms.vstring("glbValidMuHits", "-1000", "1000", "")
        process.TnP_MuonID.Variables.numberOfMatchedStations  = cms.vstring("numberOfMatchedStations", "-1000", "1000", "")
        process.TnP_MuonID.Variables.dB  = cms.vstring("dB", "-1000", "1000", "")
        process.TnP_MuonID.Variables.tkValidPixelHits  = cms.vstring("tkValidPixelHits", "-1000", "1000", "")
        process.TnP_MuonID.Variables.tkTrackerLay  = cms.vstring("tkTrackerLay", "-1000", "1000", "")
        process.TnP_MuonID.Expressions.TightCutVar = cms.vstring("TightCut", "Glb == 1 && PF == 1 && glbChi2 < 10. && glbValidMuHits > 0 && numberOfMatchedStations > 1 && abs(dB) < 0.2 && tkValidPixelHits > 0 && tkTrackerLay > 5", "PF" ,"Glb", "glbChi2", "glbValidMuHits", "numberOfMatchedStations", "dB", "tkValidPixelHits", "tkTrackerLay")
        process.TnP_MuonID.Cuts.TightCut = cms.vstring("TightCut", "TightCutVar", "0.5")
    elif num == "tightid_tkValidPixelHits":
        process.TnP_MuonID.Categories.Glb  = cms.vstring("Glb Muon", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Categories.PF  = cms.vstring("PF Muon", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Variables.glbChi2  = cms.vstring("glbChi2", "-1000", "1000", "")
        process.TnP_MuonID.Variables.glbValidMuHits  = cms.vstring("glbValidMuHits", "-1000", "1000", "")
        process.TnP_MuonID.Variables.numberOfMatchedStations  = cms.vstring("numberOfMatchedStations", "-1000", "1000", "")
        process.TnP_MuonID.Variables.dB  = cms.vstring("dB", "-1000", "1000", "")
        process.TnP_MuonID.Variables.dzPV  = cms.vstring("dzPV", "-1000", "1000", "")
        process.TnP_MuonID.Variables.tkTrackerLay  = cms.vstring("tkTrackerLay", "-1000", "1000", "")
        process.TnP_MuonID.Expressions.TightCutVar = cms.vstring("TightCut", "Glb == 1 && PF == 1 && glbChi2 < 10. && glbValidMuHits > 0 && numberOfMatchedStations > 1 && abs(dB) < 0.2 && abs(dzPV) < 0.5 && tkTrackerLay > 5", "PF" ,"Glb", "glbChi2", "glbValidMuHits", "numberOfMatchedStations", "dB", "dzPV", "tkTrackerLay")
        process.TnP_MuonID.Cuts.TightCut = cms.vstring("TightCut", "TightCutVar", "0.5")
    elif num == "tightid_tkTrackerLay":
        process.TnP_MuonID.Categories.Glb  = cms.vstring("Glb Muon", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Categories.PF  = cms.vstring("PF Muon", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Variables.glbChi2  = cms.vstring("glbChi2", "-1000", "1000", "")
        process.TnP_MuonID.Variables.glbValidMuHits  = cms.vstring("glbValidMuHits", "-1000", "1000", "")
        process.TnP_MuonID.Variables.numberOfMatchedStations  = cms.vstring("numberOfMatchedStations", "-1000", "1000", "")
        process.TnP_MuonID.Variables.dB  = cms.vstring("dB", "-1000", "1000", "")
        process.TnP_MuonID.Variables.dzPV  = cms.vstring("dzPV", "-1000", "1000", "")
        process.TnP_MuonID.Variables.tkValidPixelHits  = cms.vstring("tkValidPixelHits", "-1000", "1000", "")
        process.TnP_MuonID.Expressions.TightCutVar = cms.vstring("TightCut", "Glb == 1 && PF == 1 && glbChi2 < 10. && glbValidMuHits > 0 && numberOfMatchedStations > 1 && abs(dB) < 0.2 && abs(dzPV) < 0.5 && tkValidPixelHits > 0", "PF" ,"Glb", "glbChi2", "glbValidMuHits", "numberOfMatchedStations", "dB", "dzPV", "tkValidPixelHits")
        process.TnP_MuonID.Cuts.TightCut = cms.vstring("TightCut", "TightCutVar", "0.5")
    elif num == "tightid_tkValidPixelHits_tkTrackerLay":
        process.TnP_MuonID.Categories.Glb  = cms.vstring("Glb Muon", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Categories.PF  = cms.vstring("PF Muon", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Variables.glbChi2  = cms.vstring("glbChi2", "-1000", "1000", "")
        process.TnP_MuonID.Variables.glbValidMuHits  = cms.vstring("glbValidMuHits", "-1000", "1000", "")
        process.TnP_MuonID.Variables.numberOfMatchedStations  = cms.vstring("numberOfMatchedStations", "-1000", "1000", "")
        process.TnP_MuonID.Variables.dB  = cms.vstring("dB", "-1000", "1000", "")
        process.TnP_MuonID.Variables.dzPV  = cms.vstring("dzPV", "-1000", "1000", "")
        process.TnP_MuonID.Expressions.TightCutVar = cms.vstring("TightCut", "Glb == 1 && PF == 1 && glbChi2 < 10. && glbValidMuHits > 0 && numberOfMatchedStations > 1 && abs(dB) < 0.2 && abs(dzPV) < 0.5", "PF" ,"Glb", "glbChi2", "glbValidMuHits", "numberOfMatchedStations", "dB", "dzPV")
        process.TnP_MuonID.Cuts.TightCut = cms.vstring("TightCut", "TightCutVar", "0.5")
    elif num == "tightid_glbValidMuHits_numberOfMatchedStations":
        process.TnP_MuonID.Categories.Glb  = cms.vstring("Glb Muon", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Categories.PF  = cms.vstring("PF Muon", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Variables.glbChi2  = cms.vstring("glbChi2", "-1000", "1000", "")
        process.TnP_MuonID.Variables.dB  = cms.vstring("dB", "-1000", "1000", "")
        process.TnP_MuonID.Variables.dzPV  = cms.vstring("dzPV", "-1000", "1000", "")
        process.TnP_MuonID.Variables.tkValidPixelHits  = cms.vstring("tkValidPixelHits", "-1000", "1000", "")
        process.TnP_MuonID.Variables.tkTrackerLay  = cms.vstring("tkTrackerLay", "-1000", "1000", "")
        process.TnP_MuonID.Expressions.TightCutVar = cms.vstring("TightCut", "Glb == 1 && PF == 1 && glbChi2 < 10. && abs(dB) < 0.2 && abs(dzPV) < 0.5 && tkValidPixelHits > 0 && tkTrackerLay > 5", "Glb", "PF" , "glbChi2", "dB", "dzPV", "tkValidPixelHits", "tkTrackerLay")
        process.TnP_MuonID.Cuts.TightCut = cms.vstring("TightCut", "TightCutVar", "0.5")
    elif num == "tightid_glbChi2_dB_dzPV":
        process.TnP_MuonID.Categories.Glb  = cms.vstring("Glb Muon", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Categories.PF  = cms.vstring("PF Muon", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Variables.glbValidMuHits  = cms.vstring("glbValidMuHits", "-1000", "1000", "")
        process.TnP_MuonID.Variables.numberOfMatchedStations  = cms.vstring("numberOfMatchedStations", "-1000", "1000", "")
        process.TnP_MuonID.Variables.tkValidPixelHits  = cms.vstring("tkValidPixelHits", "-1000", "1000", "")
        process.TnP_MuonID.Variables.tkTrackerLay  = cms.vstring("tkTrackerLay", "-1000", "1000", "")
        process.TnP_MuonID.Expressions.TightCutVar = cms.vstring("TightCut", "Glb == 1 && PF == 1 && glbValidMuHits > 0 && numberOfMatchedStations > 1 && tkValidPixelHits > 0 && tkTrackerLay > 5", "Glb", "PF" , "glbValidMuHits", "numberOfMatchedStations", "tkValidPixelHits", "tkTrackerLay")
        process.TnP_MuonID.Cuts.TightCut = cms.vstring("TightCut", "TightCutVar", "0.5")
    elif num == "highptid":
        process.TnP_MuonID.Categories.CutBasedIdGlobalHighPt  = cms.vstring("PassHighptid", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Expressions.CutBasedIdGlobalHighPtVar = cms.vstring("CutBasedIdGlobalHighPtVar", "CutBasedIdGlobalHighPt==1", "CutBasedIdGlobalHighPt")
        process.TnP_MuonID.Cuts.HighptCutid  = cms.vstring("HighptCutid", "CutBasedIdGlobalHighPtVar", "0.5")
    elif num == "trkhighptid":
        process.TnP_MuonID.Categories.CutBasedIdTrkHighPt  = cms.vstring("PasstrkHighptid", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Expressions.CutBasedIdTrkHighPtVar = cms.vstring("CutBasedIdTrkHighPtVar", "CutBasedIdTrkHighPt==1", "CutBasedIdTrkHighPt")
        process.TnP_MuonID.Cuts.trkHighptCutid  = cms.vstring("trkHighptCutid", "CutBasedIdTrkHighPtVar", "0.5")
    elif num == "softid":
        process.TnP_MuonID.Categories.SoftCutBasedId  = cms.vstring("PassSoftid", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Expressions.SoftCutBasedIdVar = cms.vstring("SoftCutBasedIdVar", "SoftCutBasedId==1", "SoftCutBasedId")
        process.TnP_MuonID.Cuts.SoftCutid  = cms.vstring("SoftCutid", "SoftCutBasedIdVar", "0.5")
    elif num == "softmvaid":
        process.TnP_MuonID.Categories.SoftMvaId  = cms.vstring("PassSofMvatid", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Expressions.SoftMvaIdVar = cms.vstring("SoftMvaIdVar", "SoftMvaId==1", "SoftMvaId")
        process.TnP_MuonID.Cuts.SoftMvaCutid  = cms.vstring("SoftMvaCutid", "SoftMvaIdVar", "0.5")
    elif num == "mvaloose":
        process.TnP_MuonID.Categories.MvaLoose  = cms.vstring("PassMvaLoose", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Expressions.MvaLooseVar = cms.vstring("MvaLooseVar", "MvaLoose==1", "MvaLoose")
        process.TnP_MuonID.Cuts.MvaLooseCutid  = cms.vstring("MvaLooseCutid", "MvaLooseVar", "0.5")
    elif num == "mvamedium":
        process.TnP_MuonID.Categories.MvaMedium  = cms.vstring("PassMvaMedium", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Expressions.MvaMediumVar = cms.vstring("MvaMediumVar", "MvaMedium==1", "MvaMedium")
        process.TnP_MuonID.Cuts.MvaMediumCutid  = cms.vstring("MvaMediumCutid", "MvaMediumVar", "0.5")
    elif num == "mvatight":
        process.TnP_MuonID.Categories.MvaTight  = cms.vstring("PassMvaTight", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Expressions.MvaTightVar = cms.vstring("MvaTightVar", "MvaTight==1", "MvaTight")
        process.TnP_MuonID.Cuts.MvaTightCutid  = cms.vstring("MvaTightCutid", "MvaTightVar", "0.5")
    elif num == "looseiso":
        process.TnP_MuonID.Categories.PFIsoLoose  = cms.vstring("PassLooseiso", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Expressions.PFIsoLooseVar = cms.vstring("PFIsoLooseVar", "PFIsoLoose==1", "PFIsoLoose")
        process.TnP_MuonID.Cuts.LooseCutiso  = cms.vstring("LooseCutiso", "PFIsoLooseVar", "0.5")
    elif num == "mediumiso":
        process.TnP_MuonID.Categories.PFIsoMedium  = cms.vstring("PassMediumiso", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Expressions.PFIsoMediumVar = cms.vstring("PFIsoMediumVar", "PFIsoMedium==1", "PFIsoMedium")
        process.TnP_MuonID.Cuts.MediumCutiso  = cms.vstring("MediumCutiso", "PFIsoMediumVar", "0.5")
    elif num == "tightiso":
        process.TnP_MuonID.Categories.PFIsoTight  = cms.vstring("PassTightiso", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Expressions.PFIsoTightVar = cms.vstring("PFIsoTightVar", "PFIsoTight==1", "PFIsoTight")
        process.TnP_MuonID.Cuts.TightCutiso  = cms.vstring("TightCutiso", "PFIsoTightVar", "0.5")
    elif num == "miniisotight":
        process.TnP_MuonID.Categories.MiniIsoTight  = cms.vstring("PassMiniIsoTight", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Expressions.MiniIsoTightVar = cms.vstring("MiniIsoTightVar", "MiniIsoTight==1", "MiniIsoTight")
        process.TnP_MuonID.Cuts.MiniIsoTightCut  = cms.vstring("MiniIsoTightCut", "MiniIsoTightVar", "0.5")
    elif num == "tklooseiso":
        process.TnP_MuonID.Categories.TkIsoLoose  = cms.vstring("PasstrkLooseiso", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Expressions.TkIsoLooseVar = cms.vstring("TkIsoLooseVar", "TkIsoLoose==1", "TkIsoLoose")
        process.TnP_MuonID.Cuts.TrkLooseCutiso  = cms.vstring("TrkLooseCutiso", "TkIsoLooseVar", "0.5")
    elif num == "tktightiso":
        process.TnP_MuonID.Categories.TkIsoTight  = cms.vstring("PasstrkTightiso", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Expressions.TkIsoTightVar = cms.vstring("TkIsoTightVar", "TkIsoTight==1", "TkIsoTight")
        process.TnP_MuonID.Cuts.TrkTightCutiso  = cms.vstring("TrkTightCutiso", "TkIsoTightVar", "0.5")
    elif num == "tightidhww_above20":
        process.TnP_MuonID.Categories.CutBasedIdTight  = cms.vstring("PassTightid", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Variables.dzPV  = cms.vstring("dzPV", "-1000", "1000", "")
        process.TnP_MuonID.Variables.dB  = cms.vstring("dB", "-1000", "1000", "")
        process.TnP_MuonID.Expressions.TightHWWCutVar = cms.vstring("TightHWWCutVar", "CutBasedIdTight==1 && abs(dzPV) < 0.1 && abs(dB) < 0.02", "CutBasedIdTight", "dzPV", "dB")
        process.TnP_MuonID.Cuts.TightHWWCut = cms.vstring("TightHWWCut", "TightHWWCutVar", "0.5")
    elif num == "tightidhww_below20":
        process.TnP_MuonID.Categories.CutBasedIdTight  = cms.vstring("PassTightid", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Variables.dzPV  = cms.vstring("dzPV", "-1000", "1000", "")
        process.TnP_MuonID.Variables.dB  = cms.vstring("dB", "-1000", "1000", "")
        process.TnP_MuonID.Expressions.TightHWWCutVar = cms.vstring("TightHWWCutVar", "CutBasedIdTight==1 && abs(dzPV) < 0.1 && abs(dB) < 0.01", "CutBasedIdTight", "dzPV", "dB")
        process.TnP_MuonID.Cuts.TightHWWCut = cms.vstring("TightHWWCut", "TightHWWCutVar", "0.5")
        #FOR TRACKER MUONS
    elif num == "trackermuons":
        process.TnP_MuonID.Categories.TM  = cms.vstring("PassTM", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Expressions.TMVar = cms.vstring("TMVar", "TM==1", "TM")
        process.TnP_MuonID.Cuts.TMCut  = cms.vstring("TMCut", "TMVar", "0.5")


    if den == "looseid":
        process.TnP_MuonID.Categories.CutBasedIdLoose  = cms.vstring("PassLooseid", "dummy[pass=1,fail=0]")
    elif den == "mediumid":
        process.TnP_MuonID.Categories.CutBasedIdMedium = cms.vstring("PassMediumid", "dummy[pass=1,fail=0]")
    elif den == "tightid":
        process.TnP_MuonID.Categories.CutBasedIdTight = cms.vstring("PassTightid", "dummy[pass=1,fail=0]")
    elif den == "highptid":
        process.TnP_MuonID.Categories.CutBasedIdGlobalHighPt  = cms.vstring("PassHighptid", "dummy[pass=1,fail=0]")
    elif den == "trkhighptid":
        process.TnP_MuonID.Categories.CutBasedIdTrkHighPt  = cms.vstring("PasstrkHighptid", "dummy[pass=1,fail=0]")
    # Added for low pT bins -> ID / trackerMuons
    elif den == "trackermuons":
        process.TnP_MuonID.Categories.TM  = cms.vstring("PassTM", "dummy[pass=1,fail=0]")
    elif den == "tightidhww":
        process.TnP_MuonID.Variables.dzPV  = cms.vstring("dzPV", "-1000", "1000", "")
        process.TnP_MuonID.Variables.dB  = cms.vstring("dB", "-1000", "1000", "")
        process.TnP_MuonID.Categories.CutBasedIdTight = cms.vstring("Tight Id. HWW Muon", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Expressions.Tight2012_zIPdBCutVar = cms.vstring("Tight2012_zIPdBCut", "CutBasedIdTight == 1 && abs(dzPV) < 0.1 && abs(dB) < 0.02", "CutBasedIdTight", "dzPV", "dB")
        process.TnP_MuonID.Cuts.Tight2012_zIPdBCut = cms.vstring("Tight2012_zIPdBCut", "Tight2012_zIPdBCutVar", "0.5")
    elif den == "tightidhww_above20":
        process.TnP_MuonID.Categories.CutBasedIdTight  = cms.vstring("PassTightid", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Variables.dzPV  = cms.vstring("dzPV", "-1000", "1000", "")
        process.TnP_MuonID.Variables.dB  = cms.vstring("dB", "-1000", "1000", "")
        process.TnP_MuonID.Expressions.TightHWWCutVar = cms.vstring("TightHWWCutVar", "CutBasedIdTight==1 && abs(dzPV) < 0.1 && abs(dB) < 0.02", "CutBasedIdTight", "dzPV", "dB")
        process.TnP_MuonID.Cuts.TightHWWCut = cms.vstring("TightHWWCut", "TightHWWCutVar", "0.5")
    elif den == "tightidhww_below20":
        process.TnP_MuonID.Categories.CutBasedIdTight  = cms.vstring("PassTightid", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Variables.dzPV  = cms.vstring("dzPV", "-1000", "1000", "")
        process.TnP_MuonID.Variables.dB  = cms.vstring("dB", "-1000", "1000", "")
        process.TnP_MuonID.Expressions.TightHWWCutVar = cms.vstring("TightHWWCutVar", "CutBasedIdTight==1 && abs(dzPV) < 0.1 && abs(dB) < 0.01", "CutBasedIdTight", "dzPV", "dB")
        process.TnP_MuonID.Cuts.TightHWWCut = cms.vstring("TightHWWCut", "TightHWWCutVar", "0.5")
    elif den == "closertracks":
        process.TnP_MuonID.Variables.dB  = cms.vstring("dB", "-1000", "1000", "")
        process.TnP_MuonID.Variables.dzPV  = cms.vstring("dzPV", "-1000", "1000", "")
        process.TnP_MuonID.Expressions.TightCutVar = cms.vstring("TightCut", "abs(dB) < 0.2 && abs(dzPV) < 0.5","dB", "dzPV")
        process.TnP_MuonID.Cuts.TightCut = cms.vstring("TightCut", "TightCutVar", "0.5")
        

                                    
def FillVariables(par):
    '''Declares only the parameters which are necessary, no more'''

    if par == 'newpt' or 'newpt_eta':
        process.TnP_MuonID.Variables.pair_newTuneP_probe_pt = cms.vstring("muon p_{T} (tune-P)", "0", "1000", "GeV/c")
    if par == 'eta':
        process.TnP_MuonID.Variables.eta  = cms.vstring("muon #eta", "-2.5", "2.5", "")
    if par == 'pt' or 'pt_eta':
        process.TnP_MuonID.Variables.pt  = cms.vstring("muon p_{T}", "0", "1000", "GeV/c")
    if par == 'vtx_eta':
        process.TnP_MuonID.Variables.tag_nVertices   = cms.vstring("Number of vertices", "0", "999", "")
        process.TnP_MuonID.Variables.abseta  = cms.vstring("muon #|eta|", "0", "2.4", "")
    if par == 'pt_eta' or 'newpt_eta':
#        process.TnP_MuonID.Variables.abseta  = cms.vstring("muon #|eta|", "0", "2.4", "")
        if 'above20' in num:
            process.TnP_MuonID.Variables.eta  = cms.vstring("muon #eta", "-2.4", "2.4", "")
            print 'hola'
        elif 'below20' in num:
            process.TnP_MuonID.Variables.eta  = cms.vstring("muon #eta", "-2.4", "2.4", "")
#            process.TnP_MuonID.Variables.abseta  = cms.vstring("muon #|eta|", "0", "2.4", "")
        else:
            process.TnP_MuonID.Variables.abseta  = cms.vstring("muon #|eta|", "0", "2.4", "")
    if par == 'tag_instLumi':
        process.TnP_MuonID.Variables.tag_instLumi  = cms.vstring("Inst. Lumi [10E30]", "0", "15", "")
    if par == 'pair_deltaR':
        process.TnP_MuonID.Variables.pair_deltaR  = cms.vstring("deltaR", "0", "4", "")
    if par == 'vtx':
        print 'I filled it'
        process.TnP_MuonID.Variables.tag_nVertices   = cms.vstring("Number of vertices", "0", "999", "")

def FillBin(par):
    '''Sets the values of the bin paramters and the bool selections on the denominators'''

    #Parameter 
    if par == 'newpt_eta':
        DEN.pair_newTuneP_probe_pt = cms.vdouble(15, 20, 25, 30, 40, 50, 60, 120) 
        DEN.abseta = cms.vdouble( 0., 0.9, 1.2, 2.1, 2.4)
    elif par == 'newpt':
        DEN.pair_newTuneP_probe_pt = cms.vdouble(20, 25, 30, 40, 50, 60, 120)
    elif par == 'eta':
        DEN.eta = cms.vdouble(-2.4, -2.1, -1.6, -1.2, -0.9, -0.3, -0.2, 0.2, 0.3, 0.9, 1.2, 1.6, 2.1, 2.4)
    elif par == 'pt':
        DEN.pt = cms.vdouble(20, 25, 30, 40, 50, 60, 120)
#        DEN.pt = cms.vdouble(2.0, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0, 4.5, 5.0, 6.0, 8.0, 10.0, 15.0, 20.0, 25.0, 30.0, 40.0, 50.0, 60.0, 120.0, 200.0, 300.0, 500.0, 700.0, 1200.0)
    elif par == 'pair_deltaR':
        DEN.pair_deltaR = cms.vdouble(0., 0.4, 0.8, 1.2, 1.6, 2.0, 2.4, 2.8, 3.2, 5.0)
    elif par == 'tag_instLumi':
        DEN.tag_instLumi = cms.vdouble(1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600, 3800, 4000, 4200, 4400, 4600, 4800, 5000, 5200, 5400, 5600, 5800, 6000, 6200, 6400, 6600, 6800, 7000, 7200, 7400, 7600, 7800, 8000, 8200, 8400, 8600, 8800, 9000, 9200, 9400, 9600, 9800, 10000, 10200, 10400, 10600, 10800, 11000) # for runs BCD 
    elif par == 'vtx_eta':
        DEN.abseta = cms.vdouble(0., 0.9, 1.2, 2.1, 2.4)
        DEN.tag_nVertices = cms.vdouble(10.5,14.5,18.5,22.5,26.5,30.5,34.5,50.5)
        
    elif par == 'pt_eta':
#        DEN.pt = cms.vdouble(10, 20, 25, 30, 40, 50, 60, 120)
#        DEN.pt = cms.vdouble(20, 25, 30, 40, 50, 60, 120)
#        DEN.abseta = cms.vdouble( 0., 0.9, 1.2, 2.1, 2.4)
        if 'above20' in num:
            print 'hola'
            DEN.pt = cms.vdouble(20,25,30,40,60,100,200)
            DEN.eta = cms.vdouble(-2.4,-2.1,-1.6,-1.2,-0.8,-0.3,-0.20,0.0,0.2,0.3,0.8,1.2,1.6,2.1,2.4)
#            DEN.abseta = cms.vdouble(0.,0.2,0.3,0.8,1.2,1.6,2.1,2.4)
        elif 'below20' in num:
#            DEN.pt = cms.vdouble(10,13,16,20)
            DEN.pt = cms.vdouble(10,15,20)
#            DEN.abseta = cms.vdouble(0.,0.2,0.3,0.8,1.2,1.6,2.1,2.4)
            DEN.eta = cms.vdouble(-2.4,-2.1,-1.6,-1.2,-0.8,-0.3,-0.20,0.2,0.3,0.8,1.2,1.6,2.1,2.4)
        else:
            DEN.pt = cms.vdouble(15, 20, 25, 30, 40, 50, 60, 120)
#        DEN.abseta = cms.vdouble( 0., 0.9, 1.2, 2.1, 2.4)
            DEN.abseta = cms.vdouble(0., 0.9, 1.2, 2.1, 2.4)

        if 'above20' in den:
            DEN.pt = cms.vdouble(20,25,30,40,60,100,200)
            DEN.eta = cms.vdouble(-2.4,-2.1,-1.6,-1.2,-0.8,-0.3,-0.20,0.0,0.2,0.3,0.8,1.2,1.6,2.1,2.4)
#            DEN.abseta = cms.vdouble(0.,0.2,0.3,0.8,1.2,1.6,2.1,2.4)
        elif 'below20' in den:
            DEN.pt = cms.vdouble(10,15,20)
#            DEN.abseta = cms.vdouble(0.,0.2,0.3,0.8,1.2,1.6,2.1,2.4)
#            DEN.abseta = cms.vdouble(0.,0.2,0.3,0.8,1.2,1.6,2.1,2.4)
            DEN.eta = cms.vdouble(-2.4,-2.1,-1.6,-1.2,-0.8,-0.3,-0.20,0.2,0.3,0.8,1.2,1.6,2.1,2.4)
        else:
            DEN.pt = cms.vdouble(15, 20, 25, 30, 40, 50, 60, 120)
#        DEN.abseta = cms.vdouble( 0., 0.9, 1.2, 2.1, 2.4)
            DEN.abseta = cms.vdouble(0., 0.9, 1.2, 2.1, 2.4)

        if 'Charmonium' in sample:
#            DEN.pt = cms.vdouble(10,20,20.01)
            DEN.pt = cms.vdouble(10,13,16)
#            DEN.abseta = cms.vdouble(0.,0.2,0.3,0.8,1.2,1.6,2.1,2.4)
            DEN.eta = cms.vdouble(-0.3,-0.20,0.0,0.2,0.3)
            
        # else:
        #     DEN.pt = cms.vdouble(20,25,30,40,60,100,200)
        #     DEN.abseta = cms.vdouble(0.,0.2,0.3,0.8,1.2,1.6,2.1,2.4)

    elif par == 'vtx':
        print 'I filled it also asdf'
        DEN.tag_nVertices = cms.vdouble(0.5,2.5,4.5,6.5,8.5,10.5,12.5,14.5,16.5,18.5,20.5,22.5,24.5,26.5,28.5,30.5,32.5,34.5,36.5,38.5,40.5,42.5,44.5,46.5,48.5,50.5,52.5,54.5)
# first_single       DEN.tag_nVertices = cms.vdouble(10.5,14.5,18.5,22.5,26.5,30.5,34.5,50.5)
        #DEN.tag_nVertices = cms.vdouble(6.5,10.5,14.5,18.5,22.5,26.5,30.5,34.5,50.5)

 #Selections
    if den == "gentrack": pass
    elif den == "trackermuons": DEN.TM = cms.vstring("pass") #For low pT ID efficiencies
    elif den == "looseid": DEN.CutBasedIdLoose = cms.vstring("pass")
    elif den == "mediumid": DEN.CutBasedIdMedium = cms.vstring("pass")
    elif den == "tightid": DEN.CutBasedIdTight = cms.vstring("pass")
    elif den == "highptid": DEN.CutBasedIdGlobalHighPt = cms.vstring("pass")
    elif den == "trkhighptid": DEN.CutBasedIdTrkHighPt = cms.vstring("pass")
    elif den == "tightidhww_above20":
        DEN.CutBasedIdTight = cms.vstring("pass")
        DEN.dzPV = cms.vdouble(-0.1, 0.1)
        DEN.dB = cms.vdouble(-0.02, 0.02)
    elif den == "tightidhww_below20":
        DEN.CutBasedIdTight = cms.vstring("pass")
        DEN.dzPV = cms.vdouble(-0.1, 0.1)
        DEN.dB = cms.vdouble(-0.01, 0.01)
    elif den == "closertracks":
        DEN.dzPV = cms.vdouble(-0.5, 0.5)
        DEN.dB = cms.vdouble(-0.2, 0.2)
        

args = sys.argv[1:]
iteration = ''
if len(args) > 1: iteration = args[1]
print "The iteration is", iteration
num = 'tight'
if len(args) > 2: num = args[2]
print 'The num is', num 
den = 'tight'
if len(args) > 3: den = args[3]
print 'The den is', den 
scenario = "data_all"
if len(args) > 4: scenario = args[4]
print "Will run scenario ", scenario
sample = 'data'
if len(args) > 5: sample = args[5]
print 'The sample is', sample
if len(args) > 6: par = args[6]
print 'The binning is', par 
bgFitFunction = 'default'
if len(args) > 7: bgFitFunction = args[7]
if bgFitFunction == 'CMSshape':
    print 'Will use the CMS shape to fit the background'
elif bgFitFunction == 'custom':
    print 'Will experiment with custom fit functions'
else:
    print 'Will use the standard fit functions for the backgroud'


process = cms.Process("TagProbe")
process.load('FWCore.MessageService.MessageLogger_cfi')
process.source = cms.Source("EmptySource")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

if not num  in ['looseid', 'mediumid', 'mediumidprompt', 'tightid', 'tightid_all', 'tightid_Glb', 'tightid_PF' , 'tightid_glbChi2', 'tightid_glbValidMuHits', 'tightid_numberOfMatchedStations', 'tightid_dB', 'tightid_dzPV', 'tightid_tkValidPixelHits', 'tightid_tkTrackerLay','tightid_tkValidPixelHits_tkTrackerLay','tightid_glbValidMuHits_numberOfMatchedStations','tightid_glbChi2_dB_dzPV', 'tightidhww_above20', 'tightidhww_below20', 'puppiIso', 'puppiIsoNoLep', 'combpuppiIso','muCleanerIII', 'muCleanerIV', 'highptid', 'trkhighptid', 'softid', 'softmvaid', 'mvaloose', 'mvamedium', 'mvatight', 'looseiso', 'tightiso', 'tklooseiso', 'tktightiso', 'mediumiso', 'miniisotight', 'trackermuons', 'SIP']:
    print '@ERROR: num should be in ',['looseid', 'mediumid', 'tightid', 'tightidhww', 'puppiIso', 'puppiIsoNoLep', 'combpuppiIso', 'muCleanerIII', 'muCleanerIV', 'highptid', 'looseiso', 'tightiso', 'tklooseiso', 'mediumiso'], 'You used', num, '.Abort'
    sys.exit()
if not den in ['looseid', 'mediumid', 'tightid', 'tightidhww_below20', 'tightidhww_above20', 'highptid', 'gentrack', 'trkhighptid', 'trackermuons', 'closertracks']:
    print '@ERROR: den should be',['looseid', 'mediumid', 'tightid', 'tightidhww', 'highptid'], 'You used', den, '.Abort'
    sys.exit()
if not par in  ['pt', 'eta', 'vtx', 'pt_eta', 'vtx_eta', 'newpt', 'newpt_eta', 'tag_instLumi', 'pair_deltaR']:
    print '@ERROR: par should be', ['pt', 'eta', 'vtx', 'pt_eta', 'newpt', 'newpt_eta', 'tag_instLumi', 'pair_deltaR'], 'You used', par, '.Abort'

#_*_*_*_*_*_*_*_*_*_*_*_*
#Prepare variables, den, num and fit funct
#_*_*_*_*_*_*_*_*_*_*_*_*

#Set-up the mass lower edge

# For systematic uncertainties

if 'mass_up' in sample:
    if 'iso' in num:
        _mrange = "80"
        print 'SISTEMATIC STUDIES: mass_up lower edge = 80 GeV'
    else:
        _mrange = "75"
        print 'SISTEMATIC STUDIES: mass_up lower edge = 75 GeV'

elif 'mass_down' in sample:
    if 'iso' in num:
        _mrange = "70"
        print 'SISTEMATIC STUDIES: mass_down lower edge = 70 GeV'
    else:
        _mrange = "65"
        print 'SISTEMATIC STUDIES: mass_down lower edge = 60 GeV'

# For the nominal case
elif 'Charmonium' in sample:
    _mrange = "2.9"
else: 
    if 'iso' in num:
        _mrange = "77"
    else:
        #For ID
        _mrange = "70"        



print '_mrange is', _mrange
mass_ =" mass"
if den == "highptid" or den == "trkhighptid": mass_ = "pair_newTuneP_mass"


# nbins variation for systematics
if 'nbins_up' in sample:
    nbins = 50
elif 'nbins_down' in sample:
    nbins = 30
else:
    # nominal case
    nbins = 40


Template = cms.EDAnalyzer("TagProbeFitTreeAnalyzer",
                          SplitMode = cms.uint32(500000),
                          NumCPU = cms.uint32(1),
    SaveWorkspace = cms.bool(False),


    Variables = cms.PSet(
        #essential for all den/num
        #mass = cms.vstring("Tag-muon Mass", _mrange, "130", "GeV/c^{2}"),
        #Jeta    = cms.vstring("muon #eta", "-2.5", "2.5", ""),
        ),

    Categories = cms.PSet(),
    Expressions = cms.PSet(),
    Cuts = cms.PSet(),


    PDFs = cms.PSet(
        CBPlusExpo = cms.vstring(
            "CBShape::signal(mass, mean[3.1,3.0,3.2], sigma[0.05,0.02,0.06], alpha[3., 0.5, 5.], n[1, 0.1, 100.])",
            #"Chebychev::backgroundPass(mass, {cPass[0,-0.5,0.5], cPass2[0,-0.5,0.5]})",
            #"Chebychev::backgroundFail(mass, {cFail[0,-0.5,0.5], cFail2[0,-0.5,0.5]})",
            #"Gaussian::signal(mass, mean[3.1,3.0,3.2], sigma[0.05,0.02,0.1])",
            "Exponential::backgroundPass(mass, lp[0,-5,5])",
            "Exponential::backgroundFail(mass, lf[0,-5,5])",
            "efficiency[0.9,0,1]",
            "signalFractionInPassing[0.9]"
        ),
        voigtPlusExpo = cms.vstring(
            "Voigtian::signal(mass, mean[90,80,100], width[2.495], sigma[3,1,20])".replace("mass",mass_),
            "Exponential::backgroundPass(mass, lp[0,-5,5])".replace("mass",mass_),
            "Exponential::backgroundFail(mass, lf[0,-5,5])".replace("mass",mass_),
            "efficiency[0.9,0,1]",
            "signalFractionInPassing[0.9]"
        ),
        vpvPlusExpo = cms.vstring(
            "Voigtian::signal1(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])".replace("mass",mass_),
            "Voigtian::signal2(mass, mean2[90,80,100], width,        sigma2[4,2,10])".replace("mass",mass_),
            "SUM::signal(vFrac[0.8,0,1]*signal1, signal2)",
            "Exponential::backgroundPass(mass, lp[-0.1,-1,0.1])".replace("mass",mass_),
            "Exponential::backgroundFail(mass, lf[-0.1,-1,0.1])".replace("mass",mass_),
            "efficiency[0.9,0,1]",
            "signalFractionInPassing[0.9]"
        ),
        vpvPlusExpoMin70 = cms.vstring(
            "Voigtian::signal1(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])".replace("mass",mass_),
            "Voigtian::signal2(mass, mean2[90,80,100], width,        sigma2[4,3,10])".replace("mass",mass_),
            "SUM::signal(vFrac[0.8,0.5,1]*signal1, signal2)",
            "Exponential::backgroundPass(mass, lp[-0.1,-1,0.1])".replace("mass",mass_),
            "Exponential::backgroundFail(mass, lf[-0.1,-1,0.1])".replace("mass",mass_),
            "efficiency[0.9,0.7,1]",
            "signalFractionInPassing[0.9]"
        ),
        vpvPlusCheb = cms.vstring(
            "Voigtian::signal1(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])".replace("mass",mass_),
            "Voigtian::signal2(mass, mean2[90,80,100], width,        sigma2[4,3,10])".replace("mass",mass_),
            "SUM::signal(vFrac[0.8,0.5,1]*signal1, signal2)",
            #par3
            "RooChebychev::backgroundPass(mass, {a0[0.25,0,0.5], a1[-0.25,-1,0.1],a2[0.,-0.25,0.25]})".replace("mass",mass_),
            "RooChebychev::backgroundFail(mass, {a0[0.25,0,0.5], a1[-0.25,-1,0.1],a2[0.,-0.25,0.25]})".replace("mass",mass_),
            "efficiency[0.9,0.7,1]",
            "signalFractionInPassing[0.9]"
        ),
        vpvPlusCMS = cms.vstring(
            "Voigtian::signal1(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])".replace("mass",mass_),
            "Voigtian::signal2(mass, mean2[90,80,100], width,        sigma2[4,3,10])".replace("mass",mass_),
            "SUM::signal(vFrac[0.8,0.5,1]*signal1, signal2)",
            "RooCMSShape::backgroundPass(mass, alphaPass[70.,60.,90.], betaPass[0.02, 0.01,0.1], gammaPass[0.001, 0.,0.1], peakPass[90.0])".replace("mass",mass_),
            "RooCMSShape::backgroundFail(mass, alphaFail[70.,60.,90.], betaFail[0.02, 0.01,0.1], gammaFail[0.001, 0.,0.1], peakPass)".replace("mass",mass_),
            "efficiency[0.9,0.7,1]",
            "signalFractionInPassing[0.9]"
        ),
        voigtPlusCMS = cms.vstring(
            "Voigtian::signal(mass, mean[90,80,100], width[2.495], sigma[3,1,20])".replace("mass",mass_),
            "RooCMSShape::backgroundPass(mass, alphaPass[70.,60.,90.], betaPass[0.02, 0.01,0.1], gammaPass[0.001, 0.,0.1], peakPass[90.0])".replace("mass",mass_),
            "RooCMSShape::backgroundFail(mass, alphaFail[70.,60.,90.], betaFail[0.02, 0.01,0.1], gammaFail[0.001, 0.,0.1], peakPass)".replace("mass",mass_),
            "efficiency[0.9,0.7,1]",
            "signalFractionInPassing[0.9]"
        ),
        vpvPlusCMS10_20 = cms.vstring(
            "Voigtian::signal1(mass, mean1[90,80,100], width[2.495], sigma1[1.5,1,2])".replace("mass",mass_),
            "Voigtian::signal2(mass, mean2[90,80,100], width,        sigma2[4,3,7])".replace("mass",mass_),
            "SUM::signal(vFrac[0.8,0.5,1]*signal1, signal2)",
            "RooCMSShape::backgroundPass(mass, alphaPass[70.,60.,90.], betaPass[0.02, 0.01,0.1], gammaPass[0.001, 0.,0.1], peakPass[90.0])".replace("mass",mass_),
            "RooCMSShape::backgroundFail(mass, alphaFail[70.,60.,90.], betaFail[0.02, 0.01,0.1], gammaFail[0.001, 0.,0.1], peakPass)".replace("mass",mass_),
            "efficiency[0.9,0.7,1]",
            "signalFractionInPassing[0.9]"
        ),
        vpvPlusCMSbeta0p2 = cms.vstring(
            "Voigtian::signal1(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])".replace("mass",mass_),
            "Voigtian::signal2(mass, mean2[90,80,100], width,        sigma2[4,3,10])".replace("mass",mass_),
            "RooCMSShape::backgroundPass(mass, alphaPass[70.,60.,90.], betaPass[0.001, 0.,0.1], gammaPass[0.001, 0.,0.1], peakPass[90.0])".replace("mass",mass_),
            "RooCMSShape::backgroundFail(mass, alphaFail[70.,60.,90.], betaFail[0.03, 0.02,0.1], gammaFail[0.001, 0.,0.1], peakPass)".replace("mass",mass_),
            #"RooCMSShape::backgroundPass(mass, alphaPass[70.,60.,90.], betaPass[0.001, 0.01,0.1], gammaPass[0.001, 0.,0.1], peakPass[90.0])".replace("mass",mass_),
            #"RooCMSShape::backgroundFail(mass, alphaFail[70.,60.,90.], betaFail[0.001, 0.01,0.1], gammaFail[0.001, 0.,0.1], peakPass)".replace("mass",mass_),
            "SUM::signal(vFrac[0.8,0.5,1]*signal1, signal2)",
            "efficiency[0.9,0.7,1]",
            "signalFractionInPassing[0.9]"
        ),
        voigtPlusCMSbeta0p2 = cms.vstring(
            "Voigtian::signal(mass, mean[90,80,100], width[2.495], sigma[3,1,20])".replace("mass",mass_),
            "RooCMSShape::backgroundPass(mass, alphaPass[70.,60.,90.], betaPass[0.001, 0.,0.1], gammaPass[0.001, 0.,0.1], peakPass[90.0])".replace("mass",mass_),
            "RooCMSShape::backgroundFail(mass, alphaFail[70.,60.,90.], betaFail[0.03, 0.02,0.1], gammaFail[0.001, 0.,0.1], peakPass)".replace("mass",mass_),
            "efficiency[0.9,0.7,1]",
            "signalFractionInPassing[0.9]"
        )
    ),

    binnedFit = cms.bool(True),
    binsForFit = cms.uint32(nbins),
    saveDistributionsPlot = cms.bool(False),
    Efficiencies = cms.PSet(), # will be filled later
)




if sample == "dataidABCD_nominal":
    process.TnP_MuonID = Template.clone(                                                                                                 
       InputFileNames = cms.vstring(                            
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/TnPTreeZ_17Sep2018_SingleMuon_Run2018Av2_GoldenJSON_skimmedID.root',
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/TnPTreeZ_17Sep2018_SingleMuon_Run2018Bv1_GoldenJSON_skimmedID.root',
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/TnPTreeZ_17Sep2018_SingleMuon_Run2018Cv1_GoldenJSON_skimmedID.root',
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/TnPTreeZ_SingleMuon_Run2018Dv2_GoldenJSON_Upto323523_skimmedID.root',
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/TnPTreeZ_SingleMuon_Run2018Dv2_GoldenJSON_323524_to_End.root'
            ),                                                                                                                           
        InputTreeName = cms.string("fitter_tree"),                                                                                       
        InputDirectoryName = cms.string("tpTree"),                                                                                       
        OutputFileName = cms.string("TnP_MuonISO_%s.root" % scenario),                                                                   
        Efficiencies = cms.PSet(),                                                                                                       
        )  


if sample == "mcidABCD_nominal":
    process.TnP_MuonID = Template.clone(                                                                                                 
       InputFileNames = cms.vstring(                            
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/TnPTreeZ_102XAutumn18_DYJetsToLL_M50_MadgraphMLM_skimmedID_weightedABCD.root'
            ),                                                                                                                           
        InputTreeName = cms.string("fitter_tree"),                                                                                       
        InputDirectoryName = cms.string("tpTree"),                                                                                       
        OutputFileName = cms.string("TnP_MuonISO_%s.root" % scenario),                                                                   
        Efficiencies = cms.PSet(),                                                                                                       
        )  

if sample == "dataidABCD_signalvar":
    process.TnP_MuonID = Template.clone(                                                                                                 
       InputFileNames = cms.vstring(                            
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/TnPTreeZ_17Sep2018_SingleMuon_Run2018Av2_GoldenJSON_skimmedID.root',
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/TnPTreeZ_17Sep2018_SingleMuon_Run2018Bv1_GoldenJSON_skimmedID.root',
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/TnPTreeZ_17Sep2018_SingleMuon_Run2018Cv1_GoldenJSON_skimmedID.root',
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/TnPTreeZ_SingleMuon_Run2018Dv2_GoldenJSON_Upto323523_skimmedID.root',
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/TnPTreeZ_SingleMuon_Run2018Dv2_GoldenJSON_323524_to_End.root'
            ),                                                                                                                           
        InputTreeName = cms.string("fitter_tree"),                                                                                       
        InputDirectoryName = cms.string("tpTree"),                                                                                       
        OutputFileName = cms.string("TnP_MuonISO_%s.root" % scenario),                                                                   
        Efficiencies = cms.PSet(),                                                                                                       
        )  


if sample == "mcidABCD_signalvar":
    process.TnP_MuonID = Template.clone(                                                                                                 
       InputFileNames = cms.vstring(                            
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/TnPTreeZ_102XAutumn18_DYJetsToLL_M50_MadgraphMLM_skimmedID_weightedABCD.root'
            ),                                                                                                                           
        InputTreeName = cms.string("fitter_tree"),                                                                                       
        InputDirectoryName = cms.string("tpTree"),                                                                                       
        OutputFileName = cms.string("TnP_MuonISO_%s.root" % scenario),                                                                   
        Efficiencies = cms.PSet(),                                                                                                       
        )  



if sample == "dataidABCD_nbins_up":
    process.TnP_MuonID = Template.clone(                                                                                                 
       InputFileNames = cms.vstring(                            
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/TnPTreeZ_17Sep2018_SingleMuon_Run2018Av2_GoldenJSON_skimmedID.root',
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/TnPTreeZ_17Sep2018_SingleMuon_Run2018Bv1_GoldenJSON_skimmedID.root',
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/TnPTreeZ_17Sep2018_SingleMuon_Run2018Cv1_GoldenJSON_skimmedID.root',
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/TnPTreeZ_SingleMuon_Run2018Dv2_GoldenJSON_Upto323523_skimmedID.root',
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/TnPTreeZ_SingleMuon_Run2018Dv2_GoldenJSON_323524_to_End.root'
            ),                                                                                                                           
        InputTreeName = cms.string("fitter_tree"),                                                                                       
        InputDirectoryName = cms.string("tpTree"),                                                                                       
        OutputFileName = cms.string("TnP_MuonISO_%s.root" % scenario),                                                                   
        Efficiencies = cms.PSet(),                                                                                                       
        )  


if sample == "mcidABCD_nbins_up":
    process.TnP_MuonID = Template.clone(                                                                                                 
       InputFileNames = cms.vstring(                            
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/TnPTreeZ_102XAutumn18_DYJetsToLL_M50_MadgraphMLM_skimmedID_weightedABCD.root'
            ),                                                                                                                           
        InputTreeName = cms.string("fitter_tree"),                                                                                       
        InputDirectoryName = cms.string("tpTree"),                                                                                       
        OutputFileName = cms.string("TnP_MuonISO_%s.root" % scenario),                                                                   
        Efficiencies = cms.PSet(),                                                                                                       
        )  




if sample == "dataidABCD_nbins_down":
    process.TnP_MuonID = Template.clone(                                                                                                 
       InputFileNames = cms.vstring(                            
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/TnPTreeZ_17Sep2018_SingleMuon_Run2018Av2_GoldenJSON_skimmedID.root',
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/TnPTreeZ_17Sep2018_SingleMuon_Run2018Bv1_GoldenJSON_skimmedID.root',
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/TnPTreeZ_17Sep2018_SingleMuon_Run2018Cv1_GoldenJSON_skimmedID.root',
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/TnPTreeZ_SingleMuon_Run2018Dv2_GoldenJSON_Upto323523_skimmedID.root',
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/TnPTreeZ_SingleMuon_Run2018Dv2_GoldenJSON_323524_to_End.root'
            ),                                                                                                                           
        InputTreeName = cms.string("fitter_tree"),                                                                                       
        InputDirectoryName = cms.string("tpTree"),                                                                                       
        OutputFileName = cms.string("TnP_MuonISO_%s.root" % scenario),                                                                   
        Efficiencies = cms.PSet(),                                                                                                       
        )  


if sample == "mcidABCD_nbins_down":
    process.TnP_MuonID = Template.clone(                                                                                                 
       InputFileNames = cms.vstring(                            
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/TnPTreeZ_102XAutumn18_DYJetsToLL_M50_MadgraphMLM_skimmedID_weightedABCD.root'
            ),                                                                                                                           
        InputTreeName = cms.string("fitter_tree"),                                                                                       
        InputDirectoryName = cms.string("tpTree"),                                                                                       
        OutputFileName = cms.string("TnP_MuonISO_%s.root" % scenario),                                                                   
        Efficiencies = cms.PSet(),                                                                                                       
        )  


if sample == "dataidABCD_tag_up":
    process.TnP_MuonID = Template.clone(                                                                                                 
       InputFileNames = cms.vstring(                            
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/tag_up/TnPTreeZ_17Sep2018_SingleMuon_Run2018Av2_GoldenJSON_skimmedID.root',
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/tag_up/TnPTreeZ_17Sep2018_SingleMuon_Run2018Bv1_GoldenJSON_skimmedID.root',
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/tag_up/TnPTreeZ_17Sep2018_SingleMuon_Run2018Cv1_GoldenJSON_skimmedID.root',
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/tag_up/TnPTreeZ_SingleMuon_Run2018Dv2_GoldenJSON_Upto323523_skimmedID.root',
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/tag_up/TnPTreeZ_SingleMuon_Run2018Dv2_GoldenJSON_323524_to_End.root'
            ),                                                                                                                           
        InputTreeName = cms.string("fitter_tree"),                                                                                       
        InputDirectoryName = cms.string("tpTree"),                                                                                       
        OutputFileName = cms.string("TnP_MuonISO_%s.root" % scenario),                                                                   
        Efficiencies = cms.PSet(),                                                                                                       
        )  


if sample == "mcidABCD_tag_up":
    process.TnP_MuonID = Template.clone(                                                                                                 
       InputFileNames = cms.vstring(                            
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/tag_up/TnPTreeZ_102XAutumn18_DYJetsToLL_M50_MadgraphMLM_skimmedID_weightedABCD.root'
            ),                                                                                                                           
        InputTreeName = cms.string("fitter_tree"),                                                                                       
        InputDirectoryName = cms.string("tpTree"),                                                                                       
        OutputFileName = cms.string("TnP_MuonISO_%s.root" % scenario),                                                                   
        Efficiencies = cms.PSet(),                                                                                                       
        )  


if sample == "dataidABCD_tag_down":
    process.TnP_MuonID = Template.clone(                                                                                                 
       InputFileNames = cms.vstring(                            
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/tag_down/TnPTreeZ_17Sep2018_SingleMuon_Run2018Av2_GoldenJSON_skimmedID.root',
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/tag_down/TnPTreeZ_17Sep2018_SingleMuon_Run2018Bv1_GoldenJSON_skimmedID.root',
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/tag_down/TnPTreeZ_17Sep2018_SingleMuon_Run2018Cv1_GoldenJSON_skimmedID.root',
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/tag_down/TnPTreeZ_SingleMuon_Run2018Dv2_GoldenJSON_Upto323523_skimmedID.root',
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/tag_down/TnPTreeZ_SingleMuon_Run2018Dv2_GoldenJSON_323524_to_End.root'
            ),                                                                                                                           
        InputTreeName = cms.string("fitter_tree"),                                                                                       
        InputDirectoryName = cms.string("tpTree"),                                                                                       
        OutputFileName = cms.string("TnP_MuonISO_%s.root" % scenario),                                                                   
        Efficiencies = cms.PSet(),                                                                                                       
        )  


if sample == "mcidABCD_tag_down":
    process.TnP_MuonID = Template.clone(                                                                                                 
       InputFileNames = cms.vstring(                            
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/tag_down/TnPTreeZ_102XAutumn18_DYJetsToLL_M50_MadgraphMLM_skimmedID_weightedABCD.root'
            ),                                                                                                                           
        InputTreeName = cms.string("fitter_tree"),                                                                                       
        InputDirectoryName = cms.string("tpTree"),                                                                                       
        OutputFileName = cms.string("TnP_MuonISO_%s.root" % scenario),                                                                   
        Efficiencies = cms.PSet(),                                                                                                       
        )  


if sample == "dataidABCD_mass_up":
    process.TnP_MuonID = Template.clone(                                                                                                 
       InputFileNames = cms.vstring(                            
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/mass/TnPTreeZ_17Sep2018_SingleMuon_Run2018Av2_GoldenJSON_skimmedID.root',
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/mass/TnPTreeZ_17Sep2018_SingleMuon_Run2018Bv1_GoldenJSON_skimmedID.root',
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/mass/TnPTreeZ_17Sep2018_SingleMuon_Run2018Cv1_GoldenJSON_skimmedID.root',
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/mass/TnPTreeZ_SingleMuon_Run2018Dv2_GoldenJSON_Upto323523_skimmedID.root',
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/mass/TnPTreeZ_SingleMuon_Run2018Dv2_GoldenJSON_323524_to_End.root'
            ),                                                                                                                           
        InputTreeName = cms.string("fitter_tree"),                                                                                       
        InputDirectoryName = cms.string("tpTree"),                                                                                       
        OutputFileName = cms.string("TnP_MuonISO_%s.root" % scenario),                                                                   
        Efficiencies = cms.PSet(),                                                                                                       
        )  


if sample == "mcidABCD_mass_up":
    process.TnP_MuonID = Template.clone(                                                                                                 
       InputFileNames = cms.vstring(                            
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/mass/TnPTreeZ_102XAutumn18_DYJetsToLL_M50_MadgraphMLM_skimmedID_weightedABCD.root'
            ),                                                                                                                           
        InputTreeName = cms.string("fitter_tree"),                                                                                       
        InputDirectoryName = cms.string("tpTree"),                                                                                       
        OutputFileName = cms.string("TnP_MuonISO_%s.root" % scenario),                                                                   
        Efficiencies = cms.PSet(),                                                                                                       
        )  


if sample == "dataidABCD_mass_down":
    process.TnP_MuonID = Template.clone(                                                                                                 
       InputFileNames = cms.vstring(                            
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/mass/TnPTreeZ_17Sep2018_SingleMuon_Run2018Av2_GoldenJSON_skimmedID.root',
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/mass/TnPTreeZ_17Sep2018_SingleMuon_Run2018Bv1_GoldenJSON_skimmedID.root',
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/mass/TnPTreeZ_17Sep2018_SingleMuon_Run2018Cv1_GoldenJSON_skimmedID.root',
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/mass/TnPTreeZ_SingleMuon_Run2018Dv2_GoldenJSON_Upto323523_skimmedID.root',
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/mass/TnPTreeZ_SingleMuon_Run2018Dv2_GoldenJSON_323524_to_End.root'
            ),                                                                                                                           
        InputTreeName = cms.string("fitter_tree"),                                                                                       
        InputDirectoryName = cms.string("tpTree"),                                                                                       
        OutputFileName = cms.string("TnP_MuonISO_%s.root" % scenario),                                                                   
        Efficiencies = cms.PSet(),                                                                                                       
        )  


if sample == "mcidABCD_mass_down":
    process.TnP_MuonID = Template.clone(                                                                                                 
       InputFileNames = cms.vstring(                            
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/mass/TnPTreeZ_102XAutumn18_DYJetsToLL_M50_MadgraphMLM_skimmedID_weightedABCD.root'
            ),                                                                                                                           
        InputTreeName = cms.string("fitter_tree"),                                                                                       
        InputDirectoryName = cms.string("tpTree"),                                                                                       
        OutputFileName = cms.string("TnP_MuonISO_%s.root" % scenario),                                                                   
        Efficiencies = cms.PSet(),                                                                                                       
        )  



if sample == "mcidABC_Fall18":
    process.TnP_MuonID = Template.clone(                                                                                                 
       InputFileNames = cms.vstring(                            
            '/eos/cms/store/group/phys_muon/fernanpe/TnPTrees/Run2018_94_pre3/TnPTreeZ_102X_DYJetsToLL_M50_MadgraphMLM_skimmedID_weightedABC.root'
            ),                                                                                                                           
        InputTreeName = cms.string("fitter_tree"),                                                                                       
        InputDirectoryName = cms.string("tpTree"),                                                                                       
        OutputFileName = cms.string("TnP_MuonISO_%s.root" % scenario),                                                                   
        Efficiencies = cms.PSet(),                                                                                                       
        )  





if scenario == "mc_all":
    print "Including the weight for MC"
    process.TnP_MuonID.WeightVariable = cms.string("weight")
    process.TnP_MuonID.Variables.weight = cms.vstring("weight","0","10","")


BIN = cms.PSet(
        )

print 'debug1'
Num_dic = {'looseid':'LooseID', 'mediumid':'MediumID', 'mediumidprompt':'MediumPromptID', 'tightid':'TightID', 'tightid_all':'tightID_all', 'tightid_Glb':'tightID_Glb', 'tightid_PF':'tightID_PF' , 'tightid_glbChi2':'tightID_glbChi2', 'tightid_glbValidMuHits':'tightID_glbValidMuHits', 'tightid_numberOfMatchedStations':'tightID_numberOfMatchedStations', 'tightid_dB':'tightID_dB', 'tightid_dzPV':'tightid_dzPV', 'tightid_tkValidPixelHits':'tightID_tkValidPixelHits', 'tightid_tkTrackerLay':'tightID_tkTrackerLay','tightid_tkValidPixelHits_tkTrackerLay':'tightID_tkValidPixelHits_tkTrackerLay','tightid_glbValidMuHits_numberOfMatchedStations':'tightID_glbValidMuHits_numberOfMatchedStations', 'tightid_glbChi2_dB_dzPV':'tightID_glbChi2_dB_dzPV','trkhighptid':'TrkHighPtID', 'softid':'SoftID', 'softmvaid':'SoftMVAID', 'mvaloose':'MVALoose', 'mvamedium':'MVAMedium', 'mvatight':'MVATight', 'tightidhww_above20':'TightIDHWW', 'tightidhww_below20':'TightIDHWW','puppiIso':'PuppiIso','puppiIsoNoLep':'PuppiIsoNoLep','combpuppiIso':'combPuppiIso', 'muCleanerIII':'MuonCleanerIII', 'muCleanerIV':'MuonCleanerIV', 'highptid':'HighPtID','looseiso':'LooseRelIso', 'mediumiso':'MediumISO', 'miniisotight':'MiniISOTight', 'tightiso':'TightRelIso','tklooseiso':'LooseRelTkIso', 'tktightiso':'TightRelTkIso', 'mediumiso':'MediumIso', 'trackermuons':'genTracks', 'SIP':'SIP_4'}
Den_dic = {'gentrack':'genTracks','looseid':'LooseID','mediumid':'MediumID', 'tightid':'TightIDandIPCut','tightidhww_above20':'TightHWWCut','tightidhww_below20':'TightHWWCut','highptid':'HighPtIDandIPCut', 'trkhighptid':'TrkHighPtID', 'trackermuons':'genTracks', 'closertracks':'CloseTracks'}
Sel_dic = {'looseid':'LooseCutid','mediumid':'MediumCutid','mediumidprompt':'MediumCutidPrompt', 'tightid':'TightCutid', 'tightid_all':'TightCut', 'tightid_Glb':'TightCut', 'tightid_PF':'TightCut' , 'tightid_glbChi2':'TightCut', 'tightid_glbValidMuHits':'TightCut', 'tightid_numberOfMatchedStations':'TightCut', 'tightid_dB':'TightCut', 'tightid_dzPV':'TightCut', 'tightid_tkValidPixelHits':'TightCut', 'tightid_tkTrackerLay':'TightCut', 'tightid_tkValidPixelHits_tkTrackerLay':'TightCut', 'tightid_glbValidMuHits_numberOfMatchedStations':'TightCut', 'tightid_glbChi2_dB_dzPV':'TightCut','tightidhww_above20':'TightHWWCut','tightidhww_below20':'TightHWWCut','puppiIso':'puppiIsoCut', 'puppiIsoNoLep':'puppiIsoNoLepCut','combpuppiIso':'combpuppiIsoCut','muCleanerIII':'TM_cleanMuonIIICut', 'muCleanerIV':'TM_cleanMuonIVCut', 'highptid':'HighptCutid','looseiso':'LooseCutiso','tightiso':'TightCutiso','tklooseiso':'TrkLooseCutiso', 'tktightiso':'TrkTightCutiso', 'mediumiso':'MediumCutiso', 'trkhighptid':'trkHighptCutid', 'softid':'SoftCutid', 'softmvaid':'SoftMVACutid', 'mvaloose':'MVALooseCut', 'mvamedium':'MVAMediumCut', 'mvatight':'MVATightCut', 'miniisotight':'MiniTightCutiso', 'tightiso':'TightCutiso', 'trackermuons':'TMCut', 'closertracks':'TightCut', 'SIP':'SIPCut'}
print 'debugSel'
#Par_dic = {'eta':'eta', 'pt':}

FillVariables(par)
FillNumDen(num,den)
print 'debugFill'

print 'den is', den,'dic',Den_dic[den]
print 'num is', num,'dic',Num_dic[num]
print 'par is', par

ID_BINS = [(Sel_dic[num],("NUM_%s_DEN_%s_PAR_%s"%(Num_dic[num],Den_dic[den],par),BIN))]
print 'debug5'

print Sel_dic[num]
print ("NUM_%s_DEN_%s_PAR_%s"%(Num_dic[num],Den_dic[den],par),BIN)

#_*_*_*_*_*_*_*_*_*_*_*
#Launch fit production
#_*_*_*_*_*_*_*_*_*_*_*

for ID, ALLBINS in ID_BINS:
    print 'debug1'
    X = ALLBINS[0]
    B = ALLBINS[1]
    _output = os.getcwd() + '/Efficiency' + iteration
    if not os.path.exists(_output):
        print 'Creating', '/Efficiency' + iteration,', the directory where the fits are stored.'
        os.makedirs(_output)
    if scenario == 'data_all':
        _output += '/DATA' + '_' + sample
    elif scenario == 'mc_all':
        _output += '/MC' + '_' + sample
    if not os.path.exists(_output):
        os.makedirs(_output)
    module = process.TnP_MuonID.clone(OutputFileName = cms.string(_output + "/TnP_MC_%s.root" % (X)))
    #save the fitconfig in the plot directory
    shutil.copyfile(os.getcwd()+'/fitMuon2.py',_output+'/fitMuon2.py')
    if 'signalvar' in sample:
        shape = cms.vstring("voigtPlusExpo")
        print 'debug2'
        print 'SYSTEMATIC STUDIES: the signal function will be ONE voigtian + CMSshape'
    elif 'Charmonium' in sample:
        shape = cms.vstring("CBPlusExpo") # J/Psi Fit likes 2016 studies for low pT 
    else:
    # DEFAULT FIT FUNCTION: two voingtians + Exponential
        shape = cms.vstring("vpvPlusExpo")
        print 'debug2'



    DEN = B.clone(); num_ = ID;
    FillBin(par)

    if not "iso" in num: #customize only for ID
        if bgFitFunction == 'default':
            
            # SYSTEMATIC STUDIES: signal function variation
            if 'signalvar' in sample:
                if ('pt' in X):
                    print 'SYSTEMATIC STUDIES: the signal function will be ONE voigtian + CMSshape'
                    print 'den is', den 
                    print 'num_ is ', num
                    if den == "highptid" or num == "highptid" or den == "trkhighptid" or num == "trkhighptid":
                        if (len(DEN.pair_newTuneP_probe_pt)==9 or len(DEN.pair_newTuneP_probe_pt)==8 or len(DEN.pair_newTuneP_probe_pt)==10):
                            shape = cms.vstring("voigtPlusCMS","*pt_bin0*","voigtPlusCMS","*pt_bin1*","voigtPlusCMS","*pt_bin2*","voigtPlusCMS","*pt_bin3*","voigtPlusCMSbeta0p2","*pt_bin4*","voigtPlusCMSbeta0p2","*pt_bin5*","voigtPlusCMSbeta0p2","*pt_bin6*","voigtPlusCMSbeta0p2","*pt_bin7*","voigtPlusCMSbeta0p2", "*pt_bin8*","voigtPlusCMSbeta0p2")
                        if scenario == "mc_all":
                            if (len(DEN.pair_newTuneP_probe_pt)==9 or len(DEN.pair_newTuneP_probe_pt)==8 or len(DEN.pair_newTuneP_probe_pt)==10):
                                shape = cms.vstring("voigtPlusCMSbeta0p2","*pt_bin0*","voigtPlusExpo","*pt_bin1*","voigtPlusExpo","*pt_bin2*","voigtPlusExpo","*pt_bin3*","voigtPlusExpo","*pt_bin4*","voigtPlusCMSbeta0p2","*pt_bin5*","voigtPlusCMSbeta0p2","*pt_bin6*","voigtPlusCMSbeta0p2","*pt_bin7*","voigtPlusCMSbeta0p2", "*pt_bin8*","voigtPlusCMSbeta0p2")

                    else:
                        if (len(DEN.pt)==26):
                            shape = cms.vstring("voigtPlusCMSbeta0p2")
                        if scenario == "mc_all":
                            shape = cms.vstring("voigtPlusCMSbeta0p2")

                        if (len(DEN.pt)==9 or len(DEN.pt)==8 or len(DEN.pt)==10):
                            shape = cms.vstring("voigtPlusCMS","*pt_bin0*","voigtPlusCMS","*pt_bin1*","voigtPlusCMS","*pt_bin2*","voigtPlusCMS","*pt_bin3*","voigtPlusCMSbeta0p2","*pt_bin4*","voigtPlusCMSbeta0p2","*pt_bin5*","voigtPlusCMSbeta0p2","*pt_bin6*","voigtPlusCMSbeta0p2","*pt_bin7*","voigtPlusCMSbeta0p2","*pt_bin8*","voigtPlusCMSbeta0p2")

            #FOR JPsi
            elif 'Charmonium' in sample:
                shape = cms.vstring("CBPlusExpo","*pt_bin0*","CBPlusExpo","*pt_bin1*","CBPlusExpo","*pt_bin2*","CBPlusExpo","*pt_bin3*","CBPlusExpo","*pt_bin4*","CBPlusExpo","*pt_bin5*","CBPlusExpo","*pt_bin6*","CBPlusExpo","*pt_bin7*","CBPlusExpo","*pt_bin8*","CBPlusExpo")

            #NOMINAL CASE: ID vs pT fit funtion by default -> two voigtians + CMSshape
            else:
#            else:
                if ('pt' in X):
                    print 'den is', den 
                    print 'num_ is ', num
                    if den == "highptid" or num == "highptid" or den == "trkhighptid" or num == "trkhighptid":
                        if (len(DEN.pair_newTuneP_probe_pt)>0):
                            shape = cms.vstring("vpvPlusCMS","*pt_bin0*","vpvPlusCMS","*pt_bin1*","vpvPlusCMS","*pt_bin2*","vpvPlusCMS","*pt_bin3*","vpvPlusCMSbeta0p2","*pt_bin4*","vpvPlusCMSbeta0p2","*pt_bin5*","vpvPlusCMSbeta0p2","*pt_bin6*","vpvPlusCMSbeta0p2","*pt_bin7*","vpvPlusCMSbeta0p2", "*pt_bin8*","vpvPlusCMSbeta0p2")
                        if scenario == "mc_all":
                            if (len(DEN.pair_newTuneP_probe_pt)>0):
                                shape = cms.vstring("vpvPlusCMSbeta0p2","*pt_bin0*","vpvPlusExpo","*pt_bin1*","vpvPlusExpo","*pt_bin2*","vpvPlusExpo","*pt_bin3*","vpvPlusExpo","*pt_bin4*","vpvPlusCMSbeta0p2","*pt_bin5*","vpvPlusCMSbeta0p2","*pt_bin6*","vpvPlusCMSbeta0p2","*pt_bin7*","vpvPlusCMSbeta0p2", "*pt_bin8*","vpvPlusCMSbeta0p2")

                    else:
                        if (len(DEN.pt)==26):
                            shape = cms.vstring("vpvPlusCMSbeta0p2")
                        if scenario == "mc_all":
                            shape = cms.vstring("vpvPlusCMSbeta0p2")

                        if (len(DEN.pt)>0):
                            shape = cms.vstring("vpvPlusCMSbeta0p2","*pt_bin0*","vpvPlusCMSbeta0p2","*pt_bin1*","vpvPlusCMSbeta0p2","*pt_bin2*","vpvPlusCMSbeta0p2","*pt_bin3*","vpvPlusCMSbeta0p2","*pt_bin4*","vpvPlusCMSbeta0p2","*pt_bin5*","vpvPlusCMSbeta0p2","*pt_bin6*","vpvPlusCMSbeta0p2","*pt_bin7*","vpvPlusCMSbeta0p2","*pt_bin8*","vpvPlusCMSbeta0p2")
                            

        elif bgFitFunction == 'CMSshape':
            if den == "highpt":
                if (len(DEN.pair_newTuneP_probe_pt)==9):
                    shape = cms.vstring("vpvPlusExpo","*pt_bin4*","vpvPlusCMS","*pt_bin5*","vpvPlusCMS","*pt_bin6*","vpvPlusCheb","*pt_bin7*","vpvPlusCheb")
            else:
                if (len(DEN.pt)==9):
                    shape = cms.vstring("vpvPlusExpo","*pt_bin4*","vpvPlusCMS","*pt_bin5*","vpvPlusCheb","*pt_bin6*","vpvPlusCheb", "*pt_bin7*","vpvPlusCheb")

    print 'd3'
    mass_variable ="mass"
    print 'den is', den
    if den == "highptid" or den == "trkhighptid":
        mass_variable = "pair_newTuneP_mass"
    #compute isolation efficiency
    if scenario == 'data_all':
        if num_.find("Iso4") != -1 or num_.find("Iso3") != -1:
            setattr(module.Efficiencies, ID+"_"+X, cms.PSet(
                EfficiencyCategoryAndState = cms.vstring(num_,"below"),
                UnbinnedVariables = cms.vstring(mass_variable),
                BinnedVariables = DEN,
                BinToPDFmap = shape
                ))
        else:
            print 'd4'
            setattr(module.Efficiencies, ID+"_"+X, cms.PSet(
                EfficiencyCategoryAndState = cms.vstring(num_,"above"),
                UnbinnedVariables = cms.vstring(mass_variable),
                BinnedVariables = DEN,
                BinToPDFmap = shape
                ))
        setattr(process, "TnP_MuonID_"+ID+"_"+X, module)
        setattr(process, "run_"+ID+"_"+X, cms.Path(module))
        if num_.find("puppiIso") != -1:
            setattr(module.Efficiencies, ID+"_"+X, cms.PSet(
                    EfficiencyCategoryAndState = cms.vstring(num_,"below"),
                    UnbinnedVariables = cms.vstring(mass_variable),
                    BinnedVariables = DEN,
                    BinToPDFmap = shape
                    ))
    elif scenario == 'mc_all' and par=='vtx':
        print 'MC sample as function of nVertices -> the PU reweighting will not be applied'
        if num_.find("Iso4") != -1 or num_.find("Iso3") != -1:
            setattr(module.Efficiencies, ID+"_"+X, cms.PSet(
                EfficiencyCategoryAndState = cms.vstring(num_,"below"),
                UnbinnedVariables = cms.vstring(mass_variable),
                BinnedVariables = DEN,
                BinToPDFmap = shape
                ))
        else:
            setattr(module.Efficiencies, ID+"_"+X, cms.PSet(
                EfficiencyCategoryAndState = cms.vstring(num_,"above"),
                UnbinnedVariables = cms.vstring(mass_variable),
                BinnedVariables = DEN,
                BinToPDFmap = shape
                ))
        setattr(process, "TnP_MuonID_"+ID+"_"+X, module)
        setattr(process, "run_"+ID+"_"+X, cms.Path(module))
        if num_.find("puppiIso") != -1:
             setattr(module.Efficiencies, ID+"_"+X, cms.PSet(
                    EfficiencyCategoryAndState = cms.vstring(num_,"below"),
                    UnbinnedVariables = cms.vstring(mass_variable),
                        BinnedVariables = DEN,
                    BinToPDFmap = shape
                    ))
    elif scenario == 'mc_all' and par!='vtx':
        # PU reweighting applied for MC when par != vtx
        print 'the PU reweighting will be applied'
        if num_.find("Iso4") != -1 or num_.find("Iso3") != -1:
            setattr(module.Efficiencies, ID+"_"+X, cms.PSet(
                EfficiencyCategoryAndState = cms.vstring(num_,"below"),
                UnbinnedVariables = cms.vstring(mass_variable, "weight"),
                BinnedVariables = DEN,
                BinToPDFmap = shape
                ))
        else:
            setattr(module.Efficiencies, ID+"_"+X, cms.PSet(
                EfficiencyCategoryAndState = cms.vstring(num_,"above"),
                UnbinnedVariables = cms.vstring(mass_variable, "weight"),
                BinnedVariables = DEN,
                BinToPDFmap = shape
                ))
        setattr(process, "TnP_MuonID_"+ID+"_"+X, module)
        setattr(process, "run_"+ID+"_"+X, cms.Path(module))
        if num_.find("puppiIso") != -1:
             setattr(module.Efficiencies, ID+"_"+X, cms.PSet(
                    EfficiencyCategoryAndState = cms.vstring(num_,"below"),
                    UnbinnedVariables = cms.vstring(mass_variable,"weight"),
                        BinnedVariables = DEN,
                    BinToPDFmap = shape
                    ))
