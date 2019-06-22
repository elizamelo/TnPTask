#!/bin/csh
### USAGE: cmsRun fitMuonJpsi_2018.py FOLDER_NAME numerator denominator scenario sample parameter default sysMassRange sysBinChange sysPDFShape
### USAGE: cmsRun fitMuonJpsi_2018.py Run2017B_E_sys looseid gentrack data data2018_all pt_eta default MassRange_nominal binfit45 Gauss


#Nominal

cmsRun fitMuonJpsi_2018.py Run2018ABCD_MinusOne tightid gentrack data data2018_all eta default MassRange_nominal binfit40_nominal CBPlusExpo_nominal >& eta_tightid_Data.log & 

cmsRun fitMuonJpsi_2018.py Run2018ABCD_MinusOne tightid_all gentrack data data2018_all eta default MassRange_nominal binfit40_nominal CBPlusExpo_nominal >& eta_tightid_all_Data.log & 


cmsRun fitMuonJpsi_2018.py Run2018ABCD_MinusOne tightid_Glb gentrack data data2018_all eta default MassRange_nominal binfit40_nominal CBPlusExpo_nominal >& eta_tightid_Glb_Data.log &  

cmsRun fitMuonJpsi_2018.py Run2018ABCD_MinusOne tightid_PF gentrack data data2018_all eta default MassRange_nominal binfit40_nominal CBPlusExpo_nominal >& eta_tightid_PF_Data.log &

cmsRun fitMuonJpsi_2018.py Run2018ABCD_MinusOne tightid_glbChi2 gentrack data data2018_all eta default MassRange_nominal binfit40_nominal CBPlusExpo_nominal >& eta_tightid_glbChi2_Data.log &


cmsRun fitMuonJpsi_2018.py Run2018ABCD_MinusOne tightid_glbValidMuHits gentrack data data2018_all eta default MassRange_nominal binfit40_nominal CBPlusExpo_nominal >& eta_tightid_glbValidMuHits_Data.log & 

cmsRun fitMuonJpsi_2018.py Run2018ABCD_MinusOne tightid_numberOfMatchedStations gentrack data data2018_all eta default MassRange_nominal binfit40_nominal CBPlusExpo_nominal >& eta_tightid_numberOfMatchedStations_Data.log &

cmsRun fitMuonJpsi_2018.py Run2018ABCD_MinusOne tightid_dB gentrack data data2018_all eta default MassRange_nominal binfit40_nominal CBPlusExpo_nominal >& eta_tightid_dB_Data.log &

cmsRun fitMuonJpsi_2018.py Run2018ABCD_MinusOne tightid_dzPV gentrack data data2018_all eta default MassRange_nominal binfit40_nominal CBPlusExpo_nominal >& eta_tightid_dzPV_Data.log &

cmsRun fitMuonJpsi_2018.py Run2018ABCD_MinusOne tightid_tkValidPixelHits gentrack data data2018_all eta default MassRange_nominal binfit40_nominal CBPlusExpo_nominal >& eta_tightid_tkValidPixelHits_Data.log &

cmsRun fitMuonJpsi_2018.py Run2018ABCD_MinusOne tightid_tkTrackerLay gentrack data data2018_all eta default MassRange_nominal binfit40_nominal CBPlusExpo_nominal >& eta_tightid_tkTrackerLay_Data.log &

cmsRun fitMuonJpsi_2018.py Run2018ABCD_MinusOne tightid_tkValidPixelHits_tkTrackerLay gentrack data data2018_all eta default MassRange_nominal binfit40_nominal CBPlusExpo_nominal >& eta_tightid_tkValidPixelHits_tkTrackerLay_Data.log &

cmsRun fitMuonJpsi_2018.py Run2018ABCD_MinusOne tightid_glbValidMuHits_numberOfMatchedStations gentrack data data2018_all eta default MassRange_nominal binfit40_nominal CBPlusExpo_nominal >& eta_tightid_glbValidMuHits_numberOfMatchedStations_Data.log &

cmsRun fitMuonJpsi_2018.py Run2018ABCD_MinusOne tightid_glbChi2_dB_dzPV gentrack data data2018_all eta default MassRange_nominal binfit40_nominal CBPlusExpo_nominal >& eta_tightid_glbChi2_dB_dzPV_Data.log &





