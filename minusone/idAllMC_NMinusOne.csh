#!/bin/csh
### USAGE: cmsRun fitMuonJpsi_2018.py FOLDER_NAME numerator denominator scenario sample parameter default sysMassRange sysBinChange sysPDFShape
### USAGE: cmsRun fitMuonJpsi_2018.py Run2017B_E_sys looseid gentrack data data_all pt_eta default MassRange_nominal binfit45 Gauss


#Nominal

cmsRun fitMuonJpsi_2018.py Run2018ABCD_MinusOne tightid gentrack mc mc2018_all eta default MassRange_nominal binfit40_nominal CBPlusExpo_nominal >& eta_tightid_MC.log & 

cmsRun fitMuonJpsi_2018.py Run2018ABCD_MinusOne tightid_all gentrack mc mc2018_all eta default MassRange_nominal binfit40_nominal CBPlusExpo_nominal >& eta_tightid_all_MC.log & 


cmsRun fitMuonJpsi_2018.py Run2018ABCD_MinusOne tightid_Glb gentrack mc mc2018_all eta default MassRange_nominal binfit40_nominal CBPlusExpo_nominal >& eta_tightid_Glb_MC.log &  

cmsRun fitMuonJpsi_2018.py Run2018ABCD_MinusOne tightid_PF gentrack mc mc2018_all eta default MassRange_nominal binfit40_nominal CBPlusExpo_nominal >& eta_tightid_PF_MC.log &

cmsRun fitMuonJpsi_2018.py Run2018ABCD_MinusOne tightid_glbChi2 gentrack mc mc2018_all eta default MassRange_nominal binfit40_nominal CBPlusExpo_nominal >& eta_tightid_glbChi2_MC.log &


cmsRun fitMuonJpsi_2018.py Run2018ABCD_MinusOne tightid_glbValidMuHits gentrack mc mc2018_all eta default MassRange_nominal binfit40_nominal CBPlusExpo_nominal >& eta_tightid_glbValidMuHits_MC.log & 

cmsRun fitMuonJpsi_2018.py Run2018ABCD_MinusOne tightid_numberOfMatchedStations gentrack mc mc2018_all eta default MassRange_nominal binfit40_nominal CBPlusExpo_nominal >& eta_tightid_numberOfMatchedStations_MC.log &

cmsRun fitMuonJpsi_2018.py Run2018ABCD_MinusOne tightid_dB gentrack mc mc2018_all eta default MassRange_nominal binfit40_nominal CBPlusExpo_nominal >& eta_tightid_dB_MC.log &

cmsRun fitMuonJpsi_2018.py Run2018ABCD_MinusOne tightid_dzPV gentrack mc mc2018_all eta default MassRange_nominal binfit40_nominal CBPlusExpo_nominal >& eta_tightid_dzPV_MC.log &

cmsRun fitMuonJpsi_2018.py Run2018ABCD_MinusOne tightid_tkValidPixelHits gentrack mc mc2018_all eta default MassRange_nominal binfit40_nominal CBPlusExpo_nominal >& eta tightid_tkValidPixelHits_MC.log &

cmsRun fitMuonJpsi_2018.py Run2018ABCD_MinusOne tightid_tkTrackerLay gentrack mc mc2018_all eta default MassRange_nominal binfit40_nominal CBPlusExpo_nominal >& eta_tightid_tkTrackerLay_MC.log &

cmsRun fitMuonJpsi_2018.py Run2018ABCD_MinusOne tightid_tkValidPixelHits_tkTrackerLay gentrack mc mc2018_all eta default MassRange_nominal binfit40_nominal CBPlusExpo_nominal >& eta_tightid_tkValidPixelHits_tkTrackerLay_MC.log &

cmsRun fitMuonJpsi_2018.py Run2018ABCD_MinusOne tightid_glbValidMuHits_numberOfMatchedStations gentrack mc mc2018_all eta default MassRange_nominal binfit40_nominal CBPlusExpo_nominal >& eta_tightid_glbValidMuHits_numberOfMatchedStations_MC.log &

cmsRun fitMuonJpsi_2018.py Run2018ABCD_MinusOne tightid_glbChi2_dB_dzPV gentrack mc mc2018_all eta default MassRange_nominal binfit40_nominal CBPlusExpo_nominal >& eta_tightid_glbChi2_dB_dzPV_MC.log &






#cmsRun fitMuonJpsi_2018.py Run2018ABCD looseid gentrack data data_all pt default >& pt_looseid_MC.log &
#cmsRun fitMuonJpsi_2018.py Run2018ABCD looseid gentrack data data_all vtx default>& vtx_loosetid_MC.log &
#cmsRun fitMuonJpsi_2018.py Run2018ABCD looseid gentrack data data_all eta default >& eta_looseid_MC.log &

