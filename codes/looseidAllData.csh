#!/bin/csh


cmsRun fitMuonJpsi.py Run2016B_H looseid gentrack data data_all pt_eta default >& pt_eta_looseid_Data.log &
cmsRun fitMuonJpsi.py Run2016B_H looseid gentrack data data_all pt default >& pt_looseid_Data.log &
cmsRun fitMuonJpsi.py Run2016B_H looseid gentrack data data_all vtx default>& vtx_loosetid_Data.log &
cmsRun fitMuonJpsi.py Run2016B_H looseid gentrack data data_all eta default >& eta_looseid_Data.log &

