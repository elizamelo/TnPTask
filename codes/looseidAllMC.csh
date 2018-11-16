#!/bin/csh

cmsRun fitMuonJpsi.py Run2016B_H looseid gentrack mc mc_all pt_eta default >& pt_eta_looseid_mc.log &
cmsRun fitMuonJpsi.py Run2016B_H looseid gentrack mc mc_all pt default >& pt_looseid_mc.log &
cmsRun fitMuonJpsi.py Run2016B_H looseid gentrack mc mc_all vtx default>& vtx_looseid_mc.log &
cmsRun fitMuonJpsi.py Run2016B_H looseid gentrack mc mc_all eta default >& eta_looseid_Data.log &

