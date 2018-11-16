#!/bin/csh

cmsRun fitMuonJpsi.py Run2016B_H softid gentrack data data_all pt_eta default >& pt_eta_softid_Data.log &
cmsRun fitMuonJpsi.py Run2016B_H softid gentrack data data_all pt default >& pt_softid_Data.log &
cmsRun fitMuonJpsi.py Run2016B_H softid gentrack data data_all vtx default>& vtx_softid_Data.log &
cmsRun fitMuonJpsi.py Run2016B_H softid gentrack data data_all eta default >& eta_softid_Data.log &



