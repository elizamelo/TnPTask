#!/bin/csh

cmsRun fitMuonJpsi.py Run2016B_H tightid gentrack mc mc_all pt_eta default >& pt_eta_tightid_mc.log &
cmsRun fitMuonJpsi.py Run2016B_H tightid gentrack mc mc_all pt default >& pt_tightid_mc.log &
cmsRun fitMuonJpsi.py Run2016B_H tightid gentrack mc mc_all vtx default>& vtx_tightid_mc.log &
cmsRun fitMuonJpsi.py Run2016B_H tightid gentrack mc mc_all eta default >& eta_tightid_mc.log &


